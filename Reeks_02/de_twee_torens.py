# https://dodona.be/nl/courses/4157/series/46288/activities/2106206433


s1 = str(input('First scientist choose:'))
s2 = str(input('Second scientist choose:'))
w = str(input('Which one choose opposite:'))

if w == 'second':
    s1 = 'heads' if s1 == 'tails' else 'tails'
if w == 'first':
    s2 = 'heads' if s2 == 'tails' else 'tails'

print(s1)
print(s2)
