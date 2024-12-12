# https://dodona.be/en/courses/4157/series/46294/activities/1782810096/
import string

def inventory(sentence: str)->str:
    '''
    >>> inventory('Data aequatione quotcunque fluentes quantitates involvente, fluxiones invenire; et vice versa.')
    '7accd14eff7i3l9n4o4qrr4s9t7u5vx'
    >>> inventory('ut tensio sic vis')
    'ce3ino3sttuv'
    '''
    letters = string.ascii_lowercase
    sentence = sentence.lower()
    res = ''
    for l in letters:
        c = sentence.count(l)
        if c > 2:
            res +=f'{c}{l}'
        elif 1 <= c <= 2:
            res += l * c

    return res



def unpack(sentence: str):
    '''
    >>> unpack('6accdae13eff7i3l9n4o4qrr4s8t12ux')
    'aaaaaaccdaeeeeeeeeeeeeeeffiiiiiiilllnnnnnnnnnooooqqqqrrssssttttttttuuuuuuuuuuuux'
    >>> unpack('ce3ino3sttuv')
    'ceiiinosssttuv'
    '''

    result = []
    number_str = []

    for ch in sentence:
        if ch.isdigit():
            number_str.append(ch)
        else:
            if number_str:
                count = int(''.join(number_str))
                result.append(ch * count)
                number_str.clear()
            else:
                result.append(ch)

    return ''.join(result)




def simplify(sentence: str)->str:
    '''
    >>> simplify('6accdae13eff7i3l9n4o4qrr4s8t12ux')
    '7accd14eff7i3l9n4o4qrr4s8t12ux'
    >>> simplify('i2scvotu2ietns')
    'ce3ino3sttuv'
    '''

    return inventory(unpack(sentence))











