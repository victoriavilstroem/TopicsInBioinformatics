#!/bin/bash
set -e

LOGFILE="all_a_str_logs.txt" #specifying the log file to save running times to

echo -e "string\truntime" > "$LOGFILE" #clearing the logfile for new run

for file in $(ls all_a_str/*.txt | sort -V); do #loop over files in the all_a_str folder
    echo "Runing on $file ..." #writing to std out which file it's currently running on

    python3 main.py "$file" "$LOGFILE" "False" #running the script on the input file
done

echo "All runs complete. Results saved in $LOGFILE"