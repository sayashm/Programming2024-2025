# https://dodona.be/nl/courses/4157/series/46288/activities/2106206433

######################################
###         The two towers         ###
######################################

######################################
###           My Solution          ###
######################################
s1 = str(input('First scientist choose:'))
s2 = str(input('Second scientist choose:'))
w = str(input('Which one choose opposite:'))

if w == 'second':
    s1 = 'heads' if s1 == 'tails' else 'tails'
else:
    s2 = 'heads' if s2 == 'tails' else 'tails'

print(s1)
print(s2)

######################################
###         Sample Solution        ###
######################################
# # read outcome of two coin tosses
# # NOTE: outcomes are converted to Boolean values (head -> True, tail -> False) in order to
# #       simplify the implementation
# coin1 = input() == 'heads'
# coin2 = input() == 'heads'
# # read which scientist will say the same as his own outcome
# same = input()
# # determine response of both scientists based on the outcome of their own throws and the
# #       agreement who will say the
# # same and who will say the opposite
# if same == 'first':
# coin2 = not coin2
# else:
# coin1 = not coin1
# # output response of first scientist
# print('heads' if coin1 else 'tails')
# # output response of second scientist
# print('heads' if coin2 else 'tails')