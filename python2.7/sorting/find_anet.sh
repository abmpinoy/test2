#!/bin/bash

# 03-Mar-2015 14:17:02.585 client 69.252.66.221#46581: query: orldfl-ns-1.atlantic.net IN A -

cat queries.log | awk '{print $6}' | sort | uniq -c | sort -n | grep atlantic.net
