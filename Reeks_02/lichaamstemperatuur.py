# https://dodona.be/nl/courses/4157/series/46288/activities/328212300
import math

t = float(input('Enter your body temperature: '))

e = math.e

r = 100/t


if r < e-0.1:
    print("you have a fever")
elif r > e+0.1:
    print("you have hypothermia")
elif e-0.1 <= r <= e+0.1:
    print("you have a normal body temperature")

