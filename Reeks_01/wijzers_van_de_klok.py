# https://dodona.be/nl/courses/4157/series/46287/activities/1381266978


######################################
###           Heartbeats           ###
######################################

######################################
###           My Solution          ###
######################################


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
    elif m>=59 or m <= 0:
        print('the minute cannot be more than 59 min or less than 0 min')

######################################
###         Sample Solution        ###
######################################

# read time on a 24-hour clock
# hours = int(input())
# minutes = int(input())
# # # determine angle that minute hand makes (from 12 o’clock)
# # angle_minute = minutes / 60
# #
# # # determine angle that hour hand makes (from 12 o’clock); take into account that
# # # the hour hand also progresses as the minutes pass by
# # angle_hour = (hours % 12 + angle_minute) / 12
# #
# # # determine one of the angles between both hands
# # angle_hands = (360 * (angle_hour - angle_minute)) % 360
# # some simple arithmetic reduces the above three statements to
# angle_hands = (30 * hours - 5.5 * minutes) % 360
# # determine smallest angle between both hands
# angle_hands = min(angle_hands, 360 - angle_hands)
# # output the smallest angle between both hands
# print(f'At {hours:02d}:{minutes:02d} both hands form an angle of {angle_hands:.1f}ˇ r.')




