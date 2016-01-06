class Problem135:
    def __init__(self):
        self.encoding_map = {
            ' ': "11",
            'a': "011",
            'b': "0000010",
            'c': "000101",
            'd': "00101",
            'e': "101",
            'f': "000100",
            'g': "0000100",
            'h': "0011",
            'i': "01001",
            'j': "000000001",
            'k': "0000000001",
            'l': "001001",
            'm': "000011",
            'n': "10000",
            'o': "10001",
            'p': "0000101",
            'q': "000000000001",
            'r': "01000",
            's': "0101",
            't': "1001",
            'u': "00011",
            'v': "00000001",
            'w': "0000011",
            'x': "00000000001",
            'y': "0000001",
            'z': "000000000000",
            '!': "001000"
        }

    def solve(self):
        string_list = list(input())
        binary_string = ""
        for x in range(len(string_list)):
            binary_string += self.encoding_map[string_list[x]]

        if len(binary_string) % 8 > 0:
            binary_string += "0" * (8 - (len(binary_string) % 8))

        for x in range(0, len(binary_string), 8):
            print('%02X' % int(binary_string[x:x + 8], 2), end=" ")


if __name__ == "__main__":
    Problem135().solve()
