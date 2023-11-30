#!/bin/bash
#bash to send a POST request URL and shwo the response
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
