# https://dodona.be/nl/courses/4157/series/46291/activities/811362724

def encode_letter(L):
    '''
    >>> encode_letter('V')
    (5, 1)
    >>> encode_letter('i')
    (2, 4)
    '''

    alphabets = list(map(chr, range(97, 123)))
    alphabets.remove('k')
    dv_alphabets = [alphabets[i:i + 5] for i in range(0, 25, 5)]

    L = str(L).lower()

    if L=='k':
        L = 'c'
    for i in range(5):
        if L in dv_alphabets[i]:
           return (i+1 , dv_alphabets[i].index(L)+1)


def encode(word):
    '''
    >>> encode('VICTOR')
    '..... . .. .... . ... .... .... ... .... .... ..'
    >>> encode('Charlie')
    '. ... .. ... . . .... .. ... . .. .... . .....'
    '''
    s = ''
    for l in word:
        en_Let = encode_letter(l)
        s += '.' * en_Let[0] + ' ' + '.'*en_Let[1] + ' '
    return s[:-1]

def decode_letter(a,b):
    '''
    >>> decode_letter(5, 1)
    'V'
    >>> decode_letter(2, 4)
    'I'
    '''
    alphabets = list(map(chr, range(97, 123)))
    alphabets.remove('k')
    dv_alphabets = [alphabets[i:i + 5] for i in range(0, 25, 5)]

    return dv_alphabets[a-1][b-1].upper()

def decode(code):
    '''
    >>> decode('..... . .. .... . ... .... .... ... .... .... ..')
    'VICTOR'
    >>> decode('. ... .. ... . . .... .. ... . .. .... . .....')
    'CHARLIE'
    '''
    word = ''
    code = code.split(' ')
    l = int(len(code)/2)
    for i in range(1, l+1) :
        word += decode_letter(len(code[(2*(i)) - 2]), len(code[2*(i)-1]))

    return word







