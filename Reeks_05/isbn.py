# https://dodona.be/nl/courses/4157/series/46291/activities/620641000
def isISBN(code):

    """
    Geeft True terug als het argument een string is die een geldige ISBN-10 code
    bevat. Anders wordt False teruggegeven.

    >>> isISBN('9971502100')
    True
    >>> isISBN('9971502108')
    False
    >>> isISBN('53WKEFF2C')
    False
    >>> isISBN(4378580136)
    False
    """
    try:
        x10 = sum([int(code[i]) * (i + 1) for i in range(len(code) - 1)]) % 11
        x10t = 10 if code[9] == 'X' else int(code[9])
        if x10 == x10t:
                return (True)
        else:
                return(False)
    except:
        return(False)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
