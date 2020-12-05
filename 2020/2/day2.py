from collections import Counter

with open("day2.txt") as f:
    puzzle_input = f.read()

database = [x.split() for x in puzzle_input.split("\n")]


c = 0
for row in database:
    at_least, at_most = [int(x) for x in row[0].split("-")]
    char = row[1][0]
    password = row[2]
    if at_least <= Counter(password)[char] <= at_most:
        c += 1

print(c)


d = 0
for row in database:
    position1, position2 = [int(x) - 1 for x in row[0].split("-")]
    char = row[1][0]
    password = row[2]
    if (password[position1] == char) ^ (password[position2] == char):
        d += 1

print(d)
