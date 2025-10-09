import matplotlib.pyplot as plt
import re
from datetime import datetime, timedelta


def parse_time(time_str):
    """Convert time string (H:MM:SS.microseconds) to seconds."""
    parts = time_str.split(':')
    hours = int(parts[0])
    minutes = int(parts[1])
    seconds = float(parts[2])

    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds


def extract_size(filename):
    """Extract the numeric size from filename (e.g., 10000 from all_a_10000.txt)."""
    match = re.search(r'_(\d+)\.txt', filename)
    if match:
        return int(match.group(1))
    return None


def plot_runtime_log(log_file):
    """Read log file and create a plot of runtimes."""
    sizes = []
    runtimes = []

    with open(log_file, 'r') as f:
        # Skip header line
        next(f)

        for line in f:
            line = line.strip()
            if not line:
                continue

            # Split by whitespace
            parts = line.split()
            if len(parts) >= 2:
                filename = parts[0]
                time_str = parts[1]

                size = extract_size(filename)
                runtime_seconds = parse_time(time_str)

                if size is not None:
                    sizes.append(size)
                    runtimes.append(runtime_seconds)

    # Convert runtimes to minutes
    runtimes_minutes = [rt / 60 for rt in runtimes]

    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, runtimes_minutes, marker='o', linestyle='-', linewidth=2, markersize=8)
    plt.xlabel('Input Size', fontsize=12)
    plt.ylabel('Runtime (minutes)', fontsize=12)
    plt.title(log_file + ' Runtime vs Input Size', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    plt.show()


# Usage
if __name__ == "__main__":
    plot_runtime_log("all_a_str_logs.txt")
    plot_runtime_log("random_str_logs.txt")