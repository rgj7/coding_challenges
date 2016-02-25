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
    print(" ".join([body_constitution(w, h) for w, h in [map(float, input().split()) for _ in range(n)]]))

if __name__ == '__main__':
    main()
