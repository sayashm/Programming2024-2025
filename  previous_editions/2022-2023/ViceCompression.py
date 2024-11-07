# https://dodona.be/en/courses/1659/series/18381/activities/338479462/

import string
import re

def censored(word: str):
    '''
    >>> censored('narcotics')
    'n9'
    >>> censored('RELATIONSHIPS')
    'R13'
    '''

    return f'{word[0]}{len(word)}'

def revealed(word:str):
    '''
    >>> revealed('n9')
    'n????????'
    >>> revealed('R13')
    'R????????????'
    '''

    return f'{word[0]}{"?" * (int(word[1:])-1)}'


def flatten_list(nested_list):
    flattened = []
    for item in nested_list:
        if isinstance(item, list):
            flattened.extend(item)  # Flatten the sublist
        else:
            flattened.append(item)  # Append non-list items directly
    return flattened

def remover(sent:str):

    words = [word.strip(string.punctuation) if word != '--' else word for word in sent.split(' ') ];
    for i in range(len(words)):
        if "'" in words[i]  :
            words[i] = words[i].split("'")
        elif '-' in words[i] and words[i] != '--':
            words[i] = words[i].split("-")
        else:
            words[i] = words[i]
    words = flatten_list(words)
    return words

def censor(sent : str):
    '''

    >>> censor("He's not the Messiah -- he's a very naughty boy.")
    "H2's1 n3 t3 M7 -- h2's1 a1 v4 n7 b3."
    '''

    words = remover(sent)

    for word in words:
        if word != '--':
            sent = re.sub(fr'\b{word}\b', censored(word), sent)

    return (sent)


def reveal(sent:str):
    '''
    >>> reveal('M13 (i11 r13) w4 n3 a7.')
    'M???????????? (i?????????? r????????????) w??? n?? a??????.'
    >>> reveal('W5 l4 "G3," "L4," "J5," "C6," "h4," a3 "d4" c5 n3 b2 u4!')
    'W???? l??? "G??," "L???," "J????," "C?????," "h???," a?? "d???" c???? n?? b? u???!'
    >>> reveal('H6 f3 y4 o3-e4 t7 s5.')
    'H????? f?? y??? o??-e??? t?????? s????.'
    '''

    words = remover(sent)
    for word in words:
        if word != '--':
            sent = re.sub(fr'\b{word}\b', revealed(word), sent)
    return (sent)



