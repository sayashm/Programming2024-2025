# https://dodona.be/nl/courses/4157/series/46297/activities/1942875591
from operator import itruediv


def ispolygon(*args :list|tuple)->bool:
    '''
    >>> ispolygon(['DISEASES', 'RENUMBER', 'SOCIABLE'])
    True
    >>> ispolygon('FREELOADS, TIMEPIECE, NORMALIZE')
    False
    >>> ispolygon({'CONSULTANT', 'CAPITALIZE', 'KETTLEDRUM', 'SUBSECTION', 'LOOKALIKES'})
    False
    >>> ispolygon(('JAWBREAKERS', 2.833, 'CONSEQUENCE', 'FRIGHTFULLY', 'UNWILLINGLY'))
    False
    '''

    iterable = args[0] if isinstance(args[0], (list, tuple)) and len(args) == 1 else args
    if len(iterable) < 3:
        return False
    elif not all([isinstance(word, str) for word in iterable]):
        return False
    elif not all([word.isupper() for word in iterable]):
        return False
    elif len(set(len(word) for word in iterable)) != 1:
        return False
    elif any([letter.isdigit() for word in iterable for letter in word]):
        return False
    return True

def solution(puzzle, clockwise:bool = True, start:int = 0)-> str:
    '''
    >>> solution(['DISEASES', 'RENUMBER', 'SOCIABLE'])
    'DECEMBER'
    >>> solution(('FREELOADS', 'TIMEPIECE', 'NORMALIZE'))
    'FIREPLACE'
    >>> solution(['PERFORMER', 'ANTIVIRAL', 'CROSSBOWS', 'PHENOTYPE'], start=2)
    'CHRISTMAS'
    >>> solution(('KETTLEDRUM', 'CONSULTANT', 'CAPITALIZE', 'SUBSECTION', 'LOOKALIKES'), clockwise=False, start=3)
    'SANTACLAUS'
    >>> solution(('HOSIERY', 'ILLEGAL', 'BOULDER'), clockwise=False)
    'HOLIDAY'
    >>> solution(['ARTILLERY', 'HEXAGONAL', 'COMMANDER', 'BIOLOGIST', 'EXTENSION'], clockwise=False, start=3)
    'BOXINGDAY'
    >>> solution(('SUPERSONIC', 'MINUSCULES', 'INTEGRATOR', 'SALMONELLA'), clockwise=False)
    'SATURNALIA'
    >>> solution(('APPENDECTOMY', 'RECUPERATION', 'CONSTRICTION', 'INCONCLUSIVE'), clockwise=False)
    'ANNUNCIATION'
    '''
    lp = len(puzzle)
    lw = len(puzzle[0])
    a = 1 if clockwise else -1

    return ''.join([puzzle[(a*i+start)%lp][i] for i in range(lw)])


def solutions(puzzle, clockwise:bool = None)-> set:
    '''
    >>> solutions(['DISEASES', 'RENUMBER', 'SOCIABLE'])
    {'DECEMBER', 'DONEABEE', 'RICUABES', 'ROSUASEE', 'SESIMSLR', 'SINIABLS'}
    >>> solutions(['FREELOADS', 'TIMEPIECE', 'NORMALIZE'], clockwise=True)
    {'FIREPLACE', 'NRMMLIIDE', 'TOEEAOEZS'}
    >>> solutions(['PERFORMER', 'ANTIVIRAL', 'CROSSBOWS', 'PHENOTYPE'], clockwise=True)
    {'AREFVBYEL', 'CHRISTMAS', 'PETSORRWE', 'PNONOIOPR'}
    >>> solutions(['KETTLEDRUM', 'CONSULTANT', 'CAPITALIZE', 'SUBSECTION', 'LOOKALIKES'], clockwise=False)
    {'CEOSTLDKOE', 'COTKEATREN', 'KOBIUEIIZT', 'LUPSLLTINM', 'SANTACLAUS'}
    '''
    l = len(puzzle)
    if not ispolygon(puzzle):
        raise AssertionError('invalid polygon')

    return {solution(puzzle, c , s) for s in range(l) for c in [True, False]} if clockwise == None else {solution(puzzle,clockwise, i) for i in range(l)}
