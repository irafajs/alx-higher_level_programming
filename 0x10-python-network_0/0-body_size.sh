#!/bin/bash
#bash to count size of the reponse of a request send 
echo "$(curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}')"
