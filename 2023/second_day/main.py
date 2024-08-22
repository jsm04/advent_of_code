import os
from solution import Solve


def main():
    cwd = os.getcwd()
    with open(os.path.join(cwd, "2023", "second_day", "input.txt"), "r") as file:
        lines = file.readlines()
        sum_values = 0
        valid_ids = []
        for line in lines:
            solver = Solve(line)
            res = solver.process()
            if res != -1:
                valid_ids.append(res)
        sum_values += sum(valid_ids)
        print(f"Sum of IDs of valid games: {sum_values}")


if __name__ == "__main__":
    main()
