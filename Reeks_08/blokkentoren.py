# https://dodona.be/nl/courses/4157/series/46297/activities/1813287079



def letters(name: str) -> list:
    '''
    >>> letters('ALUMINIUM')
    ['A', 'I', 'L', 'M', 'N', 'U']
    '''
    from string import punctuation

    punc = punctuation + ' '
    return sorted([i for i in list(set(name.upper())) if (i not in punc and not i.isdigit())])


def fragments(name:str) -> list:
    '''
    >>> fragments('ALUMINIUM')
    ['A', 'BCDEFGHI', 'JKL', 'M', 'N', 'OPQRSTU', 'VWXYZ']
    '''
    from string import ascii_uppercase as upper

    letter = letters(name)
    pos = [upper.find(i)+1 for i in letter]
    pos.append(len(upper)) if letter[-1] != upper[-1] else pos
    pos.insert(0, 0)
    steps =[(pos[i], pos[i + 1]) for i in range(len(pos) - 1)]
    return [upper[i:j] for i, j in steps]


def block_tower(word:str)-> tuple:
    '''
    >>> tower = block_tower('ALUMINIUM')
    >>> tower
    ('A', 'M', 'N', 'JKL', 'VWXYZ', 'OPQRSTU', 'BCDEFGHI')
    '''

    return tuple(sorted(fragments(word), key = len))

def row_lengths(tower:tuple)->tuple:
    '''
    >>> tower = block_tower('ALUMINIUM')
    >>> tower
    ('A', 'M', 'N', 'JKL', 'VWXYZ', 'OPQRSTU', 'BCDEFGHI')
    >>> row_lengths(tower)
    (1, 1, 1, 3, 5, 7, 8)
    '''
    return tuple(len(i) for i in tower)

def vowel_positions(tower:tuple)->set:
    '''
    >>> tower = block_tower('ALUMINIUM')
    >>> tower
    ('A', 'M', 'N', 'JKL', 'VWXYZ', 'OPQRSTU', 'BCDEFGHI')
    >>> vowel_positions(tower)
    {(0, 0), (6, 7), (5, 6), (6, 3), (5, 0)}
    '''
    vowels = ['A', 'E', 'I', 'O', 'U']
    l = len(tower)

    return {(i,tower[i].find(j)) for i in range(l) for j in vowels if tower[i].find(j)!=-1}