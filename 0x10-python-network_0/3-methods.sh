#!/bin/bash
#bash to display method that the server accept
curl -sI -X OPTIONS "$1" | grep -w "Allow" | awk '{sub(/Allow: /, ""); print}'
