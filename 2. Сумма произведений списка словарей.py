import json

INPUT_FILENAME = "input.json"


def task() -> float:
    with open(INPUT_FILENAME) as file:
        json_data = json.load(file)

    sum_values = sum([item["score"] * item["weight"] for item in json_data])
    return round(sum_values, 3)


print(task())
