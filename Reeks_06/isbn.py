# https://dodona.be/nl/courses/4157/series/46295/activities/1316294687

def isISBN(code : str):
    '''
    >>> isISBN('9-9715-0210-0')
    True
    >>> isISBN('997-150-210-0')
    False
    >>> isISBN('9-9715-0210-8')
    False
    '''

    code_list = code.split('-')

    if len(code_list[0]) > 1 or len(code_list[-1]) > 1 or len(code_list) != 4:
        return False
    else:
        fcode = code.replace('-','')
        try:
            x10 = sum([int(fcode[i]) * (i + 1) for i in range(len(fcode) - 1)]) % 11
            x10t = 10 if fcode[9] == 'X' else int(fcode[9])
            return (x10 == x10t)
        except:
            return False


if __name__ == '__main__':
    import doctest

    doctest.testmod()