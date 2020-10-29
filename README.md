# takorun-sls

This project contains Serverless AWS Setup for Takorun. Please go through documentation
for information

## Prerequisites

Following are Requirements/Tool needed to develop/test/run the setup.

- AWS CLI [(Installation)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html)
- AWS SAM CLI [(Installation)](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
- Python3.8 [(Installation)](https://www.python.org/downloads/release/python-386/)
- PyCharm or Any desired IDE for development and debugging.

## Setup

Create virtual environment from python3.8

Install requirements by following command
`pip install -r requirements.txt`

Run `aws configure --profile takorun`

Enter the details required to configure the aws credentials profile.


## Deployment
There are three stages of deployment
1. dev
2. stage
3. prod

Each of the stage deployment will create <Deployment stage>-takorun
stack in Cloudformation

Run `sam build` in the shell to Build the code

Run `sam deploy` command to deploy the stack to AWS (By default deployment stage would be **dev**)
However you could use `sam deploy --config-env <stage name>` to deploy stack for specific stage
i.e 

`sam deploy --config-env production` (For production) <br/>
`sam deploy --config-env stage` (For Stage)

## Testing and Debugging

#### Invoke functions locally
For invoking lambda functions locally (Testing purpose) Look into 
[AWS Official Guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-using-invoke.html) for that.

You can also [run APIGateway locally](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-using-start-api.html)

#### Run unit tests

`pytest` is required to run tests. However it is included in the requirements.

To run unit test you may execute `pytest` from your shell (Make sure that virtual environment is activated)