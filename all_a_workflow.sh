#!/bin/bash
set -e

LOGFILE="all_a_str_logs.txt"
echo -e "string\truntime" > "$LOGFILE"

export LOGFILE  # make sure child processes see this variable

ls all_a_str/*.txt | sort -V | xargs -n 1 -P 10 -I {} bash -c '
    echo "Running on {} ..."
    python3 main.py "{}" "$LOGFILE" "False"
'

echo "All runs complete. Results saved in $LOGFILE"
