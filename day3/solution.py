import re


def mul(a, b):
    return a * b


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        memory = file.read()

    pattern = r'mul\((\d{1,3}\,\d{1,3})\)'
    matches = re.findall(pattern, memory)

    sum_of_products = 0

    for match in matches:
        sum_of_products += int(match.split(',')[0]) * int(match.split(',')[1])

    print(f"Solution: {sum_of_products}")
