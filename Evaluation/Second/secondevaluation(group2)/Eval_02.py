# https://dodona.be/en/courses/4157/series/52181/activities/1011050277/

def decode(location:str, light = ' ', dark:str = '#'):
    with open(location, 'r', encoding='utf-8') as reader:
        lines = reader.readlines()
    # read each line and split it by light
    lines = [line.strip(light+'\n').split(light) for line in lines]
    # use chr() function to take number of letter in alphabets
    return ''.join([chr(len(code)+64) for line in lines for code in line])


def encode_group(letters:str, dark:str = '#', light:str = ' ')->str:
    # change every char to upper case and use decode() function to covert every thing to the dark and light
    return light.join([dark * (ord(letter.upper())- 64) for letter in letters])

def encode_groups(groups:str, dark:str = '#', light:str = ' ')->list:
    # use every char in each group to give to encode_group finction to take the list of codes
    groups = [ch.upper() for ch in groups.split(' ') if len(ch)>0]
    return [encode_group(group, dark, light) for group in groups]


def supplement(string: str, width:int=None, character:str=' ')->str:
    # if we don't define width so it can return string
    if width is not None:
        # if the length of final string be even:
        if (width - len(string)) % 2 == 0:
            l = (width - len(string)) // 2
            return l * character + string + l * character
        # if the length of final string be odd:
        l1 = (width - len(string)) // 2
        l2 = ((width - len(string)) // 2)+1
        return l1 * character + string + l2 * character

    return string

def encode(plaintext:str, dark:str = '#', light:str = ' ', file:str = None)->str:
    # use encode_groups function to convert to code each group
    encodeGroups = encode_groups(plaintext,dark,light)
    # define the maxuimum length of groups to now how where we should continue each line
    maxL = len(max(encodeGroups, key=len))
    # use supplement function to write each line
    if file is None:
        for group in encodeGroups:
            print(supplement(group, width=maxL, character=light))

    # write file if we have the file location:
    else:
        with open(file, 'w', encoding='utf-8') as writer:
                for group in encodeGroups:
                    writer.write(supplement(group, width=maxL, character=light))
                    writer.write('\n')

def main_test():
    '''
    >>> decode('butterfly.01.txt', light='-')
    'TROGONOPTERABROOKIANA'
    >>> decode('butterfly.02.txt', dark='X', light='_')
    'ACHERONTIAATROPOS'

    >>> encode_group('A')
    '#'
    >>> encode_group('BC', dark='X')
    'XX XXX'
    >>> encode_group('DEF', dark='@', light='_')
    '@@@@_@@@@@_@@@@@@'
    >>> encode_group('GHIJ', light='1', dark='8')
    '8888888188888888188888888818888888888'

    >>> encode_groups('A BC')
    ['#', '## ###']
    >>> encode_groups('DEF GHIJ', dark='X')
    ['XXXX XXXXX XXXXXX', 'XXXXXXX XXXXXXXX XXXXXXXXX XXXXXXXXXX']
    >>> encode_groups(' a  bc   def    ', dark='@', light='_')
    ['@', '@@_@@@', '@@@@_@@@@@_@@@@@@']

    >>> supplement('spam')
    'spam'
    >>> supplement('eggs', width=10)
    '   eggs   '
    >>> supplement('bacon', width=10, character='_')
    '__bacon___'

    >>> encode('AAAAAA BBBB CCC')
    # # # # # #
    ## ## ## ##
    ### ### ###
    >>> encode('  aaa  bbb  ccc  ', light='_')
    ___#_#_#___
    _##_##_##__
    ###_###_###
    >>> encode('GH IJK LM', dark='@', light='-')
    --------@@@@@@@-@@@@@@@@--------
    @@@@@@@@@-@@@@@@@@@@-@@@@@@@@@@@
    ---@@@@@@@@@@@@-@@@@@@@@@@@@@---
    >>> encode('T r ogo nop ter a b r oo k i ana', light='-')
    -------------####################--------------
    --------------##################---------------
    ----###############-#######-###############----
    ##############-###############-################
    -####################-#####-##################-
    -----------------------#-----------------------
    ----------------------##-----------------------
    --------------##################---------------
    --------###############-###############--------
    ------------------###########------------------
    -------------------#########-------------------
    --------------#-##############-#---------------
    >>> encode('Ac h e ro nt i aa tr op o s', dark='X', light='_', file='ciphertext.02.txt')

    '''


if __name__ == '__main__':
    import doctest

    doctest.testmod()