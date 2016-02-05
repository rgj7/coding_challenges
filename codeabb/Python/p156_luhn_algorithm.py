"""
CodeAbbey, Problem 156
Coded by whoisrgj
"""


def calculate_card_number_sum(values):
    values = list(map(int, values))
    # sum of end, 3rd from end ...
    card_number_sum = sum(values[1:16:2])
    # sum of 2nd end, 4th end ...
    for v in values[0:16:2]:
        new_value = v*2
        card_number_sum += new_value
        if new_value > 9:
            card_number_sum -= 9
    return card_number_sum


def is_valid(values):
    return calculate_card_number_sum(values) % 10 == 0


def find_missing_value(values):
    missing_index = values.index('?')
    values[missing_index] = '0'  # replace ? with a 0
    remainder = 0
    if not is_valid(values):
        card_number_sum = calculate_card_number_sum(values)
        remainder = (10-(card_number_sum % 10))
        if missing_index % 2 == 0:
            if remainder % 2 != 0:
                remainder += 9
            remainder //= 2
    return missing_index, remainder


def swap_numbers(values):
    for i in range(15):
        values[i], values[i+1] = values[i+1], values[i]
        if is_valid(values):
            break
        values[i], values[i+1] = values[i+1], values[i]  # swap back


if __name__ == '__main__':
    N = int(input())
    results = list()
    for _ in range(N):
        card_number_values = list(input())
        try:
            index, value = find_missing_value(card_number_values)
            card_number_values[index] = str(value)
        except ValueError:
            swap_numbers(card_number_values)
        results.append("".join(card_number_values))
    print(" ".join(results))
