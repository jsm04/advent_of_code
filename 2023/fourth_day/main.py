import os
from typing import Generator


def read(path: str) -> Generator[str, None, None]:
    with open(path, "r") as file:
        for line in file:
            yield line.strip()


def main():
    cwd = os.getcwd()
    input_txt = os.path.join(cwd, "2023", "fourth_day", "input.txt")
    total = 0
    for line in read(input_txt):
        total += sum_card_total(line)
    print("The result is :", total)


def sum_card_total(line: str) -> int:
    lines = [s.strip() for s in line.split(":")[1].split("|")]
    winning_numbers, numbers_available = [s.split() for s in lines]
    numbers_available = set(numbers_available)
    present_numbers = [num for num in winning_numbers if num in numbers_available]
    numbers_amount = len(present_numbers)
    return 2 ** (numbers_amount - 1) if numbers_amount > 0 else 0


if __name__ == "__main__":
    main()
