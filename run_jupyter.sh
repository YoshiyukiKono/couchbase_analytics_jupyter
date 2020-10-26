#! /bin/bash

export CB_HOST_URL=$1
export CB_USER=$2
export CB_PASSWORD=$3

echo $CB_HOST_URL
echo $CB_USER
echo $CB_PASSWORD

nohup jupyter notebook --ip=* --no-browser &
