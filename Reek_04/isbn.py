# https://dodona.be/nl/courses/4157/series/46290/activities/174432505

s=[]

# Take ISBN by input and check the "STOP" order
a = True
while a :
    i = str(input(f'add number #{len(s)+1} or stop: '))

    if i.upper() == 'STOP':
        a = False
    else:
        s.append(i)

# Calculate and final check
for j in range(len(s)):
    x10 = sum([int(s[j][i]) * (i + 1) for  i in  range(len(s[j])-1)])%11
    x10c = 10 if s[j][9] == 'X' else int(s[j][9])
    print('OK') if x10 == x10c else print('WRONG')