import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="s3_indexer",
    version="0.0.1",

    description="An empty CDK Python app",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="author",

    package_dir={"": "s3_indexer"},
    packages=setuptools.find_packages(where="s3_indexer"),

    install_requires=[
        'aws-cdk.core==1.116.0',
        'aws-cdk.assets==1.116.0',
        'aws-cdk.aws-apigateway==1.116.0',
        'aws-cdk.aws-applicationautoscaling==1.116.0',
        'aws-cdk.aws-autoscaling-common==1.116.0',
        'aws-cdk.aws-certificatemanager==1.116.0',
        'aws-cdk.aws-cloudformation==1.116.0',
        'aws-cdk.aws-cloudwatch==1.116.0',
        'aws-cdk.aws-codeguruprofiler==1.116.0',
        'aws-cdk.aws-codestarnotifications==1.116.0',
        'aws-cdk.aws-cognito==1.116.0',
        'aws-cdk.aws-dynamodb==1.116.0',
        'aws-cdk.aws-ec2==1.116.0',
        'aws-cdk.aws-ecr==1.116.0',
        'aws-cdk.aws-ecr-assets==1.116.0',
        'aws-cdk.aws-efs==1.116.0',
        'aws-cdk.aws-elasticloadbalancingv2==1.116.0',
        'aws-cdk.aws-events==1.116.0',
        'aws-cdk.aws-iam==1.116.0',
        'aws-cdk.aws-kinesis==1.116.0',
        'aws-cdk.aws-kms==1.116.0',
        'aws-cdk.aws-lambda==1.116.0',
        'aws-cdk.aws-lambda-event-sources==1.116.0',
        'aws-cdk.aws-logs==1.116.0',
        'aws-cdk.aws-route53==1.116.0',
        'aws-cdk.aws-s3==1.116.0',
        'aws-cdk.aws-s3-assets==1.116.0',
        'aws-cdk.aws-s3-notifications==1.116.0',
        'aws-cdk.aws-sam==1.116.0',
        'aws-cdk.aws-secretsmanager==1.116.0',
        'aws-cdk.aws-signer==1.116.0',
        'aws-cdk.aws-sns==1.116.0',
        'aws-cdk.aws-sns-subscriptions==1.116.0',
        'aws-cdk.aws-sqs==1.116.0',
        'aws-cdk.aws-ssm==1.116.0',
        'aws-cdk.cloud-assembly-schema==1.116.0',
        'aws-cdk.custom-resources==1.116.0',
        'aws-cdk.cx-api==1.116.0',
        'aws-cdk.region-info==1.116.0'
    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)
