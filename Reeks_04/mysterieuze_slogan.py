# https://dodona.be/nl/courses/4157/series/46290/activities/1628407499

text = input('a text fragment that hides a secret message: ')
p = int(input('starting position: '))
s = int(input('step size: '))

n = len(text)

# y luaeb h o dtyo aoosgl

current_position = p % n

retext = ''
for ـ in range(n):
    retext = retext + text[current_position]
    current_position = (current_position + s) % n
print(retext)
