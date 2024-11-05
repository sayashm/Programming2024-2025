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
        if i not in w2:
            return False
    return True



def isspellable():
    pass

def solutions():
    pass

def pangrams():
    pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()
