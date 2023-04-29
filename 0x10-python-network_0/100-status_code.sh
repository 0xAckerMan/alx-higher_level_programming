#!/bin/bash
# returns the status code of the site url
curl -o /dev/null -sw "%{http_code}" "$1"
