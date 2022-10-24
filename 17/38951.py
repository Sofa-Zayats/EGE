with open('38951.txt') as f:
    numbers = list(map(int, f.readlines()))
    count = 0
    m = 0
    for i in range(len(numbers) - 1):
        if (numbers[i] % 3 == 0 or numbers[i + 1] % 3 == 0) and (numbers[i] + numbers[i + 1]) % 5 == 0:
            count += 1
            m = max(m, numbers[i] + numbers[i + 1])
    print(count, m)