import sys

from home_work.task_3.handler import count_logs_by_level, display_log_counts, filter_logs_by_level, load_logs


def main():
    if len(sys.argv) < 2:
        print(
            "Використання: python home_work/task_3/load_logs_main.py <шлях до файлу> [рівень логування]")
        sys.exit(1)

    log_file = sys.argv[1]
    log_level = sys.argv[2] if len(sys.argv) > 2 else None

    logs = load_logs(log_file)
    counts = count_logs_by_level(logs)

    display_log_counts(counts)

    if log_level:
        filtered_logs = filter_logs_by_level(logs, log_level.upper())
        print(f"\nДеталі логів для рівня '{log_level.upper()}':")
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} - {log['msg']}")


if __name__ == "__main__":
    main()
