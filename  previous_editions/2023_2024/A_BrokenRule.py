# https://dodona.be/en/courses/2802/series/29670/activities/1569380782/
from xmlrpc.client import boolean


def fill(w:str, bool:boolean):
    '''
    >>> fill('h??roglyphic', False)
    'hieroglyphic'
    >>> fill('inconc??vable', False)
    'inconceivable'
    >>> fill('fr??ndl??st', False)
    'friendliest'
    >>> fill('programmer', False)
    'programmer'
    >>> fill('alb??t', True)
    'albeit'
    >>> fill('z??tg??st', True)
    'zeitgeist'
    >>> fill('conc??rge', True)
    'concierge'
    >>> fill('glac??r', True)
    'glacier'
    '''
    # false ie true ei except after c

    if w[w.find('??')-1] == 'c':
        if bool:
            return w.replace('??','ie')
        else:
            return w.replace('??','ei')
    else:
        if bool:
            return w.replace('??','ei')
        else:
            return w.replace('??','ie')


def mask(w:str):
    '''
    >>> mask('hieroglyphic')
    'h??roglyphic'
    >>> mask('inconceivable')
    'inconc??vable'
    >>> mask('friendliest')
    'fr??ndl??st'
    >>> mask('programmer')
    'programmer'
    >>> mask('albeit')
    'alb??t'
    >>> mask('zeitgeist')
    'z??tg??st'
    >>> mask('concierge')
    'conc??rge'
    >>> mask('glacier')
    'glac??r'
    '''
    w = w.replace('ei','??')
    w = w.replace('ie','??')
    return w

def isexception(w: str):
    '''
    >>> isexception('hierarchy')
    False
    >>> isexception('ancient')
    True
    >>> isexception('ceiling')
    False
    >>> isexception('fahrenheit')
    True
    >>> isexception('daily')
    False
    >>> isexception('EiGHTietH')
    True
    >>> isexception('Expediencies')
    True
    >>> isexception('deities')
    True
    '''
    w = w.lower()

    # Check for "ei" exceptions (not after 'c')
    ei_positions = [i for i in range(len(w)) if w.startswith('ei', i)]
    for pos in ei_positions:
        if pos == 0 or w[pos - 1] != 'c':
            return True

    # Check for "ie" exceptions (after 'c')
    ie_positions = [i for i in range(len(w)) if w.startswith('ie', i)]
    for pos in ie_positions:
        if pos > 0 and w[pos - 1] == 'c':
            return True

    return False


def exceptions(sentence: str):
    '''
    >>> exceptions('I believe in the power of education.')
    0
    >>> exceptions('The ancient recipe requires a dash of weird ingredients.')
    2
    >>> exceptions('The society was fraught with a weird sense of hierarchy.')
    2
    >>> exceptions('The efficient machine processed the data with great speed.')
    1
    >>> exceptions('I before E except when your feisty foreign neighbor Keith leisurely receives eight counterfeit beige sleighs from weirdly caffeinated atheist weightlifters')
    13
    >>> exceptions('The eighty-eight-year-old weird heiress seized the beige sleigh from her feisty neighbor.')
    8
    >>> exceptions("Heigh-ho, heigh-ho, it's off to work we go. We need some sleigh'caffeine to keep us awake. We'll have a glass of madeira when we get back home. We're living in the zeitgeist of our times, heigh-ho, heigh-ho.")
    7
    '''

    words = sentence.split(' ')
    i = 0
    for word in words:
        if isexception(word):
            i += 1
    return(i)


if __name__ == "__main__":
    import doctest
    doctest.testmod()




