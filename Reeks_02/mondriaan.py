# https://dodona.be/nl/courses/4157/series/46288/activities/1357047316

x , y = float(input('x = ')) , float(input('y = '))

if 0< x <6.3 and 0< y <6:
    print('blue') if 2.2 < x < 4 and 0 < y < 2 else print('white')

elif 6.3< x <10 and 0< y <6:
    if 0< y <2.6:
        print('yellow')
    elif 2.6< y <4.1:
        print('white')
    else:
        print('blue')

elif 6 < y <10 and 0<x<10:
    print('red') if 0< x <4.65 else print('white')





