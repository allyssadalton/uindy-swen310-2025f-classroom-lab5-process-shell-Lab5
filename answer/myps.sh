#!/bin/bash
# Check if user gave number
if [ $# -ne 1 ]; then
    echo "Usage: $0 <PID>"
    exit 1
fi

PID=$1

# Use ps to look up the process
output=$(ps -o f,s,uid,pid,ppid,c,cmd -p "$PID" --no-headers)

if [ -z "$output" ]; then
    echo "no process found for $PID"
else
    # Print header (to match the style in ps output)
    echo "  F S   UID   PID  PPID  C CMD"
    echo "$output"
fi
exit


