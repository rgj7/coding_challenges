"""
CodeAbbey, Problem 170
Coded by whoisrgj
"""


def binary_search(ip_address, start, end, ip_ranges):
    median = (start + end) // 2
    ip_range = ip_ranges[median]
    ip_start = int(ip_range[0], 36)
    ip_end = ip_start + int(ip_range[1], 36)
    if ip_address < ip_start:
        return binary_search(ip_address, start, median-1, ip_ranges)
    if ip_address > ip_end:
        return binary_search(ip_address, median+1, end, ip_ranges)
    if ip_start <= ip_address <= ip_end:
        return ip_range[2]
    return -1


def main():
    # load text file
    with open("db-ip.txt", "r") as f:
        ip_ranges = [tuple(line.strip().split()) for line in f.readlines()]
    # gather input data
    n = int(input())
    results = []
    for _ in range(n):
        ip_address = int(input(), 36)
        country = binary_search(ip_address, 0, len(ip_ranges)-1, ip_ranges)
        results.append(country)
    print(*results)


if __name__ == '__main__':
    main()
