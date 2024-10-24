# https://dodona.be/nl/courses/4157/series/46291/activities/1266098554


def splitsing(soort):

    """
    Splitst de parameter (str) in een prefix en een suffix, waarbij de prefix
    bestaat uit alle medeklinkers aan het begin van de gegeven string.

    >>> splitsing('schaap')
    ('sch', 'aap')
    >>> splitsing('geit')
    ('g', 'eit')
    """
    word = soort.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    syllables = []
    pre = ''
    for i in range(len(word)):
        if word[i] not in vowels:
            pre = pre + word[i]
        else:
            suff = word[i:]
            break
    return((pre, suff))

def kruising(soort1, soort2):

    """
    Geeft tuple met twee strings terug, waarvan de eerste gevormd wordt door de
    samenstelling van de prefix van de eerste parameter (str) en de suffix van
    de tweede paramter (str), en de tweede gevormd wordt door de prefix van de
    tweede paramter en de suffix van de eerste paramter.

    >>> kruising('schaap', 'geit')
    ('scheit', 'gaap')
    >>> kruising('leeuw', 'tijger')
    ('lijger', 'teeuw')
    >>> kruising('hond', 'kat')
    ('hat', 'kond')
    """

    first_soord = splitsing(soort1)
    second_soord = splitsing(soort2)
    first_hybrid = first_soord[0]+second_soord[1]
    second_hybrid = second_soord[0]+first_soord[1]

    return((first_hybrid, second_hybrid))

if __name__ == '__main__':
    import doctest
    doctest.testmod()