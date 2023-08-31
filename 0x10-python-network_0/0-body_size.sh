#!/usr/bin/env bash
# A Bash script that takes in a URL
# Sends a request to that URL
# Displays the size of the body of the response

curl  -s "$1" | wc -c
