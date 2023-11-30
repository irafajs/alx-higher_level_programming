#!/bin/bash
#bash to diplay the status code of the response
echo "$(curl -s -o /dev/null -w "%{http_code}" "${1}")"

