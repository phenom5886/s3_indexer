
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
Partition Key: s3_key (String)

Additional fields stored:

- content_type: Object MIME type (String)
- e_tag: Object MD5 hash (String)
- size: Object size in Bytes (Number)
- creation_date: Object creation date/time stamp (String)

A Global Secondary Index is created with the Hash Key of content_type. This is to facilitate 
easy querying of files based on object type via selects rather than scans. 

## Configuration
You can set the following input parameters in the config.yml file:

- S3 bucket name
- DynamoDB table name
- DynamoDB billing mode (PROVISIONED or PAY_PER_REQUEST)
- DynamoDB read/write capacity (only required if you configure PROVISIONED billing mode)
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
