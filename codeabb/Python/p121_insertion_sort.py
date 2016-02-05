"""
CodeAbbey, Problem 121
Coded by whoisrgj
"""


def find_insert_index(values, insert_value):
    for idx in range(len(values)):
        if insert_value < values[idx]:
            return idx
    return len(values)


def shift_array(values, start, end):
    shift_count = 0
    for j in range(end, start, -1):
        array_values[j] = array_values[j-1]
        shift_count += 1
    return shift_count


if __name__ == '__main__':
    N = int(input())
    array_values = list(map(int, input().split()))
    results = list()
    for i in range(1, N):
        # save first element in unordered list
        saved_value = array_values[i]
        # find index to insert in unordered list
        insert_index = find_insert_index(array_values[:i], saved_value)
        # shift from index
        shifts = shift_array(array_values, insert_index, i)
        # replace saved value
        array_values[insert_index] = saved_value
        results.append(str(shifts))
    print(" ".join(results))

