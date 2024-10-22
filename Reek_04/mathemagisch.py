# https://dodona.be/nl/courses/4157/series/46290/activities/1260445672

num = input('An n-digit (n>=4) number, written without leading zeros: ')
l = len(num)
s = []
for i in range(l):
    splitnum = num[:i]+num[i+1:]
    intnum = int(splitnum)
    s.append(int(splitnum))
    if i+1 == l:
        print(f'{"+":<2s}{str(intnum)}')
    else:
        print(f'{str(intnum):>{l+1}s}')



e = '='
print(f'{e *(l+1)}\n {sum(s)}')
