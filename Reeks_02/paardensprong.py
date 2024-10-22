# https://dodona.be/nl/courses/4157/series/46288/activities/56374393

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

