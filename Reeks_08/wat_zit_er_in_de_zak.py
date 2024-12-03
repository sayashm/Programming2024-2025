# https://dodona.be/nl/courses/4157/series/46297/activities/680840770

def fill(letters:str) -> dict:
    '''
    >>> bag = fill('IAMDIETINGIEATQUINCEJELLYLOTSOFGROUNDMAIZEGIVESVARIETYICOOKRHUBARBANDSODAWEEPANEWORPUTONEXTRAFLESH__')
    >>> bag
    {'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 'I': 9, 'J': 1, 'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2, 'Q': 1, 'R': 6, 'S': 4, 'T': 6, 'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1, '_': 2}
    '''

    from string import ascii_uppercase as upper

    freq = {}
    for letter in upper:
        if letter not in freq:
            if letters.count(letter) == 0:
                continue
            freq[letter] = letters.count(letter)

    if letters.count('_') !=0:
        freq['_'] = letters.count('_')


    return freq


def description(bag:dict)-> dict:
    '''
    >>> bag = fill('IAMDIETINGIEATQUINCEJELLYLOTSOFGROUNDMAIZEGIVESVARIETYICOOKRHUBARBANDSODAWEEPANEWORPUTONEXTRAFLESH__')
    >>> bag
    {'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 'I': 9, 'J': 1, 'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2, 'Q': 1, 'R': 6, 'S': 4, 'T': 6, 'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1, '_': 2}

    >>> description(bag)
    {1: {'J', 'K', 'Q', 'X', 'Z'}, 2: {'B', 'C', 'F', 'H', 'M', 'P', 'V', 'W', 'Y', '_'}, 3: {'G'}, 4: {'D', 'L', 'S', 'U'}, 6: {'N', 'R', 'T'}, 8: {'O'}, 9: {'A', 'I'}, 12: {'E'}}
    '''

    set(bag.values())

    descript = {}
    for letter in bag.keys():
        if bag[letter] not in descript:
            descript[bag[letter]] = {letter}

        else:
            descript[bag[letter]].add(letter)

    return descript


def remove(letters: str, bag: dict)->dict:
    '''
    >>> bag = fill('IAMDIETINGIEATQUINCEJELLYLOTSOFGROUNDMAIZEGIVESVARIETYICOOKRHUBARBANDSODAWEEPANEWORPUTONEXTRAFLESH__')
    >>> bag
    {'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 'I': 9, 'J': 1, 'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2, 'Q': 1, 'R': 6, 'S': 4, 'T': 6, 'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1, '_': 2}
    >>> description(bag)
    {1: {'J', 'K', 'Q', 'X', 'Z'}, 2: {'B', 'C', 'F', 'H', 'M', 'P', 'V', 'W', 'Y', '_'}, 3: {'G'}, 4: {'D', 'L', 'S', 'U'}, 6: {'N', 'R', 'T'}, 8: {'O'}, 9: {'A', 'I'}, 12: {'E'}}
    >>> remove('AEERTYOXMCNB_S', bag)
    >>> bag
    {'A': 8, 'B': 1, 'C': 1, 'D': 4, 'E': 10, 'F': 2, 'G': 3, 'H': 2, 'I': 9, 'J': 1, 'K': 1, 'L': 4, 'M': 1, 'N': 5, 'O': 7, 'P': 2, 'Q': 1, 'R': 5, 'S': 3, 'T': 5, 'U': 4, 'V': 2, 'W': 2, 'Y': 1, 'Z': 1, '_': 1}
    >>> description(bag)
    {1: {'B', 'C', 'J', 'K', 'M', 'Q', 'Y', 'Z', '_'}, 2: {'F', 'H', 'P', 'V', 'W'}, 3: {'G', 'S'}, 4: {'D', 'L', 'U'}, 5: {'N', 'R', 'T'}, 7: {'O'}, 8: {'A'}, 9: {'I'}, 10: {'E'}}
    >>> remove('XXX', bag)
    Traceback (most recent call last):
    AssertionError: not all letters are in the bag
    '''

    for letter in letters:
        if letter not in bag:
            raise AssertionError('not all letters are in the bag')
        bag[letter] -= 1
        if bag[letter] == 0:
            del bag[letter]
