#!/bin/bash
# this program accepts url as argument and sends a GET request to output the result
curl "$1" -sX GET -H "X-School-User-Id: 98"
