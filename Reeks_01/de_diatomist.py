# https://dodona.be/nl/courses/4157/series/46287/activities/1633935550
import math

######################################
###         The diatomist          ###
######################################

######################################
###           My Solution          ###
######################################

r  = float(input('please input the r of small circle: '))
R  = float(input('please input the R of small circle: '))

n =int( 0.83 * ( ( R ** 2 ) / ( r ** 2 ) ) - 1.9)
pi = math.pi
area1 = r**2 * pi * n
area2 = R**2 * pi

prop = area1/area2 * 100
print(f'{n} smaller circles cover {prop :.2f}% of the larger circle')


######################################
###         Sample Solution        ###
######################################

# # read diameter of smaller and larger circles
# r = float(input())
# R = float(input())
# # estimate number of smaller circles that fit into larger circle
# count = math.floor(0.83 * (R ** 2 / r ** 2) - 1.9)
# # determine coverage of larger circle (percentage)
# area_large = math.pi * R ** 2
# area_small = math.pi * r ** 2
# coverage = (count * area_small) / area_large * 100
# # output number of circles and coverage of larger circle
# print(f'{count} smaller circles cover {coverage:.2f}% of the larger circle')