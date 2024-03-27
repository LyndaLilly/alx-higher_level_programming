#!/bin/bash
# this gets hhtps request from url request.
curl -s "$1" | wc -c
