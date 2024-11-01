# https://dodona.be/nl/courses/4157/series/46288/activities/328212300
######################################
###        Personal warmth         ###
######################################

######################################
###           My Solution          ###
######################################
import math

t = float(input('Enter your body temperature: '))

e = math.e

r = 100/t


if r < e-0.1:
    print("you have a fever")
elif r > e+0.1:
    print("you have hypothermia")
else:
    print("you have a normal body temperature")

######################################
###         Sample Solution        ###
######################################

# # read body temperature
# body_temperature = float(input())
# # make estimate of e
# estimate = 100 / body_temperature
# # make diagnosis from body temperature
# eps = 0.1
# if estimate < math.e - eps:
#     diagnosis = 'you have a fever'
# elif estimate > math.e + eps:
#     diagnosis = 'you have hypothermia'
# else:
#     diagnosis = 'you have a normal body temperature'
# # output diagnosis
# print(diagnosis)



