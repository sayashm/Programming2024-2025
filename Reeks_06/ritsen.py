# https://dodona.be/nl/courses/4157/series/46295/activities/1325500143


from itertools import zip_longest
def merge(L , D):
    '''
    >>> merge(('A', 'B', 'C'),  [1, 2, 3])
    ['A', 1, 'B', 2, 'C', 3]
    >>> merge(['A'], [1, 2, 3, 4])
    ['A', 1]
    >>> merge(('A', 'B'),  (1, 2, 3, 4))
    ['A', 1, 'B', 2]
    >>> merge(('A', 'B', 'C'),  [1, 2])
    ['A', 1, 'B', 2]
    '''

    return [item for pair in zip(L,D) for item in pair]

def weave(L , D):
    '''
    >>> weave(('A', 'B', 'C'),  [1, 2, 3])
    ['A', 1, 'B', 2, 'C', 3]
    >>> weave(['A'], [1, 2, 3, 4])
    ['A', 1, 'A', 2, 'A', 3, 'A', 4]
    >>> weave(('A', 'B'),  (1, 2, 3, 4))
    ['A', 1, 'B', 2, 'A', 3, 'B', 4]
    >>> weave(('A', 'B', 'C'),  [1, 2])
    ['A', 1, 'B', 2, 'C', 1]
    '''

    n = max(len(L), len(D))
    L = (L * (n // len(L) + 1))[:n]
    D = (D * (n // len(D) + 1))[:n]
    return [item for pair in zip(L, D) for item in pair]


def zipper(L , D):
    '''
    >>> zipper(('A', 'B', 'C'),  [1, 2, 3])
    ['A', 1, 'B', 2, 'C', 3]
    >>> zipper(['A'], [1, 2, 3, 4])
    ['A', 1, 2, 3, 4]
    >>> zipper(('A', 'B'),  (1, 2, 3, 4))
    ['A', 1, 'B', 2, 3, 4]
    >>> zipper(('A', 'B', 'C'),  [1, 2])
    ['A', 1, 'B', 2, 'C']
    '''

    return [item for pair in zip_longest(L, D) for item in pair if item is not None]






