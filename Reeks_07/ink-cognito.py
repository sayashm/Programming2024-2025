# https://dodona.be/nl/courses/4157/series/46296/activities/70555744


def product(s: list|tuple, *args: int|list|tuple)->int:
    '''
    >>> product([2, 3, 11, 23, 31])
    47058
    >>> product((2, 3, 7, 47, 395), 0)
    389865
    >>> product([2, 3, 7, 47, 583, 1223], 1, 3)
    9982126
    >>> product((2, 3, 7, 43, 3263, 4051, 2558951), 0, 2, 4)
    1337254054629
    '''

    from math import prod
    return prod(s[i] for i in range(len(s)) if i not in args)


def transform(s: list|tuple, i : int)->int:
    '''
    >>> transform([2, 3, 11, 23, 31], 0)
    11765
    >>> transform((2, 3, 11, 23, 31), 1)
    5229
    >>> transform([2, 3, 11, 23, 31], 2)
    389
    >>> transform((2, 3, 11, 23, 31), 3)
    89
    >>> transform([2, 3, 11, 23, 31], 4)
    49
    >>> transform((2, 3, 4, 5, 6), 3)
    29
    >>> transform((2, 3, 4, 5, 6), 4)
    Traceback (most recent call last):
    AssertionError: invalid transformation
    '''
    prod_result = (product(s, i) + 1)
    S = s[i]
    if prod_result % S == 0:
        return prod_result // S
    raise AssertionError("invalid transformation")


def transformation(*args : int|list|tuple)->list:
    '''
    >>> transformation(2, 3, 11, 23, 31)
    [11765, 5229, 389, 89, 49]
    >>> transformation(2, 3, 7, 47, 395)
    [194933, 86637, 15913, 353, 5]
    >>> transformation(2, 3, 7, 47, 583, 1223)
    [351869942, 156386641, 28724077, 637157, 4141, 941]
    >>> transformation(2, 3, 7, 43, 3263, 4051, 2558951)
    [15272109930890495, 6787604413729109, 1246702851501265, 33038636951629, 5737528889, 3722498629, 9329]
    >>> transformation(2, 3, 11, 25, 29, 1097, 2753)
    [36127240463, 16056551317, 1194288941, 231214339, 171829919, 120083, 19067]
    >>> transformation(2, 3, 4, 5, 6)
    Traceback (most recent call last):
    AssertionError: invalid transformation
    '''
    iterable = args[0] if isinstance(args[0], (list, tuple)) else args
    return [transform(iterable, ind) for ind in range(len(iterable))]



def ink_cognito(s: list|tuple , t: list|tuple) -> tuple:
    '''
    >>> ink_cognito([2, 3, 7, 47, None], [194933, None, None, 353, 5])
    ([2, 3, 7, 47, 395], [194933, 86637, 15913, 353, 5])
    >>> ink_cognito((2, 3, 11, None, 31), (None, 5229, 389, None, 49))
    ([2, 3, 11, 23, 31], [11765, 5229, 389, 89, 49])
    >>> ink_cognito([2, 3, 7, 47, 583, None], [None, None, None, None, None, 941])
    ([2, 3, 7, 47, 583, 1223], [351869942, 156386641, 28724077, 637157, 4141, 941])
    '''
    s , t = list(s) , list(t)
    sPosNone  = s.index(None)
    tPosNone  = [i for i,x in enumerate(t) if x is None]

    if sPosNone not in tPosNone:
        s[sPosNone] = (product(s, sPosNone)+1)// t[sPosNone]

    else:
        tPosNoNone = next(i for i, x in enumerate(t) if x is not None and i != sPosNone)
        s[sPosNone] = (s[tPosNoNone] * t[tPosNoNone] - 1) // product(s, sPosNone,tPosNoNone)

    return s, transformation(s)






