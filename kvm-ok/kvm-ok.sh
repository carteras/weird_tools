#!/bin/bash

# Count the number of times 'vmx' or 'svm' is mentioned in /proc/cpuinfo
count=$(grep -E "vmx|svm" /proc/cpuinfo | wc -l)

if [ "$count" -gt 0 ]; then
    exit 0
else
    exit 1
fi
