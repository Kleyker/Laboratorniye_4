import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME) as file:  # Читаем содержимое CSV файла и создаем список словарей
        lines = [line for line in csv.DictReader(file)]

    with open(OUTPUT_FILENAME, "w") as file:  # Создаем JSON файл с отступом в 4 пробела
        json.dump(lines, file, indent=4)


if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
