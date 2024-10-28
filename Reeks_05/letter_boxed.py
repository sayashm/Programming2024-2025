# https://dodona.be/nl/courses/4157/series/46291/activities/1263323198

def side(letter , puzzle):
    '''
    >>> side('O', 'YOI-RCM-VSA-LTE')
    0
    >>> side('V', 'YOI-RCM-VSA-LTE')
    2
    >>> side('E', 'YOI-RCM-VSA-LTE')
    3
    >>> side('X', 'YOI-RCM-VSA-LTE')
    -1
    '''
    split_puzzle = puzzle.split('-')
    for index, part in enumerate(split_puzzle):
        if letter in part:
            return index
    return -1

def iscomplete(solution , puzzle):
    '''
    >>> iscomplete('MYSTIC-CORAL-LIVER', 'YOI-RCM-VSA-LTE')
    True
    >>> iscomplete('DENIM-MAIZE-EGGPLANT', 'GND-IET-MZL-AP')
    True
    >>> iscomplete('GAINSBORO-ONYX-PEAR', 'BGY-NXE-PAO-SRI')
    True
    >>> iscomplete('KOBI-PLATINUM-ZOMP', 'TML-OZB-IUK-APN')
    True
    >>> iscomplete('DESERT-TEAL-LIVID', 'SIT-EVW-ADC-KLR')
    False
    >>> iscomplete('RUFOUS-SKOBELOFF', 'FL-XUM-SKE-BOR')
    False
    >>> iscomplete('DENIM-OPAL-MANDARIN', 'NMO-AI-LDR-EYP')
    False
    >>> iscomplete('BONE-SEPIA-BROWN', 'ODI-VAR-BEP-SNW')
    False
    '''
    set_solution = set(solution.replace('-',''))
    set_puzzle = set(puzzle.replace('-',''))

    return set_puzzle.issubset(set_solution)

def isconsecutive(solution):
    '''
    >>> isconsecutive('MYSTIC-CORAL-LIVER')
    True
    >>> isconsecutive('DENIM-MAIZE-EGGPLANT')
    True
    >>> isconsecutive('GAINSBORO-ONYX-PEAR')
    False
    >>> isconsecutive('KOBI-PLATINUM-ZOMP')
    False
    >>> isconsecutive('DESERT-TEAL-LIVID')
    True
    >>> isconsecutive('RUFOUS-SKOBELOFF')
    True
    >>> isconsecutive('DENIM-OPAL-MANDARIN')
    False
    >>> isconsecutive('BONE-SEPIA-BROWN')
    False
    '''

    split_solution = solution.split('-')
    b = True

    for i in range(len(split_solution) - 1):
        if split_solution[i][-1] != split_solution[i + 1][0]:
            return False
    return True

def iscrossing(solution, puzzle):
    '''
    >>> iscrossing('MYSTIC-CORAL-LIVER', 'YOI-RCM-VSA-LTE')
    True
    >>> iscrossing('DENIM-MAIZE-EGGPLANT', 'GND-IET-MZL-AP')
    False
    >>> iscrossing('GAINSBORO-ONYX-PEAR', 'BGY-NXE-PAO-SRI')
    True
    >>> iscrossing('KOBI-PLATINUM-ZOMP', 'TML-OZB-IUK-APN')
    False
    >>> iscrossing('DESERT-TEAL-LIVID', 'SIT-EVW-ADC-KLR')
    True
    >>> iscrossing('RUFOUS-SKOBELOFF', 'FL-XUM-SKE-BOR')
    False
    >>> iscrossing('DENIM-OPAL-MANDARIN', 'NMO-AI-LDR-EYP')
    True
    >>> iscrossing('BONE-SEPIA-BROWN', 'ODI-VAR-BEP-SNW')
    False
    '''


    split_solution = solution.split('-')

    for word in split_solution:
        for i in range(len(word)-1):
            if side(word[i], puzzle) == side(word[i+1], puzzle):
                return False
    return True


def issolution(solution, puzzle):
    '''
    >>> issolution('MYSTIC-CORAL-LIVER', 'YOI-RCM-VSA-LTE')
    True
    >>> issolution('DENIM-MAIZE-EGGPLANT', 'GND-IET-MZL-AP')
    False
    >>> issolution('GAINSBORO-ONYX-PEAR', 'BGY-NXE-PAO-SRI')
    False
    >>> issolution('KOBI-PLATINUM-ZOMP', 'TML-OZB-IUK-APN')
    False
    >>> issolution('DESERT-TEAL-LIVID', 'SIT-EVW-ADC-KLR')
    False
    >>> issolution('RUFOUS-SKOBELOFF', 'FL-XUM-SKE-BOR')
    False
    >>> issolution('DENIM-OPAL-MANDARIN', 'NMO-AI-LDR-EYP')
    False
    >>> issolution('BONE-SEPIA-BROWN', 'ODI-VAR-BEP-SNW')
    False
    '''
    return iscrossing(solution, puzzle) and isconsecutive(solution) and iscomplete(solution , puzzle)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
