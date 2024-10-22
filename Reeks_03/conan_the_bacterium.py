# https://dodona.be/nl/courses/4157/series/46289/activities/1462225048

a, b , n , t = int(input('a? ')), int(input('b? ')), int(input('n? ')), int(input('t? '))
z = 1
for i in range(n):
    z = a * z + b

zt = t
s = 0
while zt < z:
    zt = a * zt + b
    s += 1


print(f'experiment #1: {z} cells after {n} seconds\nexperiment #2: {zt} cells after {s} seconds')