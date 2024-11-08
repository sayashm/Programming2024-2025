# https://dodona.be/en/courses/1659/series/18379/activities/423431787/
from difflib import SequenceMatcher


def forward_sequence(words:str):
    '''
    >>> forward_sequence('Space, Cinema, Ester, Abaci, Cabaret, Seamen')
    'spacecinemaesterabacicabaretseamen'
    '''

    # replace ' ' and ',' between words. return lowercase of all string
    return words.replace(',','').replace(' ','').lower()

def backward_sequence(words:str):
    '''
    >>> backward_sequence('Space, Cinema, Ester, Abaci, Cabaret, Seamen')
    'nemaesterabacicabaretseamenicecaps'
    '''

    # use forward_sequence function to take the string
    forward_string = forward_sequence(words)

    # reverse the forward sring
    return forward_string[::-1]

def common_sequence(words:str):
    '''
    >>> common_sequence('Space, Cinema, Ester, Abaci, Cabaret, Seamen')
    'nemaesterabacicabaretseamen'
    '''

    # Make forward_sequence and backward_sequence

    backwardSequence = backward_sequence(words)
    forwardsequence = forward_sequence(words)

    #find common part of two strings
    match = SequenceMatcher(None, backwardSequence, forwardsequence).find_longest_match()
    common = backwardSequence[match.a: match.size]

    return(common)

def missing_word(words:str):
    '''
    >>> missing_word('Space, Cinema, Ester, Abaci, Cabaret, Seamen')
    'Icecaps'
    '''

    # Make forward_sequence and backward_sequence
    backwardSequence = backward_sequence(words)
    forwardsequence = forward_sequence(words)

    # find missing part:
    match = SequenceMatcher(None, backwardSequence, forwardsequence).find_longest_match()
    common = backwardSequence[match.size:].capitalize()
    return common





