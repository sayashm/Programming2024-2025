# https://dodona.be/nl/courses/4157/series/46288/activities/1357047316


######################################
###            Mondrian            ###
######################################

######################################
###           My Solution          ###
######################################

x , y = float(input('x = ')) , float(input('y = '))

if x <6.3 and y <6:
    print('blue') if 2.2 < x < 4 and y < 2 else print('white')

elif 6.3< x and y <6:
    if y <2.6:
        print('yellow')
    elif 2.6< y <4.1:
        print('white')
    else:
        print('blue')

elif 6 < y:
    print('red') if x <4.65 else print('white')


######################################
###         Sample Solution        ###
######################################

# # read coordinate of point on painting
# x, y = float(input()), float(input())
# # determine color of rectangle that contains the given point
# if x < 4.65 and y > 6.0:
#     color = 'red'
# elif x > 6.3 and y < 2.6:
#     color = 'yellow'
# elif (2.2 < x < 4.0 and y < 2) or (x > 6.3 and 4.1 < y < 6.0):
#     color = 'blue'
# else:
#     color = 'white'
#     # print the color
# print(color)





