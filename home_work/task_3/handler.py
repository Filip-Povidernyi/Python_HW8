from collections import defaultdict
import sys


def parse_log_line(line: str) -> dict:

    if line.startswith('20'):

        date, time, log_level, message = line.split(' ', 3)

        return {"date": date, "time": time, "log_level": log_level, "msg": message}

    return {}


def load_logs(file_path: str) -> list:
    logs = []
    try:
        with open(file_path, "+r", encoding='utf-8') as file:

            for line in file:
                log_entry = parse_log_line(line.strip())

                if log_entry:
                    logs.append(log_entry)

    except FileNotFoundError:
        print(f"Помилка: файл '{file_path}' не знайдено.")
        sys.exit(1)
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        sys.exit(1)

    return logs


def filter_logs_by_level(logs: list, level: str) -> list:

    return [item for item in logs if item['log_level'] == level]


def count_logs_by_level(logs: list) -> dict:

    counts = defaultdict(int)
    for log in logs:
        counts[log["log_level"]] += 1
    return dict(counts)


def display_log_counts(counts: dict):

    print("\nРівень логування | Кількість")
    print("-" * 25)
    for level, count in sorted(counts.items()):
        print(f"{level:<15} | {count}")
