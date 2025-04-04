import os
from collections import Counter

def parse_log_line(lines):
    """Parses log lines into a list of dictionaries."""
    return list(map(lambda line: dict(zip(["date", "time", "level", "description"], line.strip().split(maxsplit=3))), 
                    filter(lambda line: len(line.strip().split(maxsplit=3)) == 4, lines)))

def load_logs(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as fh:
            return fh.readlines()
    except FileNotFoundError:
        print(f"Помилка: Файл {file_path} не знайдено.")
        return []
    except Exception as e:
        print(f"Помилка читання файлу: {e}")
        return []

def count_logs_by_level(logs):

    return dict(Counter(map(lambda log: log["level"], logs)))

def print_log_count_table(counts):
    
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    list(map(lambda kv: print(f"{kv[0].ljust(15)}| {kv[1]}"), counts.items()))

# Завантаження і обробка логів
logs = parse_log_line(load_logs("logfile.log"))
if logs:
    log_counts = count_logs_by_level(logs)
    print_log_count_table(log_counts)
