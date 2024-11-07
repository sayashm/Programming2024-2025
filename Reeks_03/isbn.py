# https://dodona.be/nl/courses/4157/series/46289/activities/1898834779
s=[]
while True :
    i = str(input(f'add number #{len(s)+1} or stop: '))
    if i == 'stop':
        break
    try:
        s.append(int(i))
    except:
        print("Please enter a valid number or 'stop'.")

val = [s[i:i+10] for i in range(0, len(s)-9, 10)]

for i in range(len(val)):
    S = val[i][0:9]
    x1x9 = []
    for n in range(9):
        x1x9.append(S[n]*(n+1))
    x10 = sum(x1x9) % 11
    x10t = val[i][9]
    print('OK') if x10 == x10t else print("WRONG")