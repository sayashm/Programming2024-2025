# https://dodona.be/en/courses/1659/series/18380/activities/1936992119/

# two string input taking:
s=[]
for _ in range(0,2):
    i = str(input(f'add number #{len(s)+1} or stop: '))
    if i == 'stop':
        break
    try:
            s.append(str(i))
    except:
        print("Please enter a valid number or 'stop'.")



# Make dictionary for each letter:

letters = {'****':'C', '*o**':'D', '***o':'E', '*o*o':'F', 'oo**':'G', 'oo*o':'A', 'o*oo':'B', 'oooo':'C'}

def checker(w:str):
    for i in w:
        if  i not in 'o*':
            return False
    return True

if len(s[0]) == len(s[1]) and len(s[0])//2 !=0 and len(s[1])//2 !=0 and  checker(s[0]) and checker(s[1]):
    l1  = [s[0][i:i+2] for i in range(0, len(s[0]),2)]
    l2  = [s[1][i:i+2] for i in range(0, len(s[1]),2)]

    result =  ''.join(str(letters[l1[i]+l2[i]]) if l1[i]+l2[i] in letters else '?' for i in range(len(l1)) )
    print(result)

else:
    print('MYSTERY GUEST')




