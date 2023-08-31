#!/usr/bin/env bash
# A Bash script that sends a DELETE request
# to the URL passed as the first argument
# Displays the body of the response

curl -sXL "$1"
