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

isOn=False
lastState=False

BUTTONPIN=24
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setup(BUTTONPIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

LEDPIN=23
GPIO.setup(LEDPIN, GPIO.OUT, initial=GPIO.LOW)

def btn_pressed():
    global isOn
    global lastState
    lastState=isOn
    isOn=True
    if lastState != isOn:
      print("Button was pressed")
      GPIO.output(LEDPIN, GPIO.HIGH) # Turn on
      post_hello_world()

def btn_released():
    global isOn
    global lastState
    lastState=isOn
    isOn=False
    if lastState != isOn:
      print("Button was released")  
      GPIO.output(LEDPIN, GPIO.LOW) # Turn off


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

def start_app():
    print("Python GPIO Test Lambda started")
    try:
        while True:
            input_state = GPIO.input(BUTTONPIN)
            if input_state == False:
                btn_pressed()
            else:
                btn_released()
            sleep(0.2) # Sleep for 0.2 second

    except Exception as e:
        print("Button error: " + str(e))
    finally:
        print("Closing Button")


# Start executing the function above
start_app()

# This is a dummy handler and will not be invoked
# Instead the code above will be executed in an infinite loop for our example
def lambda_handler(event, context):
    return
