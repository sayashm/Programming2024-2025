# https://dodona.be/nl/courses/4157/series/46288/activities/408865752


first = str(input('Which one is lighter? '))
second = str(input('Which one is lighter? '))

if first == 'right':
    m = 0
    if second == 'right':
        n = 0
    elif second == 'left':
        n = 1
    else:
        n = 2
elif first == 'left':
    m = 1
    if second == 'right':
        n = 0
    elif second == 'left':
        n = 1
    else:
        n = 2
else:
    m = 2
    if second == 'right':
        n = 0
    elif second == 'left':
        n = 1
    else:
        n = 2

c = (3 * m) + n +1
print(f'coin #{c} is counterfeit')

