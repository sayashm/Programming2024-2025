# https://dodona.be/nl/courses/4157/series/46288/activities/408865752

######################################
###         Counterfeiting         ###
######################################

######################################
###           My Solution          ###
######################################

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


######################################
###         Sample Solution        ###
######################################

# # find group that contains the counterfeit coin based on the first weighing:
# # group 0 = 1-2-3; group 1 = 4-5-6; group 2 = 7-8-9
# weighing = input()
# group = 0 if weighing == 'right' else (1 if weighing == 'left' else 2)
# # determine which coin in the group is counterfeit
# weighing = input()
# coin = 1 if weighing == 'right' else (2 if weighing == 'left' else 3)
# # indicate which coin is counterfeit
# print(f'coin #{3 * group + coin} is counterfeit')
