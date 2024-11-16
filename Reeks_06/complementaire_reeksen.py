# https://dodona.be/nl/courses/4157/series/46295/activities/1096544639

def isincreasing(L):
    '''
    >>> isincreasing([2, 3, 5, 7, 11, 13])
    True
    >>> isincreasing((0, 0, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 6))
    True
    >>> isincreasing([5, 3, 2, 7, 8, 1, 9])
    False
    '''

    return all(x <= y for x , y in zip(L, L[1:]))


def frequency_sequence(L):
    '''
    >>> frequency_sequence([2, 3, 5, 7, 11, 13])
    [0, 0, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 6]
    >>> frequency_sequence((0, 0, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 6))
    [2, 3, 5, 7, 11, 13, 14]
    >>> frequency_sequence([5, 3, 2, 7, 8, 1, 9])
    Traceback (most recent call last):
    AssertionError: given sequence is not increasing
    '''

    if not isincreasing(L):
        raise AssertionError("given sequence is not increasing")

    res = []
    count = 0
    index = 0
    n = max(L) + 1
    length = len(L)

    for i in range(n):
        while index < length and L[index] == i:
            index += 1
            count += 1
        res.append(count)

    return res



def lift(L):
    '''
    >>> lift([2, 3, 5, 7, 11, 13])
    [3, 5, 8, 11, 16, 19]
    >>> lift((0, 0, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 6))
    [1, 2, 4, 6, 7, 9, 10, 12, 13, 14, 15, 17, 18, 20]
    >>> lift([5, 3, 2, 7, 8, 1, 9])
    [6, 5, 5, 11, 13, 7, 16]
    '''

    return [sum(t) for t in [(x+1, y) for x, y in zip(range(len(L)), L)]]

def complementary_sequences(L):
    '''
    >>> complementary_sequences([2, 3, 5, 7, 11, 13])
    ([3, 5, 8, 11, 16, 19], [1, 2, 4, 6, 7, 9, 10, 12, 13, 14, 15, 17, 18, 20])
    >>> complementary_sequences((1, 3, 3, 5, 5, 5, 7, 7, 7, 7))
    ([2, 5, 6, 9, 10, 11, 14, 15, 16, 17], [1, 3, 4, 7, 8, 12, 13, 18])
    >>> complementary_sequences([5, 3, 2, 7, 8, 1, 9])
    Traceback (most recent call last):
    AssertionError: given sequence is not increasing
    '''

    return (lift(L) , lift(frequency_sequence(L)))




