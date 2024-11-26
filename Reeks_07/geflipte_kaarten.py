# https://dodona.be/nl/courses/4157/series/46296/activities/165334097


cards = [(5, 9), (6, 10), (2, 7), (1, 8), (4, 3)]

def visible(cards:list) -> int :
    '''
    >>> cards = [(5, 9), (6, 10), (2, 7), (1, 8), (4, 3)]
    >>> visible(cards)
    18
    '''
    return sum([i[0] for i in cards ])


def maximum(cards) -> int:
    '''
    >>> maximum(cards)
    38
    '''
    return sum([max(i) for i in cards])




def flip(cards:list, selection:list|tuple = None):
    '''
    >>> flip(cards)
    >>> cards
    [(9, 5), (10, 6), (7, 2), (8, 1), (3, 4)]
    >>> visible(cards)
    37
    >>> flip(cards, [3])
    >>> cards
    [(9, 5), (10, 6), (7, 2), (8, 1), (4, 3)]
    >>> visible(cards)
    38
    >>> flip(cards, [1])
    Traceback (most recent call last):
    AssertionError: invalid selection
    >>> cards
    [(9, 5), (10, 6), (7, 2), (8, 1), (4, 3)]
    >>> flip(cards, (9, 10, 2))
    Traceback (most recent call last):
    AssertionError: invalid selection
    >>> cards
    [(9, 5), (10, 6), (7, 2), (8, 1), (4, 3)]
    >>> flip(cards, (4, 7, 9))
    >>> cards
    [(5, 9), (10, 6), (2, 7), (8, 1), (3, 4)]
    >>> visible(cards)
    28

    '''

    if selection is None:
        for inx , (i ,j) in enumerate(cards):
            cards[inx] = (j , i)

    else:
        if not set(selection).issubset([i for i, j in cards]):
            raise AssertionError("invalid selection")

        for inx, (i, j) in enumerate(cards):
            if i in selection:
                cards[inx] = (j, i)


def isvalid(cards) -> bool:
    '''
    >>> isvalid(cards)
    True
    >>> isvalid([(5, 9), (10, 6), (8, 1), (3, 4)])
    False
    >>> isvalid([(5, 9), (10, 6), (9, 7), (8, 1), (3, 4)])   # twice 9, no 2
    False
    '''

    return set(range(1, 2*len(cards)+1)) == {elem for pair in cards for elem in pair}

def generate_cards(n:int)->list:
    '''
    >>> generate_cards(5)   # doctest: +SKIP
    [(9, 5), (8, 1), (2, 3), (6, 4), (7, 10)]
    >>> generate_cards(5)   # doctest: +SKIP
    [(2, 3), (4, 1), (7, 8), (9, 10), (6, 5)]
    '''

    from random import shuffle

    l = list(range(1, 2*n+1))
    shuffle(l)

    return [(l[(2 * i - 1)-1], l[(2 * i)-1]) for i in range(1, n+1)]



if __name__ == '__main__':
    import doctest
    doctest.testmod()