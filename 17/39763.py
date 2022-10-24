with open('39763.txt')as f:
    a = list(map(int,f.readlines()))
    count = 0
    m = 0
    for i in range(len(a)-2):
        h = max(a[i], a[i + 1], a[i + 2])
        c1 = min(a[i], a[i + 1], a[i + 2])
        c2 = 
#c**2<a**2+b**2

