# https://dodona.be/nl/courses/4157/series/46287/activities/910319224


x1 = int(input('x1 : '))*1
x2 = int(input('x2 : '))*2
x3 = int(input('x3 : '))*3
x4 = int(input('x4 : '))*4
x5 = int(input('x5 : '))*5
x6 = int(input('x6 : '))*6
x7 = int(input('x7 : '))*7
x8 = int(input('x8 : '))*8
x9 = int(input('x9 : '))*9

X = (x1, x2, x3, x4 ,x5, x6, x7, x8, x9)
Sum = sum(X)

x10 = Sum % 11
print(x10)