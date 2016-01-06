import csv

names = []
with open('names.txt', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    for r in reader:
        names = r

names.sort()
scores = []

for idx, name in enumerate(names):
    score = 0
    for c in name:
        score += ord(c)-64
    score *= idx+1
    scores.append(score)

print(sum(scores))