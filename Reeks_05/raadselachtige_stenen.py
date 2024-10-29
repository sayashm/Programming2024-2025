# https://dodona.be/nl/courses/4157/series/46291/activities/247416777

def digit_sum(num):
    '''
    >>> digit_sum(987654321)
    45
    >>> digit_sum(123456789)
    45
    >>> digit_sum(864197532)
    45
    '''

    return sum(int(i) for i in str(num))

def issolution(i , j):
    '''
    >>> issolution(987654321, 123456789)
    True
    >>> issolution(93243, 58134)
    False
    '''
    return digit_sum(i) == digit_sum(j) == digit_sum(i-j)

def solutions(a, b):
    '''
    >>> solutions(1000, 2000)
    1311
    >>> solutions(2000, 3000)
    1202
    >>> solutions(3000, 4000)
    1128
    '''
    pass
    count = 0
    for i in range(a + 1, b + 1):
        for j in range(a, i):
            if issolution(i, j):
                count += 1
    return count