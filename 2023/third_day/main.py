import os


def main():
    cwd = os.getcwd()
    with open(os.path.join(cwd, "2023", "third_day", "example.txt"), "r") as file:
        result = solve(file.readlines())
        print("Function return value: ", result)
        print("Is okay: ", result == 4361)


def solve(lines: list[str]):
    total_sum: int = 0
    for line_index, line in enumerate(lines):
        line = line.strip()
        last_line = len(lines) - 1
        if line_index in (0, last_line):
            continue
        for char_index, char in enumerate(line):
            if char == ".":
                continue
            if char != "." and not char.isdigit():
                prev_line, next_line = lines[line_index - 1], lines[line_index + 1]
                total_sum += find_adyacents(prev_line, char_index)
                total_sum += find_adyacents(next_line, char_index)
    return total_sum


def find_adyacents(line: str, idx: int):
    total_sum = 0
    curr_char = line[idx]
    # if current index is a dot check both sides
    if not curr_char.isdigit():
        # Manage numbers previous to the dot
        prev_idx = idx - 1
        prev_char = line[prev_idx]
        padding = 0
        if prev_char.isdigit():
            n: int = 0
            while prev_char.isdigit():
                n += int(prev_char + ("0" * padding))
                tmp = line[prev_idx - 1]
                if not tmp.isdigit():
                    break
                padding += 1
                prev_idx -= 1
                prev_char = tmp
            total_sum += n
        # Manage numbers after to the dot
        next_idx = idx + 1
        next_char = line[next_idx]
        if next_char.isdigit():
            n: str = ""
            while next_char.isdigit():
                n = n + next_char
                tmp = line[next_idx + 1]
                if not tmp.isdigit():
                    break
                next_idx += 1
                next_char = tmp
            total_sum += int(n)
    else:
        # curr_char as mid
        num: list[int] = [curr_char]
        left, right = idx - 1, idx + 1
        # check and insert before mid
        prev_number = line[left]
        if prev_number.isdigit():
            while prev_number.isdigit():
                num.insert(0, prev_number)
                tmp = line[left - 1]
                if not tmp.isdigit():
                    break
                left -= 1
                prev_number = tmp

        # check and append after mid
        next_number = line[right]
        if next_number.isdigit():
            while next_number.isdigit():
                num.append(next_number)
                tmp = line[right + 1]
                if not tmp.isdigit():
                    break
                right += 1
                next_number = tmp
        total_sum += int("".join(num))

    return total_sum


if __name__ == "__main__":
    main()
