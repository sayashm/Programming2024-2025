# https://dodona.be/nl/courses/4157/series/46293/activities/381503733

def mirror_number(number : int)->int:
    '''
    >>> mirror_number(7847)
    7487
    >>> mirror_number(37865)
    56873
    '''
    return int(''.join(list(str(number))[::-1]))


def reduction(number:int, position:int)->int:
    '''
    >>> reduction(27847, 0)
    7847
    >>> reduction(27847, 1)
    2847
    >>> reduction(27847, 2)
    2747
    '''
    return int(str(number)[:position]+str(number)[position+1:])


def numerator(number : int)->int:
    '''
    >>> numerator(27847)
    54197
    >>> numerator(937865)
    865739
    '''
    len_num_string = len(str(number))
    return sum([sum([reduction(number, i), mirror_number(reduction(number, i))]) for i in range(len_num_string)])


def denominator(number):
    '''
    >>> denominator(27847)
    28
    >>> denominator(937865)
    38
    '''
    return sum([int(i) for i in list(str(number))])


def catch(number:int)->float:
    '''
    >>> catch(27847)
    1935.607142857143
    >>> catch(937865)
    22782.605263157893
    '''

    return numerator(number)/denominator(number)