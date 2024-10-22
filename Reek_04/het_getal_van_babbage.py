# https://dodona.be/nl/courses/4157/series/46290/activities/1314977477

import math

steps = int(input('How many? '))
number = str(input('The number? '))

j = 0

if math.sqrt(int(number)).is_integer() and number[0] != '0':
    s = int(math.sqrt(int(number)))
    print(f'{s} * {s} = {number}')
    j += 1

i = 1
while True:
    if j == steps:
        break
    else:
        m = str(i)+number
        if math.sqrt(int(m)).is_integer():
            s = int(math.sqrt(int(m)))
            print(f'{s} * {s} = {m}')
            j+=1

        i+=1
