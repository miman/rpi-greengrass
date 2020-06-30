/*
 * Demonstrates a simple MQTT receiver using Greengrass Core NodeJS SDK
 * This lambda function will receive MQTT msgs and repost the payload on the topic "hello/world"
 */

const ggSdk = require('aws-greengrass-core-sdk');

const iotClient = new ggSdk.IotData();
const os = require('os');
const util = require('util');

function publishCallback(err, data) {
    console.log(err);
    console.log(data);
}

let myName = process.env.AWS_IOT_THING_NAME;
// const myPlatform = util.format('%s-%s', os.platform(), os.release());
const msgToSend = {
    topic: 'hello/world',
    payload: '',
    queueFullPolicy: 'AllOrError',
};

function publishMqttMsg(msg, topic) {
    let payload = {
        receivedMsg: msg,
        topic: topic,
        deviceName: myName
    };
    msgToSend.payload = JSON.stringify(payload)
    iotClient.publish(msgToSend, publishCallback);
}

// This is a handler which does nothing for this example
exports.handler = function handler(event, context) {
    console.log("ggs-mqtt-listen-lambda> event received");
    console.log(event);
    // console.log(context);
    // console.log(context.clientContext.Custom);
    publishMqttMsg(event, context.clientContext.Custom.subject);
    console.log("ggs-mqtt-listen-lambda> MQTT msg posted");
};

/*
The received context
{
  invokedFunctionArn: 'arn:aws:lambda:eu-west-1:123456789:function:ggs-mqtt-listen:2',
  awsRequestId: '03048fc4-ead8-40b6-7fbf-6883bcfa11b8',
  functionName: 'ggs-mqtt-listen',
  functionVersion: '2',
  clientContext: { 
    client: {}, 
    Custom: { 
        subject: 'viot/test' 
    }, 
    env: {}
  }
}

*/