#!/bin/bash
set -e

LOGFILE="random_str_logs.txt"

echo -e "string\truntime" > "$LOGFILE"

for file in $(ls random_str/*.txt | sort -V); do
    echo "Running on $LOGFILE ..."

    python3 main.py "$file" "$LOGFILE" "False"
done

echo "All runs complete. Results saved in $LOGFILE"