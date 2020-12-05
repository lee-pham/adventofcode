from collections import Counter
a = 367479
b = 893698
password_count = 0
for i in range(a, b + 1):
    ordered_password = ''.join(sorted(str(i)))
    if str(i) == ordered_password and Counter(ordered_password).most_common(1)[0][1] >= 2:
        password_count += 1

print(password_count)


''''''''''''''
''' Part 2 '''
''''''''''''''

password_count = 0
for i in range(a, b + 1):
    ordered_password = ''.join(sorted(str(i)))
    if str(i) == ordered_password and 2 in Counter(ordered_password).values():
        password_count += 1

print(password_count)
