#
# Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#

# greengrassHelloWorld.py
# Demonstrates a simple publish to a topic using Greengrass core sdk
# This lambda function will retrieve underlying platform information and send
# a hello world message along with the platform information to the topic
# 'hello/world'. The function will sleep for five seconds, then repeat.
# Since the function is long-lived it will run forever when deployed to a
# Greengrass core.  The handler will NOT be invoked in our example since
# the we are executing an infinite loop.

import logging
import platform
import sys
import os
import json
import greengrasssdk

# Setup logging to stdout
logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

# Creating a greengrass core sdk client
client = greengrasssdk.client("iot-data")

device = os.environ['AWS_IOT_THING_NAME']

def post_echo(msg, topic):
    text_to_send = {
        "receivedMsg": msg,
        "topic": topic,
        "deviceName": device
    }
    try:
        client.publish(
            topic="echo/output",
            queueFullPolicy="AllOrException",
            payload=json.dumps(text_to_send)
        )
    except Exception as e:
        logger.error("Failed to publish message: " + repr(e))

# This is a Lambda handler that will be called whenever a msg is posted on a topic routed to this Lambda
def lambda_handler(event, context):
    print("power-controller> Msg received")
    # Get the name of the topic this message was received on
    topic = context.client_context.custom["subject"]
    post_echo(event, topic)

