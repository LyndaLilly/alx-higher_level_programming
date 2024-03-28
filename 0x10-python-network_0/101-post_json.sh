#!/bin/bash
# this code transfers GET request to particular URL and outputs it.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
