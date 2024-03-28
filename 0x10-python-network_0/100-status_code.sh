#!/bin/bash
# this code transfers GET request to particular URL and outputs it
curl -s -o /dev/null -w "%{http_code}" "$1"
