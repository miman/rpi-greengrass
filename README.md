# rpi-greengrass
Lambda functions for Greengrass running on an AWS greengrass device accessing external hardware

This project cotains a number of test Lambdas accessing external hardware running in a greengrass device.

Each sub-project contains code for a specific Lambda

Video tutorials for these projects can be found here:
https://www.youtube.com/playlist?list=PLoZRZ2zrcw_8meOFNa1iNrBmBtWFG7EYR

Sub-modules
* [Hello World](./hello-world/README.md)
    * Contains Lambdas that only send a hardcoded string to the IoT Core backend over MQTT (no usage of external HW)
* [cntrl-gpio-pin-lambda-python](./cntrl-gpio-pin-lambda-python/README.md)
    * Python Lamda listening to a button & controlling a lamp based on button state
* [ggs-gpio-test-lambda-nodejs](./ggs-gpio-test-lambda-nodejs/README.md)
    * NodeJS Lamda listening to a button & controlling a lamp based on button state
* [ggs-mqtt-listen-lambda-nodejs](./ggs-mqtt-listen-lambda-nodejs/README.md)
    * Lambda listening to MQTT msgs from backoffice (IoT Core)
* [rfid-rc522-lambda-python](./rfid-rc522-lambda-python/README.md)
    * Lambda polling RC522 RFID reader & sending RFID tags to IoT Core over MQTT
