#!/bin/bash
# Curls and return json
curl -sX POST -H "Content-type: application/json" -H "Accept: application/json" -d "@$2" "$1"
