#!/bin/bash

uptime

# product=`sudo lshw | grep Raspberry`
product=`cat /proc/cpuinfo | grep "Model"`
echo -e ${product:9}

os=`grep PRETTY_NAME /etc/os-release`
echo -e ${os:12}

free -h
