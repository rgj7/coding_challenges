"""
CodeAbbey, Problem 28
Coded by Raul Gonzalez
"""


def body_constitution(weight, height):
    bmi = weight / (height**2)
    if bmi < 25:
        return "under" if bmi < 18.5 else "normal"
    else:
        return "over" if bmi < 30 else "obese"


def main():
    n = int(input())
    results = []
    for _ in range(n):
        weight, height = map(float, input().split())
        results.append(body_constitution(weight, height))
    print(" ".join(results))

if __name__ == '__main__':
    main()
