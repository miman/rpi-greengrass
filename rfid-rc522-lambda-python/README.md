# rfid-rc522-lambda-python
Lambda functions for Greengrass running on an AWS greengrass device accessing external hardware

This project contains a Lambda polling RC522 RFID reader & sending RFID tags to IoT Core over MQTT

## Prerequisites

### Greengrass SDK
Observer that you MUST copy the greengrasssdk folder from the [Python SDK](https://github.com/aws/aws-greengrass-core-sdk-python/) to this folder before you can create a deployment package !

### Resources
You MUST also create 2 Resources:
* A device resource for ***/dev/gpiomem***
* A device resource for SPIO (one of these depending on which SPIO PINS you are using):
    * ***/dev/spidev0.0***
    * ***/dev/spidev0.1***

For both resources:
* you should select **Group owner file access permission**:
    * ***Automatically add OS group permissions of the Linux group that owns the resource***
* You need to add this lambda as **Lambda function affiliations**

### Subscriptions
You MUST add a subscription for ***rfid/read*** with this Lambda as **Source** & IoT Cloud as **Target**

## Usage
Run the **zip-ggs-module.bat** to create a zip file that can be uploaded to the Lambda function

OBS.
When the Lambda has been uploaded you MUST do the following 2 steps before you can deploy theLambda to a Greengrass device
1. Create a version
2. Create an Alias

The alias should then be choosen when creating/updating the Lambda in the Greegrass group before deploying it.

Remember that the Resources & Subscriptions MUST be updated with the new version for the Lambda to work !!

PIN Connection

RC522   --  R-PI
=================
3.3     --  3.3

RST     --  PIN 22 / GPIO23

GND     --  GND

MISO    --  PIN 21 (MISO) / SPMISO / GPIO09

MOSI    --  PIN 19 (MOSI) / SPMOSI / GPIO10

SCK     --  PIN 23 (SCK) / SPISCLK/ GPIO11                        SCK = Selektor

SDA     --  PIN 24 (SDA) / SPICEO / GPIO08


[Back to Main page](../README.md)