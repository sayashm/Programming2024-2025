# https://dodona.be/en/courses/773/series/10808/activities/730046655/
from fractions import Fraction

def word_fraction(word:str, frac:Fraction)->str:
    if len(word)%frac.denominator == 0:
        return word[:int(frac*len(word))] if frac > 0  else word[int(frac*len(word)):]
    raise AssertionError('invalid fraction')

def combine(words:list, fracs:list)->str:
    return ''.join(word_fraction(word, frac) for word , frac in zip(words,fracs))


def decompose(question:str)->tuple:
    question = question.replace('What is ', '').replace('?','').replace(' and ', ', ')
    frac_wordstr = question.split(', ')

    return ([string.split(' ')[1] for string in frac_wordstr],
            [Fraction(string.split(' ')[0]) for string in frac_wordstr])

def answer(question:str)->str:
    return combine(decompose(question)[0],decompose(question)[1])





def main_test():
    '''
    >>> word_fraction('wallaby', Fraction(4, 7))
    'wall'
    >>> word_fraction('parakeet', Fraction(2, 8))
    'pa'
    >>> word_fraction('perch', Fraction(3, 5))
    'per'

    >>> word_fraction('ALPACA', Fraction(-1, 3))
    'CA'
    >>> word_fraction('PARTRIDGE', Fraction(-7, 9))
    'RTRIDGE'

    >>> word_fraction('manatee', Fraction(1, 2))
    Traceback (most recent call last):
    AssertionError: invalid fraction

    >>> combine(['wallaby', 'parakeet', 'perch'], [Fraction(4, 7), Fraction(1, 4), Fraction(3, 5)])
    'wallpaper'
    >>> combine(['ALPACA', 'PARTRIDGE'], [Fraction(-1, 3), Fraction(-7, 9)])
    'CARTRIDGE'
    >>> combine(['Manatee', 'cheetah', 'hamster'], [Fraction(3, 7), Fraction(3, 7), Fraction(-4, 7)])
    'Manchester'

    >>> decompose('What is 4/7 wallaby, 1/4 parakeet and 3/5 perch?')
    (['wallaby', 'parakeet', 'perch'], [Fraction(4, 7), Fraction(1, 4), Fraction(3, 5)])
    >>> decompose('What is -1/3 ALPACA and -7/9 PARTRIDGE?')
    (['ALPACA', 'PARTRIDGE'], [Fraction(-1, 3), Fraction(-7, 9)])
    >>> decompose('What is 3/7 Manatee, 3/7 cheetah and -4/7 hamster?')
    (['Manatee', 'cheetah', 'hamster'], [Fraction(3, 7), Fraction(3, 7), Fraction(-4, 7)])

    >>> answer('What is 4/7 wallaby, 1/4 parakeet and 3/5 perch?')
    'wallpaper'
    >>> answer('What is -1/3 ALPACA and -7/9 PARTRIDGE?')
    'CARTRIDGE'
    >>> answer('What is 3/7 Manatee, 3/7 cheetah and -4/7 hamster?')
    'Manchester'
    '''

if __name__ == '__main__':
    import doctest
    doctest.testmod()