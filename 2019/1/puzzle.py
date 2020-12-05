with open('input.txt') as f:
    masses = f.readlines()

masses = [int(x) for x in masses]

test_input = (12, 14, 1969, 100756)
test_output = (2, 2, 654, 33583)


def calculate_fuel(mass):
    return mass // 3 - 2

print(sum([calculate_fuel(x) for x in masses]))


def adv_calculate_fuel(mass):
    total = 0
    delta = calculate_fuel(mass)
    while delta >= 0:
        total += delta
        delta = calculate_fuel(delta)
    return total

print(sum([adv_calculate_fuel(x) for x in masses]))
