import argparse
import os
from datetime import datetime
from utils import SuffixArray

def main():
    #run program by writing string to create suffix array over as argument
    parser = argparse.ArgumentParser(description="Create Suffix Array")
    parser.add_argument("input_file", help="Path to input file")
    parser.add_argument("logs_file", help="Write the name of the file you want the running times to be saved to")
    parser.add_argument("save_suffix_array", help="Write True to save suffix array in file. Write False to not save suffix array")
    args = parser.parse_args()
    with open(args.input_file) as f:
        string = f.read().strip()
            
    
    start_time = datetime.now()

    #creating the suffix array from the string passed as first argument
    tree = SuffixArray(string)
    suffix_array = tree.suffix_array()
    if args.save_suffix_array.lower() == "true":
        output_file = args.input_file + ".suffix_array.txt"
        with open(output_file, "w") as f:
            f.write("\t".join(map(str, suffix_array)) + "\n")
    elif args.save_suffix_array.lower() == "false":
        print("Not saving suffix array")

    end_time = datetime.now()
    time = end_time - start_time

    with open(args.logs_file, "a") as f:
        f.write(f"{args.input_file}\t{time}\n")

if __name__ == "__main__":
    main()

    

