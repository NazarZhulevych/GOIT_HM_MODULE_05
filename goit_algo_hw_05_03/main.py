import sys
from collections import Counter

def load_logs(file_path: str) -> list:
    """Loads logs from a file, filters invalid lines, and parses them into a list of dictionaries."""
    try:
        with open(file_path, "r", encoding="utf-8") as fh:
            lines = fh.readlines()
            # Filter only valid lines before parsing
            valid_lines = list(filter(lambda line: len(line.strip().split(maxsplit=3)) == 4, lines))
            return parse_log_lines(valid_lines)
    except FileNotFoundError:
        print(f"Помилка: Файл {file_path} не знайдено.")
        return []
    except Exception as e:
        print(f"Помилка читання файлу: {e}")
        return []

def parse_log_lines(lines: list[str]) -> list:
    """Parses valid log lines into a list of dictionaries."""
    return [
        {
            "date": line_parts[0],
            "time": line_parts[1],
            "level": line_parts[2],
            "description": line_parts[3]
        }
        for line in lines
        if len(line_parts := line.strip().split(maxsplit=3)) == 4
    ]

def filter_logs_by_level(logs: list, level: str) -> list:
    """Filters parsed logs by level and returns a list of log entries (dicts)."""
    return [log for log in logs if log.get("level") == level]

def count_logs_by_level(logs: list) -> dict:
    """Counts the number of logs by level."""
    return dict(Counter(log["level"] for log in logs))

def display_log_counts(counts: dict):
    """Prints a formatted table of log counts by level, computed from logs."""
    counts = count_logs_by_level(counts)
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level.ljust(15)}| {count}")


# Main execution

if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Використання:")
        print("  python main.py logfile.log             # Для статистики")
        print("  python main.py logfile.log ERROR       # Для фільтрації за рівнем")
        sys.exit(1)

    log_file_path = sys.argv[1]
    logs = load_logs(log_file_path)

    if not logs:
        print("Немає дійсних логів для обробки.")
        sys.exit(0)

    if len(sys.argv) == 2:
        # Only logfile path: show statistics
        display_log_counts(logs)
    else:
        # logfile path + log level
        level = sys.argv[2].upper()
        filtered_logs = filter_logs_by_level(logs, level)
        display_log_counts(logs)
        if filtered_logs:
            print(f"\nДеталі логів для рівня '{level}':")
            print("-------------------------------")
            for log in filtered_logs:
                print(f"{log['date']} {log['time']} {log['level']} {log['description']}")
        else:
            print(f"Немає логів з рівнем {level}.")

