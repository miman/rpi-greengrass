/*
 * Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
 */

/*
 * Demonstrates a simple publish to a topic using Greengrass Core NodeJS SDK
 * This lambda function will retrieve underlying platform information and send
 * a hello world message along with the platform information to the topic
 * 'hello/world'. The function will sleep for five seconds, then repeat.
 * Since the function is long-lived it will run forever when deployed to a
 * Greengrass core.
 */

const ggSdk = require('greengrass-core-sdk');
var gpio = require('rpi-gpio');

const iotClient = new ggSdk.IotData();
const os = require('os');
const util = require('util');

gpio.setup(23, gpio.DIR_HIGH, write);
let isOn = false;

function greengrassHelloWorldRun() {
    isOn = !isOn;
    gpio.write(7, isOn, function(err) {
        if (err) throw err;
        console.log('Written " + isOn + " to pin');
    });
}

// Schedule the job to run every 5 seconds
setInterval(greengrassHelloWorldRun, 5000);

// This is a handler which does nothing for this example
exports.handler = function handler(event, context) {
    console.log(event);
    console.log(context);
};
