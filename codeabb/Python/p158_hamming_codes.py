"""
CodeAbbey, Problem 158
Coded by whoisrgj
"""
from operator import xor
from functools import reduce


def decode(string):
    binary_string = list(map(int, string))
    parity_bit_count, index = 0, 0
    parity_bit_indexes = []
    while index < len(binary_string):
        parity_bit_count += 1
        parity_bit_indexes.append(index)
        index = (2 ** parity_bit_count) - 1
    checksum = []
    for x in ((2 ** i) for i in range(parity_bit_count)):
        bits = []
        for index in range(x - 1, len(binary_string), x * 2):
            bits.extend(binary_string[index:index + x])
        parity_bit = reduce(xor, bits)
        checksum.append(parity_bit)
    error = int("".join(map(str, reversed(checksum))), 2)
    if error:
        binary_string[error-1] ^= 1
    binary_string = [binary_string[i] for i in range(len(binary_string))
                     if i not in parity_bit_indexes]
    return "".join(map(str, binary_string))


def encode(string):
    binary_string = list(map(int, string))
    parity_bit_count, index = 0, 0
    while index < len(binary_string):
        parity_bit_count += 1
        binary_string.insert(index, 0)
        index = (2 ** parity_bit_count) - 1
    for x in ((2**i) for i in range(parity_bit_count)):
        bits = []
        for index in range(x-1, len(binary_string), x*2):
            bits.extend(binary_string[index:index+x])
        parity_bit = reduce(xor, bits)
        binary_string[x-1] = parity_bit
    return "".join(map(str, binary_string))


def main():
    n1 = int(input())
    results = []
    for _ in range(n1):
        encoded_bin_str = encode(input())
        results.append(encoded_bin_str)
    n2 = int(input())
    for _ in range(n2):
        decoded_bin_str = decode(input())
        results.append(decoded_bin_str)
    print(*results)

if __name__ == '__main__':
    main()
