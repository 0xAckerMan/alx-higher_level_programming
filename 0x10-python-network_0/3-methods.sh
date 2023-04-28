#!/bin/bash
# Displays http methods
curl -sI "$1" | grep "Allow: " | sed 's/Allow: //'
