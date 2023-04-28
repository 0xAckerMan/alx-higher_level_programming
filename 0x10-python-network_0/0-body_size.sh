#!/bin/bash
#Script takes url and displays length of response
curl -sI "$1" | grep "Content-Length" | cut -d ' ' -f 2
