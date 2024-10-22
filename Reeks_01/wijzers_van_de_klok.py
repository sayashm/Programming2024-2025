# https://dodona.be/nl/courses/4157/series/46287/activities/1381266978

h = int(input('please enter the hour:'))
m = int(input('please enter the minute: '))

if 0<=h<=24 and 0<=m<=59:
    if h>=12:
        h0 = h-12
        dh = (h0 * 5 * 6) + ((m / 60) * 5 * 6)
    else:
        dh = (h * 5 * 6) + ((m / 60) * 5 * 6)

    dm = m * 6

    degree1 = abs(dm - dh)
    degree2 = 360 - degree1

    degree = min(degree2, degree1)

    target = 2
    hp = str(h)
    hp = hp.zfill(target)

    mp = str(m)
    mp = mp.zfill(target)

    print(f'At {hp}:{mp} both hands form an angle of {degree:.1f}°.')

else:
    if h>=24 or h <= 0:
        print('the hour cannot be more than 24 hr or less than 0 hr')
    if m>=59 or m <= 0:
        print('the minute cannot be more than 59 min or less than 0 min')




