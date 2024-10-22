# https://dodona.be/nl/courses/4157/series/46289/activities/1419328999

numstr = int(input('number? '))
num = numstr
print(num)

while numstr > 7 :
    numstr = int(str(numstr)[:-1]) + (5 * int(str(numstr)[-1]))
    print(numstr)
    if numstr == 49:
        print(f'{num} is divisible by 7')
        break
    else:
        if numstr != 7 and numstr < 10:
            print(f'{num} is not divisible by 7')
            break
        elif numstr == 7:
            print(f'{num} is divisible by 7')
            break





