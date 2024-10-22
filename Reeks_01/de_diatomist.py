# https://dodona.be/nl/courses/4157/series/46287/activities/1633935550
import math

r  = float(input('please input the r of small circle: '))
R  = float(input('please input the R of small circle: '))

n =int( 0.83 * ( ( R ** 2 ) / ( r ** 2 ) ) - 1.9)
pi = math.pi
area1 = r**2 * pi * n
area2 = R**2 * pi

prop = area1/area2 * 100
print(f'{n} smaller circles cover {prop :.2f}% of the larger circle')
