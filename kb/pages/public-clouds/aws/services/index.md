---
layout: doc
title: "Services"
render_with_liquid: false
description: "Overview of key AWS services and deployment methods"
---

This section contains detailed guides for deploying and managing common AWS services using both Terraform and the AWS CLI on Linux environments.

## Container Services

- [Amazon EKS (Elastic Kubernetes Service)](eks.html) - Managed Kubernetes service
- [Amazon ECS (Elastic Container Service)](ecs.html) - Container orchestration service
- [Amazon ECR (Elastic Container Registry)](ecr.html) - Docker container registry

## Compute Services

- [Amazon EC2 (Elastic Compute Cloud)](ec2.md) - Virtual servers in the cloud
- [AWS Lambda](lambda.md) - Serverless compute service

## Storage Services

- [Amazon S3 (Simple Storage Service)](s3.html) - Object storage service
- [Amazon EBS (Elastic Block Store)](ebs.md) - Block storage for EC2

## Database Services

- [Amazon RDS (Relational Database Service)](rds.md) - Managed relational databases
- [Amazon DynamoDB](dynamodb.md) - Managed NoSQL database

## Networking Services

- [Amazon VPC (Virtual Private Cloud)](vpc.md) - Isolated cloud resources
- [Amazon CloudFront](cloudfront.md) - Content delivery network
- [Amazon Route 53](route53.html) - DNS and domain management

## Security & Identity Services

- [AWS IAM (Identity and Access Management)](iam.html) - User and permissions management

## Monitoring & Messaging Services

- [Amazon CloudWatch](cloudwatch.html) - Monitoring and observability
- [Amazon SNS (Simple Notification Service)](sns.html) - Pub/sub messaging
- [Amazon SQS (Simple Queue Service)](sqs.html) - Managed message queues

## Application Services

- [AWS Elastic Beanstalk](elastic-beanstalk.html) - Platform as a Service (PaaS)
- [AWS Batch](batch.html) - Batch computing at scale

## GenAI & ML Services

- [Amazon SageMaker](sagemaker.html) - Machine learning platform
- [Amazon Bedrock](bedrock.html) - Generative AI foundation models
- [Amazon Comprehend](comprehend.html) - Natural language processing

## Each guide includes:

1. Service overview and key concepts
2. Terraform deployment examples
3. AWS CLI deployment commands
4. Best practices
5. Common issues and troubleshooting

These guides are designed to help you deploy AWS resources programmatically using Infrastructure as Code (IaC) principles with Terraform or command-line automation with AWS CLI.
