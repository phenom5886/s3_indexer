
# S3 DynamoDB Index!
## Overview
A CDK project that deploys an integrated serverless infrastructure to maintain an index 
of S3 objects in DynamoDB. The purpose of this is to allow for real-time reporting & monitoring 
of assets stored in the S3 bucket.

Infrastructure deployed:

- An S3 bucket
- A DynamoDB Table
- Lambda Function
- Necessary IAM permissions
- Event integrations 

## DynamoDB Table Structure
The DynamoDB table is simple in the initial state. 

Sort Key: s3_key (S)

Additional fields stored:

- content_type: Object MIME type
- e_tag: Object MD5 hash
- size: Object size (Bytes)

Additional secondary indexes can be created to allow better searching on additional fields.

## Configuration
You can set the following input parameters in the config.yml file:

- S3 bucket name
- DynamoDB table name
- DynamoDB read/write capacity
- Reserved concurrency for Lambda function

## Setup & Deployment
First install all requirements:

```
$ pip install -r requirements.txt
```
Then you can deploy:
```
$ cdk deploy 
```

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
