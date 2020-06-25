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
from threading import Timer
import os
import RPi.GPIO as GPIO
from time import sleep
from mfrc522 import SimpleMFRC522

import greengrasssdk

# Setup logging to stdout
logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

# Creating a greengrass core sdk client
client = greengrasssdk.client("iot-data")

# Initiate RFID reader
reader = SimpleMFRC522()

device = os.environ['AWS_IOT_THING_NAME']

# This is a dummy handler and will not be invoked
# Instead the code above will be executed in an infinite loop for our example
def lambda_handler(event, context):
    return

def post_read_rfid_tag(id_no, text):
    text_to_send="RFID tag read '" + str(id_no) + "' with content '" + text.strip() + "' on Greengrass device: " + device
    print(text_to_send)
    try:
        client.publish(
            topic="rfid/read",
            queueFullPolicy="AllOrException",
            payload=text_to_send
        )
    except Exception as e:
        logger.error("Failed to publish message: " + repr(e))

def start_read_cycle():
    print("Starting RFID RC522 reader")
    try:
        while True:
            id_no, text = reader.read()
            post_read_rfid_tag(id_no, text)
            sleep(0.2) # Sleep for 0.2 second

    except Exception as e:
        print("RFID reader error: " + str(e))
    finally:
        print("Closing RFID reader")

# Start executing the function above
start_read_cycle()
