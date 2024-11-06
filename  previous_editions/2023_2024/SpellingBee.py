# https://dodona.be/en/courses/2802/series/29677/activities/831188340/

def isspellable(w1, w2):

    '''
        >>> isspellable('houseplant', 'oesHpln')
        False
        >>> isspellable('phone', 'oesHpln')
        True
        >>> isspellable('epsilon', 'oesHpln')
        False
        >>> isspellable('loophole', 'oesHpln')
        True
    '''

    for i in w1:
        if i.lower() not in w2.lower(): return False
    return True


def ispangram(w1, w2):
    '''
    >>> ispangram('helplessness', 'oesHpln')
    False
    >>> ispangram('hopelessness', 'oesHpln')
    True
    '''
    if isspellable(w1,w2):
        for i in w2:
            if i.lower() not in w1.lower(): return False
        return True
    else: return False


def solutions(location, p, minimum=4):
    '''
    >>> solutions('words.txt', 'oesHpln')
    {'hones', 'hellos', 'hopelessness', 'shone', 'hopes', 'shoon', 'hellholes', 'heels', 'nosh', 'shoos', 'hello', 'hoop', 'hell', 'loopholes', 'shells', 'hoes', 'loophole', 'noshes', 'hopeless', 'phones', 'sloshes', 'hens', 'shes', 'helplessness', 'holes', 'shell', 'hops', 'peepholes', 'hose', 'pooh', 'hope', 'posh', 'phone', 'hellhole', 'shleps', 'shlepps', 'shoe', 'shlep', 'shops', 'poohs', 'shop', 'shoes', 'slosh', 'sheep', 'hole', 'helpless', 'hoops', 'helps', 'hoses', 'help', 'shlepp', 'shoo', 'hone', 'peephole', 'sheen', 'heel'}
    >>> solutions('words.txt', 'oesHpln', minimum=10)
    {'hopelessness', 'helplessness'}
    >>> solutions('words.txt', 'ocgrNminas')     # two occurrences of letter N
    Traceback (most recent call last):
    AssertionError: invalid puzzle
    >>> solutions('words.txt', 'LpuomsietrgnC')  # two capitals
    Traceback (most recent call last):
    AssertionError: invalid puzzle
    '''

    # check duplicate
    def is_valid_puzzle(word):
        lower_count = len(set(word.lower()))
        uppercase_count = sum(map(str.isupper, word))
        return lower_count == len(word) and uppercase_count == 1

    # Raise an error if puzzle is invalid
    assert is_valid_puzzle(p), "invalid puzzle"

    mandatory_letter = next(filter(str.isupper, p))

    # open file:
    with open(location, 'r') as file:
        words = file.read().splitlines()

    res = set()
    for w in words:
        if (len(w) >= minimum and mandatory_letter.lower() in w.lower() and isspellable(w , p) ):
            res.add(w)
    return res



def pangrams(location, p):
    '''
    >>> pangrams('words.txt', 'oesHpln')
    {'hopelessness'}
    >>> pangrams('words.txt', 'ocgrNmias')
    {'microorganism', 'microorganisms'}
    >>> pangrams('words.txt', 'Lpuomsietrgnc')
    {'multiprocessing'}
    '''

    # check duplicate
    def is_valid_puzzle(word):
        lower_count = len(set(word.lower()))
        uppercase_count = sum(map(str.isupper, word))
        return lower_count == len(word) and uppercase_count == 1

    # Raise an error if puzzle is invalid
    assert is_valid_puzzle(p), "invalid puzzle"

    with open(location, 'r') as file:
        words = file.read().splitlines()

    result_set = set()
    for w in words:
        if (ispangram(w, p) and w in solutions(location, p)):
            result_set.add(w)

    return result_set



if __name__ == "__main__":
    import doctest
    doctest.testmod()
