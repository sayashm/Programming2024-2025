# https://dodona.be/nl/courses/4157/series/46296/activities/387454511

def isISBN13(code: str):
    if not isinstance(code, str) or len(code) != 13:
        return False
    try:
        o = sum(int(code[i]) for i in range(0, 12, 2))
        e = sum(int(code[i]) for i in range(1, 12, 2))
        X13 = (10 - (o + 3 * e) % 10) % 10
        return X13 == int(code[-1])
    except:
        return False

def isISBN10(code: str):
    if not isinstance(code, str) or len(code) != 10:
        return False
    try:
        x10 = sum(int(code[i]) * (i + 1) for i in range(9)) % 11
        x10t = 10 if code[9].upper() == 'X' else int(code[9])
        return x10 == x10t
    except:
        return False

def isISBN(code : str, isbn13:bool = True ):
    '''
    >>> isISBN('9789027439642', False)
    False
    >>> isISBN('9789027439642', True)
    True
    >>> isISBN('9789027439642')
    True
    >>> isISBN('080442957X')
    False
    >>> isISBN('080442957X', False)
    True
    >>> isISBN('8397833414060', False)
    False
    '''

    if isbn13:
        return isISBN13(code)
    else:
        return isISBN10(code)


codes = ['0012345678', '0012345679', '9971502100', '080442957X', 5, True, 'The Practice of Computing Using Python', '9789027439642', '5486948320146']

def areISBN(codes: list, isbn13: bool = None):
    '''
    >>> areISBN(codes)
    [False, True, True, True, False, False, False, True, False]
    >>> areISBN(codes, True)
    [False, False, False, False, False, False, False, True, False]
    >>> areISBN(codes, False)
    [False, True, True, True, False, False, False, False, False]
    '''

    if isbn13 == None:
        return [isISBN13(code) if isinstance(code, str) and len(code) == 13 else
                isISBN10(code) if isinstance(code, str) else
                False
                for code in codes]

    return [ isISBN(code, isbn13) for code in codes]


