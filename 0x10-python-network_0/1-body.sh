#!/bin/bash
#bash to count size of the reponse of a request send 
response=$(curl -s -w "%{http_code}" "$1"); status_code=${response: -3}; [ "$status_code" -eq 200 ] && curl -s "$1" echo " this is :$status_code" || exit
