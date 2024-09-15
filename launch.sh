#!/bin/bash
# Check if the domain name is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <config_file>"
    exit 1
fi

CONFIG=$1


./venv/bin/python ./src/main.py $CONFIG