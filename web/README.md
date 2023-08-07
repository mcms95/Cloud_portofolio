# Cloud_resume_challenge

Thing to learn while doing the project:

● Full-stack software development (the
static website and Python pieces)

● Version control (the Github piece)

● Infrastructure as code (the
CloudFormation / SAM piece)

● Continuous integration and delivery
(connecting GitHub Actions, SAM, and
AWS)

● Cloud services and “serverless”
(Lambda, API Gateway, DynamoDB,
Route53, CloudFront, S3)

● Application security (IAM, S3 policies,
CORS, API authentication/authorization)

● Networking, as in the way computers
talk to each other (DNS, CDNs, the
whole "cloud" thing)

● Networking, as in the way people talk to
each other (the blog post, the Discord
community - this is probably the
highest-value step in the whole
challenge because of the professional
doors it can unlock for you, and we'll talk
about that in more detail later on.)


AWS SAM - Serverless Aplication Model

Serverless explanation -> "Something happend's, we react"

2 parts:

1 - Transform templates - IaC
- Shortdhand syntax expresses resources and event source mappings
- It provides infrastructure as code for serverlesss aplications 
- We can use any Cloudformation resources in SAM (is built on top of cloudformation)

2 - SAM CLI 
Provides tooling for local development with rapid iteration, debugging, build, packaging, and deployment for serverless applications
(built specifactly for serverless)


AWS SAM transform template:
Lambda function
IAM role
API Gateway
Dyanmo Db

There are 8 serverless resource types:

AWS::Serverless::Function
AWS::Serverless::Api
AWS::Serverless::HttpApi
AWS::Serverless::SimpleTable
AWS::Serverless::LayerVersion
AWS::Serverless::Application
AWS::Serverless::StateMachine
AWS::Serverless::Connector


Lambda Function event sources, 16 function event source types suppported in AWS SAM:
Amazon S3
Amazon SNS
Amazon Kinesis
Amazon DynamoDB
Amazon SQS
Api
HttpApi
Schedule
Amazon Cognito
Amazon MSK
Amazon MQ
CloudWatchEvent
CloudWatchLogs
IoTRule
EventBridgeRule
Alexa Skills

Lambda:
Always look for the least privelage principle, in lambda there are 2 types of roles:
1- who can invoke it
2- what it is allowed to do


SAM CLI 
1 - App development:

- init: Initializes a new SAM project, creating the necessary files and folder structure for your serverless application.
- build: Builds the serverless application, resolving dependencies and packaging the code into deployment artifacts.
- local: Invokes your Lambda functions locally by emulating the AWS Lambda environment using Docker. || Great for testing

- logs: Fetches logs for a function, displaying them on the console. You can view logs from AWS CloudWatch Logs.
- trace: Fetches and displays the execution trace of a Lambda function.
- deploy: Deploys a SAM application. This is an alias for the 'sam build' and 'sam deploy' commands.
- sync : Update your code without redeploying || Watch for changed files

2- Stack Management:

- validate: Validates an AWS SAM template.
- package: Packages an AWS SAM application. This is an alias for 'aws cloudformation package'.
- delete: Deletes a CloudFormation stack. This is an alias for 'aws cloudformation delete-stack'.
- deploy: Deploys an AWS SAM application. This is an alias for 'aws cloudformation deploy'.
- pipeline: Deploys a SAM pipeline application. This is an alias for 'sam package', 'sam deploy', and other pipeline-related commands.
- publish: Publishes a packaged SAM application to the AWS Serverless Application Repository.
