x = 7 * 512 ** 1912 + 6 * 64 ** 1954 - 5 * 8 ** 1991 - 4 * 8 ** 1980 - 2022
count = 0
while x != 0:
    if x % 8 == 7:
        count += 1
    x //= 8
print(count)
