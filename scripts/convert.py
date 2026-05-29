#!/usr/bin/env python3
"""
GitBook -> Jekyll converter for WWW-Freundcloud.

Reads the GitBook wiki (default /mnt/data/Source/wiki) and writes Jekyll-ready
markdown under kb/, plus _data/toc.yml (sidebar nav) and kb/img/ (assets).

Design choices that keep links working without hardcoding the site baseurl:
  * The source tree is mirrored 1:1 under kb/, so existing *relative* links
    between pages keep pointing at the right files.
  * Page permalinks preserve the path with an .html extension (set in
    _config.yml for the kb scope), so `../sre/toil.md` -> `../sre/toil.html`
    resolves correctly.
  * README.md -> index.md (and links to README.md -> index.html).
  * Images are copied to kb/img/ and rewritten as paths *relative to each file*,
    so they work locally and under /WWW-Freundcloud alike.

Everything is idempotent: kb/ and _data/toc.yml are regenerated each run.

Usage:
    python3 scripts/convert.py [--wiki PATH] [--out PATH] [--report PATH]
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import sys
from pathlib import Path

# Directories in the wiki that are NOT content and must be skipped entirely.
EXCLUDE_DIRS = {
    ".git", ".github", ".gitbook", "_book", "_snippets", ".npm-global",
    "node_modules", "scripts", "vendor", ".bundle",
}

# Root-level markdown files we don't migrate into the KB (handled as bespoke
# me-first pages, or simply not wanted).
EXCLUDE_FILES = {
    "SUMMARY.md", "README.md", "CLAUDE.md", "CONTRIBUTING.md", "TODO.md",
    "GITBOOK-BEST-PRACTICES.md", "404.md", "about-me.md", "cv.md",
}

# Specific wiki-relative paths to skip — the site has bespoke, humanized
# /about/ and /cv/ pages, so the GitBook originals are not migrated.
EXCLUDE_RELPATHS = {
    "pages/about-me.md",
    "pages/cv.md",
}

HINT_STYLE_MAP = {
    "info": "info", "tip": "success", "success": "success",
    "warning": "warning", "danger": "danger", "note": "info",
}

stats = {
    "pages": 0, "block_files": 0, "assets": 0,
    "links_rewritten": 0, "images_rewritten": 0, "readme_collisions": 0,
}
audit: list[str] = []


# --------------------------------------------------------------------------- #
# SUMMARY.md -> nav tree
# --------------------------------------------------------------------------- #
def parse_summary(summary_path: Path):
    """Parse SUMMARY.md into a list of sections.

    Returns (sections, referenced_links) where sections is:
      [{title, children: [{title, link, depth, children: [...]}]}]
    Top-level `## Heading` lines start a new section; `# Table of contents`
    is ignored. List items become nav entries nested by indentation.
    """
    sections: list[dict] = []
    referenced: set[str] = set()
    current = {"title": "Knowledge Base", "children": []}
    # Stack of (indent, node) for nesting list items.
    stack: list[tuple[int, dict]] = []

    line_re = re.compile(r"^(?P<indent>\s*)[-*]\s+\[(?P<title>.*?)\]\((?P<link>.*?)\)")
    head_re = re.compile(r"^##\s+(?P<title>.+?)\s*$")

    for raw in summary_path.read_text(encoding="utf-8").splitlines():
        h = head_re.match(raw)
        if h:
            if current["children"]:
                sections.append(current)
            current = {"title": h.group("title").strip(), "children": []}
            stack = []
            continue

        m = line_re.match(raw)
        if not m:
            continue
        indent = len(m.group("indent").expandtabs(2))
        link = m.group("link").strip()
        title = m.group("title").strip()
        # Strip anchor / fragment-only refs for the nav URL mapping.
        clean_link = link.split("#")[0]
        if clean_link:
            referenced.add(clean_link)
        node = {"title": title, "link": clean_link, "anchor": link, "children": []}

        # Find parent by indentation.
        while stack and stack[-1][0] >= indent:
            stack.pop()
        if stack:
            stack[-1][1]["children"].append(node)
        else:
            current["children"].append(node)
        stack.append((indent, node))

    if current["children"]:
        sections.append(current)
    return sections, referenced


# --------------------------------------------------------------------------- #
# Path mapping
# --------------------------------------------------------------------------- #
def out_rel_for(src_rel: str) -> str:
    """Map a wiki-relative .md path to its kb/-relative output path."""
    p = src_rel
    if p.lower().endswith("readme.md"):
        p = p[: -len("README.md")] + "index.md"
    return p


def url_for(src_rel: str) -> str:
    """Built URL (root-relative, no baseurl) for a wiki-relative .md path."""
    out = out_rel_for(src_rel)
    return "/kb/" + out[:-3] + ".html"  # .md -> .html


# --------------------------------------------------------------------------- #
# Content transforms
# --------------------------------------------------------------------------- #
def strip_front_matter(text: str) -> tuple[dict, str]:
    """Remove a leading GitBook YAML front matter block; return (meta, body)."""
    meta = {}
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            block = text[3:end]
            body = text[end + 4:]
            for line in block.splitlines():
                if ":" in line and not line.strip().startswith("#"):
                    k, _, v = line.partition(":")
                    meta[k.strip()] = v.strip()
            return meta, body.lstrip("\n")
    return meta, text


def first_h1(body: str) -> str | None:
    m = re.search(r"^#\s+(.+?)\s*$", body, re.MULTILINE)
    return m.group(1).strip() if m else None


def convert_hints(text: str) -> str:
    def repl(m):
        style = (m.group("style") or "info").lower()
        cls = HINT_STYLE_MAP.get(style, "info")
        inner = m.group("body").strip("\n")
        return f'<div class="callout callout-{cls}" markdown="1">\n{inner}\n</div>'
    # Styled hints: {% hint style="info" %} ... {% endhint %}
    styled = re.compile(
        r'{%\s*hint\s+style="(?P<style>[^"]*)"\s*%}(?P<body>.*?){%\s*endhint\s*%}',
        re.DOTALL,
    )
    text = styled.sub(repl, text)

    # Unstyled hints: {% hint %} ... {% endhint %}
    def repl_plain(m):
        inner = m.group("body").strip("\n")
        return f'<div class="callout callout-info" markdown="1">\n{inner}\n</div>'
    plain = re.compile(r"{%\s*hint\s*%}(?P<body>.*?){%\s*endhint\s*%}", re.DOTALL)
    return plain.sub(repl_plain, text)


def convert_tabs(text: str) -> str:
    tab_re = re.compile(
        r'{%\s*tab\s+title="(?P<title>[^"]*)"\s*%}(?P<body>.*?){%\s*endtab\s*%}',
        re.DOTALL,
    )

    def repl(m):
        block = m.group("body")
        tabs = list(tab_re.finditer(block))
        if not tabs:
            return block
        buttons, panels = [], []
        for i, t in enumerate(tabs):
            active = " active" if i == 0 else ""
            buttons.append(f'<button class="{active.strip()}">{t.group("title")}</button>')
            panels.append(
                f'<div class="tab-panel{active}" markdown="1">\n'
                f'{t.group("body").strip(chr(10))}\n</div>'
            )
        return (
            '<div class="tabs">\n<div class="tab-buttons">'
            + "".join(buttons)
            + "</div>\n"
            + "\n".join(panels)
            + "\n</div>"
        )

    pattern = re.compile(r"{%\s*tabs\s*%}(?P<body>.*?){%\s*endtabs\s*%}", re.DOTALL)
    return pattern.sub(repl, text)


def convert_misc_blocks(text: str) -> str:
    # {% code ... %} ... {% endcode %} -> keep inner (fenced code stays).
    text = re.sub(r"{%\s*code[^%]*%}", "", text)
    text = re.sub(r"{%\s*endcode\s*%}", "", text)

    # {% content-ref url="X" %} label {% endcontent-ref %} -> link.
    def ref_repl(m):
        url = m.group("url")
        return f"\n[{url}]({url})\n"
    text = re.sub(
        r'{%\s*content-ref\s+url="(?P<url>[^"]*)"\s*%}.*?{%\s*endcontent-ref\s*%}',
        ref_repl, text, flags=re.DOTALL,
    )

    # {% embed url="X" %} -> link.
    text = re.sub(r'{%\s*embed\s+url="(?P<url>[^"]*)"\s*%}',
                  lambda m: f"\n<{m.group('url')}>\n", text)

    # {% file src="X" %} -> link.
    text = re.sub(r'{%\s*file\s+src="(?P<src>[^"]*)"\s*%}',
                  lambda m: f"\n[Download]({m.group('src')})\n", text)
    return text


def strip_leftover_liquid(text: str, src_rel: str) -> str:
    leftovers = re.findall(r"{%-?\s*\w[^%]*%}", text)
    if leftovers:
        audit.append(f"LEFTOVER LIQUID in {src_rel}: {sorted(set(leftovers))[:5]}")
    text = re.sub(r"{%-?\s*[^%]*%}", "", text)
    return text


def rel_path(from_out_rel: str, to_kb_rel: str) -> str:
    """Relative path from one kb/ output file to another kb/ resource."""
    from_dir = os.path.dirname(from_out_rel)
    rp = os.path.relpath(to_kb_rel, from_dir or ".")
    return rp.replace(os.sep, "/")


def rewrite_images(body: str, src_rel: str, out_rel: str, wiki: Path,
                   asset_map: dict[str, str]) -> str:
    """Rewrite markdown + <img> image refs to relative paths into kb/img/."""
    src_dir = os.path.dirname(src_rel)

    def resolve(ref: str) -> str | None:
        ref = ref.split("#")[0].split("?")[0].strip()
        if not ref or ref.startswith(("http://", "https://", "data:", "mailto:")):
            return None
        target = os.path.normpath(os.path.join(src_dir, ref))
        kb_img = asset_map.get(target.replace(os.sep, "/"))
        if kb_img:
            return rel_path(out_rel, kb_img)
        return None

    def md_repl(m):
        alt, ref = m.group("alt"), m.group("ref")
        new = resolve(ref)
        if new:
            stats["images_rewritten"] += 1
            return f"![{alt}]({new})"
        return m.group(0)

    body = re.sub(r"!\[(?P<alt>[^\]]*)\]\((?P<ref>[^)]+)\)", md_repl, body)

    def img_repl(m):
        ref = m.group("ref")
        new = resolve(ref)
        if new:
            stats["images_rewritten"] += 1
            return m.group(0).replace(ref, new)
        return m.group(0)

    body = re.sub(r'<img[^>]*src="(?P<ref>[^"]+)"[^>]*>', img_repl, body)
    return body


def rewrite_links(body: str, src_rel: str, out_rel: str,
                  known: set[str]) -> str:
    """Rewrite intra-repo .md links to the mirrored .html output paths."""
    src_dir = os.path.dirname(src_rel)

    def repl(m):
        text, ref = m.group("text"), m.group("ref")
        raw = ref.strip()
        if raw.startswith(("http://", "https://", "mailto:", "#", "tel:")):
            return m.group(0)
        anchor = ""
        if "#" in raw:
            raw, anchor = raw.split("#", 1)
            anchor = "#" + anchor
        if not raw.endswith(".md"):
            return m.group(0)
        target = os.path.normpath(os.path.join(src_dir, raw)).replace(os.sep, "/")
        if target not in known:
            audit.append(f"BROKEN LINK in {src_rel}: -> {ref}")
            return m.group(0)
        target_out = out_rel_for(target)
        new = rel_path(out_rel, target_out)[:-3] + ".html"
        stats["links_rewritten"] += 1
        return f"[{text}]({new}{anchor})"

    return re.sub(r"\[(?P<text>[^\]]*)\]\((?P<ref>[^)]+)\)", repl, body)


def yaml_escape(s: str) -> str:
    # Backslash first, then quotes — titles carry markdown-escaped brackets
    # like \[BEGINNER\] which are invalid escapes in a double-quoted scalar.
    return s.replace("\\", "\\\\").replace('"', '\\"')


# --------------------------------------------------------------------------- #
# Asset copy
# --------------------------------------------------------------------------- #
def copy_assets(wiki: Path, out_root: Path) -> dict[str, str]:
    """Copy asset trees into kb/img/, return {wiki_rel_path -> kb_rel_path}."""
    asset_map: dict[str, str] = {}
    img_root = out_root / "img"
    sources = [(".gitbook/assets", "gitbook"), ("assets", "assets")]
    exts = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".ico", ".pdf"}
    for sub, dest in sources:
        base = wiki / sub
        if not base.is_dir():
            continue
        for f in base.rglob("*"):
            if f.is_file() and f.suffix.lower() in exts:
                rel = f.relative_to(base)
                kb_rel = f"img/{dest}/{rel.as_posix()}"
                dst = img_root / dest / rel
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(f, dst)
                # Values are kb/-relative (no "kb/" prefix) to match out_rel.
                asset_map[f.relative_to(wiki).as_posix()] = kb_rel
                stats["assets"] += 1
    return asset_map


# --------------------------------------------------------------------------- #
# Nav emission
# --------------------------------------------------------------------------- #
def emit_toc(sections, valid_targets: set[str]) -> str:
    lines = ["# Generated by scripts/convert.py from the GitBook SUMMARY.md.",
             "# Do not edit by hand; re-run the converter instead."]

    def node_lines(node, indent):
        # Drop excluded leaf pages (bespoke /about/ and /cv/) from the nav.
        if node.get("link") in EXCLUDE_RELPATHS and not node.get("children"):
            return
        pad = "  " * indent
        title = yaml_escape(node["title"])
        link = node.get("link")
        if link and link in valid_targets:
            url = url_for(link)
            lines.append(f'{pad}- title: "{title}"')
            lines.append(f'{pad}  url: "{url}"')
        else:
            lines.append(f'{pad}- title: "{title}"')
        if node.get("children"):
            lines.append(f"{pad}  children:")
            for c in node["children"]:
                node_lines(c, indent + 2)

    for sec in sections:
        lines.append(f'- title: "{yaml_escape(sec["title"])}"')
        if sec["children"]:
            lines.append("  children:")
            for c in sec["children"]:
                node_lines(c, 2)
    return "\n".join(lines) + "\n"


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--wiki", default="/mnt/data/Source/wiki")
    ap.add_argument("--out", default=str(Path(__file__).resolve().parent.parent / "kb"))
    ap.add_argument("--data", default=str(Path(__file__).resolve().parent.parent / "_data" / "toc.yml"))
    ap.add_argument("--report", default=str(Path(__file__).resolve().parent.parent / "docs" / "plans" / "link-audit.txt"))
    args = ap.parse_args()

    wiki = Path(args.wiki).resolve()
    out_root = Path(args.out).resolve()
    if not wiki.is_dir():
        sys.exit(f"wiki not found: {wiki}")

    # Clean output for idempotency.
    if out_root.exists():
        # Preserve a hand-written kb/index.md.
        keep = (out_root / "index.md").read_text(encoding="utf-8") if (out_root / "index.md").exists() else None
        shutil.rmtree(out_root)
    else:
        keep = None
    out_root.mkdir(parents=True, exist_ok=True)
    if keep is not None:
        (out_root / "index.md").write_text(keep, encoding="utf-8")

    # 1. Collect content markdown files.
    md_files: list[str] = []
    for root, dirs, files in os.walk(wiki):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        for fn in files:
            if not fn.endswith(".md"):
                continue
            rel = os.path.relpath(os.path.join(root, fn), wiki).replace(os.sep, "/")
            if "/" not in rel and fn in EXCLUDE_FILES:
                continue
            if rel in EXCLUDE_RELPATHS:
                continue
            md_files.append(rel)
    known = set(md_files)

    # 2. SUMMARY -> nav.
    summary = wiki / "SUMMARY.md"
    sections, referenced = parse_summary(summary) if summary.exists() else ([], set())

    # 3. Assets.
    asset_map = copy_assets(wiki, out_root)

    # 4. Build title map from SUMMARY for nicer page titles.
    summary_titles: dict[str, str] = {}
    def walk_titles(nodes):
        for n in nodes:
            if n.get("link"):
                summary_titles.setdefault(n["link"], n["title"])
            walk_titles(n.get("children", []))
    for sec in sections:
        walk_titles(sec["children"])

    # 5. Convert each page.
    written_targets: set[str] = set()
    for src_rel in md_files:
        text = (wiki / src_rel).read_text(encoding="utf-8", errors="replace")
        had_blocks = "{%" in text
        meta, body = strip_front_matter(text)

        title = summary_titles.get(src_rel) or first_h1(body) or \
            Path(src_rel).stem.replace("-", " ").replace("_", " ").title()
        # Drop a leading duplicate H1 (the doc layout renders page.title).
        body = re.sub(r"^#\s+.+?\n", "", body, count=1)

        body = convert_hints(body)
        body = convert_tabs(body)
        body = convert_misc_blocks(body)
        body = rewrite_images(body, src_rel, out_rel_for(src_rel), wiki, asset_map)
        body = rewrite_links(body, src_rel, out_rel_for(src_rel), known)
        body = strip_leftover_liquid(body, src_rel)

        out_rel = out_rel_for(src_rel)
        out_path = out_root / out_rel
        out_path.parent.mkdir(parents=True, exist_ok=True)
        if out_path.exists() and out_path.name == "index.md":
            stats["readme_collisions"] += 1
            audit.append(f"README/index collision kept first: {out_rel}")
            continue

        fm = ["---", "layout: doc", f'title: "{yaml_escape(title)}"',
              # Belt-and-braces: never let Liquid parse migrated technical
              # docs (Helm/Go templates/shell contain {{ }} and {% %}).
              "render_with_liquid: false"]
        desc = meta.get("description")
        if desc:
            fm.append(f'description: "{yaml_escape(desc.strip())[:180]}"')
        fm.append("---")
        out_path.write_text("\n".join(fm) + "\n\n" + body.strip() + "\n", encoding="utf-8")
        stats["pages"] += 1
        if had_blocks:
            stats["block_files"] += 1
        written_targets.add(src_rel)

    # 6. Nav data file (only link to pages we actually wrote).
    Path(args.data).parent.mkdir(parents=True, exist_ok=True)
    Path(args.data).write_text(emit_toc(sections, written_targets), encoding="utf-8")

    # 7. Audit report.
    Path(args.report).parent.mkdir(parents=True, exist_ok=True)
    report = [
        "# GitBook -> Jekyll conversion report",
        "",
        f"wiki:   {wiki}",
        f"output: {out_root}",
        "",
        "## Counts",
    ] + [f"  {k}: {v}" for k, v in stats.items()] + [
        "",
        f"## Audit findings ({len(audit)})",
    ] + (audit if audit else ["  (none)"])
    Path(args.report).write_text("\n".join(report) + "\n", encoding="utf-8")

    print("Conversion complete.")
    for k, v in stats.items():
        print(f"  {k}: {v}")
    print(f"  audit findings: {len(audit)} (see {args.report})")


if __name__ == "__main__":
    main()
