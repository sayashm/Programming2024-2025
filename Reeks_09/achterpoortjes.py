# https://dodona.be/nl/courses/4157/series/46298/activities/286850454

def reverse(sentence:str):
    '''
    >>> reverse('God bless our brave Confederates, Lord!')
    'Dro lseta red efnoc Evarbruossel, Bdog!'
    >>> reverse('Dro lseta red efnoc Evarbruossel, Bdog!')
    'God bless our brave Confederates, Lord!'
    >>> reverse('Lee, Johnson, Smith, and Beauregard!')
    'Dra, Geruaeb, Dnaht, ims Nosnhojeel!'
    >>> reverse('Help Jackson, Smith, and Johnson Joe,')
    'Eojn Osnhojd, Nahti, msn Oskcajp Leh,'
    >>> reverse('To give them fits in Dixie, oh!')
    'Ho eixi dnis tifm eh Tevig, ot!'
    '''
    from string import punctuation
    punc = punctuation+' '

    res = [None] * len(sentence)

    for ind, l in enumerate(sentence):
        if l in punc:
            res[ind] = l

    index = len(sentence) - 1
    for l in sentence:
        if l not in punc:
            while res[index] is not None:
                index -= 1

            res[index] = l.lower() if sentence[index].islower() else l.upper()


    return ''.join(res)


def codec(location:str, saveto:str = None):
    '''
    >>> codec('plaintext.txt')
    Dro lseta red efnoc Evarbruossel, Bdog!
    Dra, Geruaeb, Dnaht, ims Nosnhojeel!
    Eojn Osnhojd, Nahti, msn Oskcajp Leh,
    Ho eixi dnis tifm eh Tevig, ot!
    >>> codec('plaintext.txt', 'ciphertext.txt')
    >>> codec('ciphertext.txt')
    God bless our brave Confederates, Lord!
    Lee, Johnson, Smith, and Beauregard!
    Help Jackson, Smith, and Johnson Joe,
    To give them fits in Dixie, oh!
    >>> codec('ciphertext.txt', 'plaintext2.txt')
    '''

    reader = open(location, 'r')
    lines = reader.readlines()
    text = [reverse(line.rstrip()) for line in lines]

    if saveto is None:
        for line in text:
            print(line)
    else:
        writer = open(saveto, 'w')
        for line in text:
            print(line, file = writer)
        writer.close()

    reader.close()

def filecomp(location1:str, location2:str)->bool:
    '''
    >>> filecomp('plaintext.txt', 'ciphertext.txt')
    False
    >>> filecomp('plaintext.txt', 'plaintext2.txt')
    True
    '''
    reader1 = open(location1, 'r')
    reader2 = open(location2, 'r')
    lines1 = reader1.readlines()
    lines2 = reader2.readlines()
    text1 = [reverse(line.rstrip()) for line in lines1]
    text2 = [reverse(line.rstrip()) for line in lines2]

    return text1 == text2
