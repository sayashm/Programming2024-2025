# https://dodona.be/nl/courses/4157/series/46291/activities/582137927


def multiplication(x):
    '''
    >>> multiplication(327)
    42
    >>> multiplication(42)
    8
    >>> multiplication(277777788888899)
    4996238671872
    '''
    m = 1
    for d in str(x):
        m = m * int(d)
    return(m)

def digital_root(x):
    '''
    >>> digital_root(327)
    8
    >>> digital_root(68889)
    0
    >>> digital_root(277777788888899)
    0
    '''
    while x>=10:
        x = multiplication(x)
    return(x)

def persistence(x):
    '''
    >>> persistence(327)
    2
    >>> persistence(8)
    0
    >>> persistence(277777788888899)
    11
    '''
    i = 0
    while x>=10:
        x = multiplication(x)
        i += 1
    return(i)

def most_persistent(a,b):
    '''
    >>> most_persistent(1, 100)
    77
    >>> most_persistent(100, 1000)
    679
    >>> most_persistent(1000, 10000)
    6788
    >>> most_persistent(277777788888000, 277777788889000)
    277777788888899
    '''
    l = []
    for i in range(a,b+1):
        p = persistence(i)
        l.append((i,p))

    tmax = max(l, key=lambda x :x[1])
    return(tmax[0])
