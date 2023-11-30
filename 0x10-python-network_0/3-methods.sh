#!/bin/bash
#bash to display method that the server accept
curl -sI -X OPTIONS "$1" | grep "Allow" | awk '{print $2}'
