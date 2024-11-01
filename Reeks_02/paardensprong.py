# https://dodona.be/nl/courses/4157/series/46288/activities/56374393

######################################
###          Knight move           ###
######################################

######################################
###           My Solution          ###
######################################

p1 = str(input('First Position: '))
p2 = str(input('Second Position: '))

p1l , p1n = p1

p2l , p2n = p2

op1l = ord(p1l) - ord('a') +1
op2l = ord(p2l) - ord('a') +1

np1n = int(p1n)
np2n = int(p2n)

possible = [
    (op1l +1 , np1n +2),
    (op1l -1 , np1n +2),
    (op1l +1 , np1n -2),
    (op1l -1 , np1n -2),
    (op1l +2 , np1n +1),
    (op1l -2 , np1n +1),
    (op1l +2 , np1n -1),
    (op1l -2 , np1n -1),
]

print(f'a knight can jump from {p1} to {p2}') if (op2l , np2n) in possible else print(f'a knight cannot jump from {p1} to {p2}')

######################################
###         Sample Solution        ###
######################################

# # read two given position on chess board
# position1 = input()
# position2 = input()
# # decompose positions into row and column indices
# col1, row1 = position1
# col2, row2 = position2
# # convert row indices into integers
# row1, row2 = int(row1), int(row2)
# # convert column indices into integers (zero-based)
# col1 = ord(col1) - ord('a')
# col2 = ord(col2) - ord('a')
# # determine whether a knight can move between two given positions: this is the case if it
# #       jumps over one column and two
# # rows or one row and two columns
# conclusion = '' if {abs(row1 - row2), abs(col1 - col2)} == {1, 2} else 'not'
# print(f'a knight can{conclusion} jump from {position1} to {position2}')