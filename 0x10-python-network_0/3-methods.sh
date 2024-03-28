#!/bin/bash
# this outputs HTTP methods to server that a particular url will take.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
