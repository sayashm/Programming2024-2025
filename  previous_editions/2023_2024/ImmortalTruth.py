# https://dodona.be/en/courses/2802/series/29671/activities/1737773601/
s=[]
for _ in range(0,6):
    i = str(input(f'add number #{len(s)+1} or stop: '))
    if i == 'stop':
        break
    try:
            s.append(str(int(i)))
    except:
        print("Please enter a valid number or 'stop'.")
#
# s= [
#     "123789",
#     "561945",
#     "642864",
#     "242868",
#     "323787",
#     "761943"
# ]

l = len(s)
hl = l//2
s1 , s2 = s[:hl] , s[hl:]

lnum = len(s1[0])

for digit in range(lnum):
    # st11 = ''
    # for num in s1:
    #     st11 += f'{num[:digit+1]:<{lnum+1}s}+ '
    # st21  = ''
    # for num in s2:
    #     st21 += f'{num[:digit+1]:<{lnum+1}s}+ '
    left = ' + '.join([f'{num[:digit+1]:<{lnum}}' for num in s1])
    right = ' + '.join([f'{num[:digit+1]:<{lnum}}' for num in s2])

    eq = '=' if eval(left) == eval(right) else '≠'
    print(f'{left} {eq} {right}'.rstrip())


for digit in range(lnum-1):
    # st12 = ''
    # for num in s1:
    #     st12 += f'{num[digit+1:lnum]:>{lnum}s} + '
    # st22 = ''
    # for num in s2:
    #     st22 += f'{num[digit+1:lnum]:>{lnum}s} + '
    left = ' + '.join([f'{num[digit+1:]:>{lnum}}' for num in s1])
    right = ' + '.join([f'{num[digit+1:]:>{lnum}}' for num in s2])

    eq = '=' if eval(left) == eval(right) else '≠'
    print(f'{left} {eq} {right}'.rstrip())


