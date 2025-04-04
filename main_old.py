import os
import argparse

def parse_log_line(lines: list) -> list:
    """Parses log lines into a list of dictionaries."""
    file_content = []
    
    for line in lines:
        parts = line.strip().split(maxsplit=3)  # Use maxsplit to avoid truncation
        
        if len(parts) == 4:
            date, time, error_level, error_description = parts
            line_content = {  # Create a new dictionary in each loop iteration
                "date": date,
                "time": time,
                "level": error_level,
                "description": error_description.strip()
            }
            file_content.append(line_content)
    
    return file_content

def load_logs(file_path: str) -> list:
    """Loads logs from a file."""
    with open(file_path, "r", encoding="utf-8") as fh:
        content = fh.readlines()
    return content

def count_logs_by_level(logs: list) -> dict:
    """Counts log occurrences by level."""
    level_count = {"INFO": 0, "ERROR": 0, "DEBUG": 0, "WARNING": 0}

    for log in logs:
        log_level = log["level"]
        if log_level in level_count:
            level_count[log_level] += 1

    return level_count  # Now correctly returns a count dictionary

def print_log_count_table(counts):
    """Prints log level counts in table format."""
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level.ljust(15)}| {count}")

def filter_logs_by_level(logs: list) -> dict:
    """Filters logs by level and returns a count dictionary."""
    info_list = []
    error_list = []
    debug_list = []
    warning_list = []

    for log in logs:
        if log.get("level") == "INFO":
            info_list.append(log)
        elif log.get("level") == "ERROR":  
            error_list.append(log)
        elif log.get("level") == "DEBUG":
            debug_list.append(log)
        elif log.get("level") == "WARNING":
            warning_list.append(log)

    # Count logs by level
    return {
        "INFO": count_logs_by_level(info_list),
        "ERROR": count_logs_by_level(error_list),
        "DEBUG": count_logs_by_level(debug_list),
        "WARNING": count_logs_by_level(warning_list),
    }

# Load and process logs
logs = parse_log_line(load_logs("logfile.log"))
log_counts = count_logs_by_level(logs)

# Print the log count table
print_log_count_table(log_counts)



"""
def main():
    # Initialize argparse to parse command-line arguments
    parser = argparse.ArgumentParser(description="Load logs from a file.")
    
    # Define the argument for the log file path
    parser.add_argument('file_path', type=str, help="Path to the log file")
    
    # Parse the arguments passed to the script
    args = parser.parse_args()
    
    # Call load_logs with the provided file path
    logs = load_logs(args.file_path)
    
    # Print the logs to the terminal (or handle them however you like)
    

if __name__ == "__main__":
    main()
"""
