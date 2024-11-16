# https://dodona.be/nl/courses/4157/series/46295/activities/636597847
from itertools import permutations


def next(L):
    '''
    >>> next([32, 9, 14, 3])
    (23, 5, 11, 29)
    >>> next((1, 2, 1, 2, 1, 0))
    (1, 1, 1, 1, 1, 1)
    >>> next((1, 2, 1, 2, 1, 1))
    (1, 1, 1, 1, 0, 0)
    '''

    return tuple([abs(x-y)  for x,y in zip(L, L[1:]+L[:1])])


def ducci(L):
    '''
    >>> ducci([32, 9, 14, 3])
    ((32, 9, 14, 3), (23, 5, 11, 29), (18, 6, 18, 6), (12, 12, 12, 12), (0, 0, 0, 0))
    >>> ducci((1, 2, 1, 2, 1, 0))
    ((1, 2, 1, 2, 1, 0), (1, 1, 1, 1, 1, 1), (0, 0, 0, 0, 0, 0))
    >>> ducci((1, 2, 1, 2, 1, 1))
    ((1, 2, 1, 2, 1, 1), (1, 1, 1, 1, 0, 0), (0, 0, 0, 1, 0, 1), (0, 0, 1, 1, 1, 1), (0, 1, 0, 0, 0, 1), (1, 1, 0, 0, 1, 1), (0, 1, 0, 1, 0, 0), (1, 1, 1, 1, 0, 0))
    '''

    res = [tuple(L)]
    tres = next(L)
    while tres not in res:
        res.append(tres)
        tres = next(res[-1])

    if sum(tres) != 0:
        res.append(tres)

    return tuple(res)

def period(L):
    '''
    >>> period([32, 9, 14, 3])
    0
    >>> period((1, 2, 1, 2, 1, 0))
    0
    >>> period((1, 2, 1, 2, 1, 1))
    6
    '''

    return 0 if sum(ducci(L)[-1]) == 0 else len(ducci(L)) - (ducci(L).index(ducci(L)[-1])+1)


