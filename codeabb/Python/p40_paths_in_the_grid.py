"""
CodeAbbey, Problem 40
Coded by whoisrgj
"""


def main():
    rows, cols = map(int, input().split())
    grid = []
    for _ in range(rows):
        grid.append(input().split())

    value = 1
    for col in range(cols):
        if grid[0][col] == 'X':
            value = 0
        grid[0][col] = value

    value = 1
    for row in range(1, rows):
        if grid[row][0] == 'X':
            value = 0
        grid[row][0] = value

    for row in range(1, rows):
        for col in range(1, cols):
            if grid[row][col] == 'X':
                grid[row][col] = 0
            else:
                grid[row][col] = grid[row][col-1] + grid[row-1][col]
    print(grid[rows-1][cols-1])

if __name__ == '__main__':
    main()