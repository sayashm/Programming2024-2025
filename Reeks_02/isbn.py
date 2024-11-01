# https://dodona.be/nl/courses/4157/series/46288/activities/182880102

######################################
###              ISBN              ###
######################################

######################################
###           My Solution          ###
######################################

x1 = int(input('x1 : '))*1
x2 = int(input('x2 : '))*2
x3 = int(input('x3 : '))*3
x4 = int(input('x4 : '))*4
x5 = int(input('x5 : '))*5
x6 = int(input('x6 : '))*6
x7 = int(input('x7 : '))*7
x8 = int(input('x8 : '))*8
x9 = int(input('x9 : '))*9
x10 = int(input('x10 : '))

X = (x1, x2, x3, x4 ,x5, x6, x7, x8, x9)
Sum = sum(X)

x = Sum % 11

print('OK') if ( x10 == x ) else print('WRONG')

######################################
###         Sample Solution        ###
######################################

# # read ten digits of an ISBN-10 code (each on a separate line)
# x1 = int(input())
# x2 = int(input())
# x3 = int(input())
# x4 = int(input())
# x5 = int(input())
# x6 = int(input())
# x7 = int(input())
# x8 = int(input())
# x9 = int(input())
# x10 = int(input())
# # compute check digit
# check_digit = (
# x1 + 2 * x2 + 3 * x3 + 4 * x4 + 5 * x5 + 6 * x6 + 7 * x7 + 8 * x8 + 9 * x9
# ) % 11
# # check and output check digit
# print('OK' if x10 == check_digit else 'WRONG')
# # alternative solution:
# #
# # if x10 == check_digit:
# # print('OK')
# # else:
# # print('WRONG')
