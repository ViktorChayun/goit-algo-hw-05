"""
    https://www.edu.goit.global/uk/learn/26850204/19951493/19951593/homework
    
    Розробіть Python-скрипт для аналізу файлів логів
        * читати лог-файл переданий як аргумент командного рядка
        * виводити статистику за рівнями логування наприклад, INFO, ERROR, DEBUG. 
        * користувач може вказати рівень логування як другий аргумент командного рядка, щоб отримати всі записи цього рівня.
        * рівні логування: INFO, ERROR, DEBUG, WARNING
    
    Спосіб запуску
        python main.py '/path/logfile.log'
        python main.py 'path/tlogfile.log' error
"""
import sys
from pathlib import Path
from datetime import datetime
from collections import Counter

# перевірка на існування файлу - повертає обєкт Path
def checkFile(path:str) -> Path:
    f_path = Path(path)
    if not f_path.exists():
            print("ERROR: File is not existing")
            sys.exit(1)
    return f_path

# Парсинг рядка логу
def parse_log_line(line: str) -> dict:
    try:
        str_date, str_time, str_level, *str_msg = line.split(' ')
        
        dt = datetime.strptime(str_date, "%Y-%m-%d").date()
        tm = datetime.strptime(str_time, "%H:%M:%S").time()
        msg = ' '.join(str_msg)
        msg = msg.rstrip("\n")
    except:
        print(f'Incorrect format of log-file: {line}')
        dt = None
        tm = None
        str_level = ""
        msg = ""
    
    return {"date": dt, "time": tm, "level": str_level.lower(), "message": msg}

# Завантаження лог-файлів
def load_logs(file_path: str) -> list:
    try:
        with open(file_path, "r", encoding="utf-8") as fh:
            lines = fh.readlines()
    except:
        print("ERROR: Failure during file reading.")
        sys.exit(2)
    
    # Парсинг рядка логу
    return list(map(parse_log_line, lines))

# Фільтрацію за рівнем логування
def filter_logs_by_level(logs: list, level: str) -> list:
    return list( filter(lambda val: val["level"] == level.lower(), logs) )

# Підрахунок записів за рівнем логування
def count_logs_by_level(logs: list) -> dict:
    # Витягнути всі рівні "level" у список
    levels = [entry["level"] for entry in logs]
    # рухуємо каунтером к-ть різних рівнів, результат буде довідник
    return Counter(levels)

# Вивід результатів
def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    if "info" in counts:
        print(f"INFO             | {counts['info']}")
    if "debug" in counts:
        print(f"DEBUG            | {counts['debug']}")
    if "error" in counts:
        print(f"ERROR            | {counts['error']}")
    if "warning" in counts:
        print(f"WARNING          | {counts['warning']}")

# відфільтровуємо і виводимо додаткову інфу по левелу логування
def display_log_details(parsed_lines:list, param:str):
    filtered_lines = filter_logs_by_level(parsed_lines, param)
    if len(filtered_lines):
        print(f"\nДеталі логів для рівня '{param.upper()}':")
        for line in filtered_lines:
            str_date = line['date'].strftime('%Y-%m-%d')
            str_time = line['time'].strftime('%H:%M:%S')
            print(f"{str_date} {str_time} - {line['message']}")
    else:
        print(f"Відсутні записи для рівня логування '{param.upper()}'")
    
def processing(path:str, param:str = ""):
    f_path = checkFile(path)
    # Завантаження лог-файлу
    parsed_lines = load_logs(f_path.absolute())    
    
    # Підрахунок записів за рівнем логування
    res = count_logs_by_level(parsed_lines)
    
    # Вивід результатів
    display_log_counts(res)
    
    # вивід деталей логу відфільтрованих по параметру рівня
    if param:
        display_log_details(parsed_lines, param)

# Завантаження лог-файлів
def main():
    if len(sys.argv) ==1:
        print("Please indicate path to log file.")
    elif len(sys.argv) ==2:
        # виклик з 1 параметром - шляхом до файлу
        processing(sys.argv[1])
    elif len(sys.argv) ==3:
        # виклик з 2 параметрами - шлях до файлу + фільтрування
        processing(sys.argv[1], sys.argv[2])
    else:
        print("Incorrect parameters.")

# start
if __name__ == "__main__":
    main()