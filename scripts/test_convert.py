#!/usr/bin/env python3
"""Unit tests for the GitBook -> Jekyll converter."""

import unittest
import convert as c


class TestBlocks(unittest.TestCase):
    def test_hint_info(self):
        out = c.convert_hints('{% hint style="info" %}\nBe careful.\n{% endhint %}')
        self.assertIn('class="callout callout-info"', out)
        self.assertIn("Be careful.", out)
        self.assertIn('markdown="1"', out)

    def test_hint_tip_maps_to_success(self):
        out = c.convert_hints('{% hint style="tip" %}\nNice.\n{% endhint %}')
        self.assertIn("callout-success", out)

    def test_hint_unknown_style_falls_back_info(self):
        out = c.convert_hints('{% hint style="weird" %}\nx\n{% endhint %}')
        self.assertIn("callout-info", out)

    def test_tabs(self):
        src = (
            "{% tabs %}\n"
            '{% tab title="Linux" %}\nrun a\n{% endtab %}\n'
            '{% tab title="macOS" %}\nrun b\n{% endtab %}\n'
            "{% endtabs %}"
        )
        out = c.convert_tabs(src)
        self.assertIn('class="tabs"', out)
        self.assertIn("<button", out)
        self.assertEqual(out.count("tab-panel"), 2)
        self.assertIn("Linux", out)
        self.assertIn("macOS", out)

    def test_code_block_tags_stripped(self):
        src = '{% code title="x.sh" %}\n```bash\necho hi\n```\n{% endcode %}'
        out = c.convert_misc_blocks(src)
        self.assertNotIn("{% code", out)
        self.assertNotIn("endcode", out)
        self.assertIn("echo hi", out)

    def test_content_ref(self):
        src = '{% content-ref url="foo.md" %}\nlabel\n{% endcontent-ref %}'
        out = c.convert_misc_blocks(src)
        self.assertIn("foo.md", out)
        self.assertNotIn("content-ref", out)


class TestFrontMatter(unittest.TestCase):
    def test_strip(self):
        meta, body = c.strip_front_matter(
            "---\ndescription: Hello world\ncover: x.png\n---\n\n# Title\n\nBody"
        )
        self.assertEqual(meta.get("description"), "Hello world")
        self.assertTrue(body.startswith("# Title"))

    def test_no_front_matter(self):
        meta, body = c.strip_front_matter("# Title\n\nBody")
        self.assertEqual(meta, {})
        self.assertTrue(body.startswith("# Title"))


class TestPaths(unittest.TestCase):
    def test_readme_to_index(self):
        self.assertEqual(c.out_rel_for("pages/sre/README.md"), "pages/sre/index.md")

    def test_plain_md(self):
        self.assertEqual(c.out_rel_for("pages/sre/toil.md"), "pages/sre/toil.md")

    def test_url_for(self):
        self.assertEqual(c.url_for("pages/sre/toil.md"), "/kb/pages/sre/toil.html")
        self.assertEqual(c.url_for("pages/sre/README.md"), "/kb/pages/sre/index.html")

    def test_rel_path(self):
        self.assertEqual(c.rel_path("pages/a/b.md", "kb/img/x.png"), "../../kb/img/x.png")


class TestSummary(unittest.TestCase):
    def test_parse(self):
        import tempfile
        import os
        text = (
            "# Table of contents\n\n"
            "- [Welcome](README.md)\n\n"
            "## Section One\n\n"
            "- [Parent](pages/p.md)\n"
            "  - [Child](pages/c.md)\n"
        )
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as f:
            f.write(text)
            name = f.name
        try:
            from pathlib import Path
            sections, refs = c.parse_summary(Path(name))
            titles = [s["title"] for s in sections]
            self.assertIn("Section One", titles)
            self.assertIn("pages/p.md", refs)
            self.assertIn("pages/c.md", refs)
            sec = [s for s in sections if s["title"] == "Section One"][0]
            self.assertEqual(sec["children"][0]["title"], "Parent")
            self.assertEqual(sec["children"][0]["children"][0]["title"], "Child")
        finally:
            os.unlink(name)


if __name__ == "__main__":
    unittest.main(verbosity=2)
