import os


def main():
    cwd = os.getcwd()

    with open(os.path.join(cwd, "2023", "first_day", "input.txt"), "r") as file:
        total_sum = 0
        lines = file.readlines()
        for line in lines:
            nums = []
            first_digit_found = False
            last_digit = None
            for char in line:
                if char.isdigit():
                    if not first_digit_found:
                        nums.append(char)
                        first_digit_found = True
                    last_digit = char
            if first_digit_found and last_digit is not None:
                if len(nums) == 1 or nums[-1] != last_digit:
                    nums.append(last_digit)
                total_sum += int("".join(nums))
    print(f"Sum of calibration values: {total_sum}")


if __name__ == "__main__":
    main()
