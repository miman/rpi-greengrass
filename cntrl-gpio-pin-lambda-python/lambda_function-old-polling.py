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
from gpiozero import LED, Button
from time import sleep
from signal import pause

import greengrasssdk

# Setup logging to stdout
logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

# Creating a greengrass core sdk client
client = greengrasssdk.client("iot-data")

# Retrieving platform information to send from Greengrass Core
my_platform = platform.platform()

device = os.environ['AWS_IOT_THING_NAME']

red_led = LED(23)

# When deployed to a Greengrass core, this code will be executed immediately
# as a long-lived lambda function.  The code will enter the infinite while
# loop below.
# If you execute a 'test' on the Lambda Console, this test will fail by
# hitting the execution timeout of three seconds.  This is expected as
# this function never returns a result.
def post_hello_world():
    text_to_send="Button pressed on Greengrass device: " + device
    try:
        client.publish(
            topic="hello/world",
            queueFullPolicy="AllOrException",
            payload=text_to_send
        )
    except Exception as e:
        logger.error("Failed to publish message: " + repr(e))

def start_btn_trigger():
    button = Button(24)
    is_pressed=False
    last_state=False
    while True:
        last_state = is_pressed
        is_pressed = button.is_pressed
        if last_state != is_pressed:
            if is_pressed:
                post_hello_world()
                red_led.on()
            else:
                red_led.off()
        sleep(0.2)

# Start executing the function above
start_btn_trigger()

# This is a dummy handler and will not be invoked
# Instead the code above will be executed in an infinite loop for our example
def lambda_handler(event, context):
    return
