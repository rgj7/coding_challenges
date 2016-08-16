"""
CodeAbbey, Problem 206
Coded by whoisrgj
"""

decode_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"
decode_dict = {k: v for v, k in enumerate(decode_str)}


def encode(string):
    remainder = len(string) % 5
    pad_count = 5 - remainder
    string += str(pad_count) * pad_count
    binary_string = "".join(["{0:0>8b}".format(ord(c)) for c in string])
    tokens = [binary_string[i:i+5] for i in range(0, len(binary_string), 5)]
    return "".join([decode_str[int(x, 2)] for x in tokens])


def decode(string):
    tokens = "".join(["{0:0>5b}".format(decode_dict[c]) for c in string])
    binary_string = [tokens[i:i+8] for i in range(0, len(tokens), 8)]
    decoded_string = [chr(int(x, 2)) for x in binary_string]
    for _ in range(int(decoded_string[-1])):
        decoded_string.pop()
    return "".join(decoded_string)


def main():
    n = int(input())
    results = []
    for x in range(n):
        results.append(decode(input()) if x % 2 else encode(input()))
    print(*results)

if __name__ == '__main__':
    main()
