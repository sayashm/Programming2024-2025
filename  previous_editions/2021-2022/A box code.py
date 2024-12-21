# https://dodona.be/en/courses/773/series/10808/activities/1540405843/
import random
from string import punctuation

def read_box_code (location:str)->dict:

    with open(location, 'r', encoding='utf-8') as reader:
        lines = reader.readlines()

    lines = [line.rstrip().split(' ') for line in lines]

    res ={}
    for digit , ch in lines:
        if digit in res:
            res[digit].add(''.join(sorted(ch)))
        else:
            res[digit] = {''.join(sorted(ch))}

    return res


def letter2code(letter: str, code:dict):
    num = ord(letter.upper())-64
    if num > 9:
        res = []
        for digit in list(str(num)):
            l = list(code[digit])
            res.append(random.choice(l))

        return '-'.join(res)
    l_code = code[str(num)]
    return random.choice(list(l_code))


def code2letter(letter:str, code:dict)->str:
    letters = letter.split('-')
    sort_letter = []
    for l in letters:
        sort_letter.append(''.join(sorted(l)))

    if len(sort_letter) > 1:
        num = ''
        for l in sort_letter:
            num += ''.join([i for i in code if l in code[i]][0])
    else:
        num = [i for i in code if sort_letter[0] in code[i]][0]


    return chr(int(num)+64)




def encode(sentence:str, code:dict)->dict:
    punc = punctuation + ' '
    res = ''
    for letter in sentence:
        if letter not in punc:
            res += letter2code(letter, code)+' '


    return res.rstrip()


def decode(sentence:str, code:dict)->str:
    list_sentence = sentence.split(' ')

    return ''.join(code2letter(c,code) for c in list_sentence)



def main_test():
    '''
    >>> box_code = read_box_code('code.txt')
    >>> box_code['0'] == {'deh'}
    True
    >>> box_code['1'] == {'b', 'd'}
    True

    >>> box_code['9'] == {'abef', 'aefh'}
    True

    >>> letter2code('H', box_code)
    'fecgha'
    >>> letter2code('x', box_code)
    'hfac-bfg'

    >>> code2letter('fecgha', box_code)
    'H'
    >>> code2letter('hfac-bfg', box_code)
    'X'

    >>> encode('And now for something completely different!', box_code)
    'b b-bgf fbg d-bfg b-hae afhc-fagc bhgc b-eha b-hfceag d-feha d-hae b-agfc hae afhc-edh ghecfa fahe d-fgb ab gcaf b-aeh d-gfca d-gcbh d-chfa eah cahf-hed eah d-acfh hfac-hea fbg fbea ghcb chgb eha b-cahfeg hae b-bgf hcfa-hed'
    >>> encode('And now for something completely different!', box_code)
    'd d-bgf bgf d-fgb d-hea ahcf-cfag cgfh d-ahe d-cgfeha b-fbae b-aeh b-fgac ahe afhc-ehd afghec fhea b-bfg ba cagf b-ahe d-cagf b-hgbc b-chfa aeh afhc-hde hae d-chaf cahf-hea fgb ehaf cgbh chgb hae b-aefcgh aeh d-bfg fach-hed'

    >>> decode('b b-bgf fbg d-bfg b-hae afhc-fagc bhgc b-eha b-hfceag d-feha d-hae b-agfc hae afhc-edh ghecfa fahe d-fgb ab gcaf b-aeh d-gfca d-gcbh d-chfa eah cahf-hed eah d-acfh hfac-hea fbg fbea ghcb chgb eha b-cahfeg hae b-bgf hcfa-hed', box_code)
    'ANDNOWFORSOMETHINGCOMPLETELYDIFFERENT'
    >>> decode('d d-bgf bgf d-fgb d-hea ahcf-cfag cgfh d-ahe d-cgfeha b-fbae b-aeh b-fgac ahe afhc-ehd afghec fhea b-bfg ba cagf b-ahe d-cagf b-hgbc b-chfa aeh afhc-hde hae d-chaf cahf-hea fgb ehaf cgbh chgb hae b-aefcgh aeh d-bfg fach-hed', box_code)
    'ANDNOWFORSOMETHINGCOMPLETELYDIFFERENT'
    '''



if __name__ == '__main__':
    import doctest

    doctest.testmod()