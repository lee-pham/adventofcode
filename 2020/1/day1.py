import random
import math

with open('day1.txt') as f:
    puzzle_input = f.read()

expense_report = [int(x) for x in puzzle_input.split("\n")]


for expense in expense_report:
    difference = 2020 - expense
    if difference in expense_report:
        print(expense * difference)
        break


while sum(random3 := random.sample(expense_report, 3)) != 2020:
    pass

print(math.prod(random3))
