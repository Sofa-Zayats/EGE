x = 3 * 4 ** 38 + 2 * 4 ** 23 + 4 ** 20 + 3 * 4 ** 4 + 1
count = 0
while x != 0:
    if x % 16 == 0:
        count += 1
    x //= 16
print(count)
