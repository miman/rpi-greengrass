# example-lambda-python
Lambda functions for Greengrass running on an AWS greengrass device accessing external hardware

This project contains a Lambda posting a text msg to the Topic ***hello/world*** to **IoT Cloud** once every 5 seconds.

## Prerequisites

### Greengrass SDK
Observer that you MUST copy the greengrasssdk folder from the [Python SDK](https://github.com/aws/aws-greengrass-core-sdk-python/) to this folder before you can create a deployment package !

### Resources
No resources needs to be created for this project

### Subscriptions
You MUST add a subscription for ***hello/world*** with this Lambda as **Source** & IoT Cloud as **Target**

## Usage
Run the **zip-ggs-module.bat** to create a zip file that can be uploaded to the Lambda function

OBS.
When the Lambda has been uploaded you MUST do the following 2 steps before you can deploy theLambda to a Greengrass device
1. Create a version
2. Create an Alias

The alias should then be choosen when creating/updating the Lambda in the Greegrass group before deploying it.

Remember that the Subscriptions MUST be updated with the new version for the Lambda to work !!

[Back to Main page](../README.md)