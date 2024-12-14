# https://dodona.be/en/courses/2802/series/29677/activities/570316391/

def read_key(location:str):
    with open(location, 'r', encoding='utf-8') as reader:
        lines = reader.readlines()

    return {line.rstrip().split('\t')[0]:(int(line.rstrip().split('\t')[1]),int(line.rstrip().split('\t')[2])) for line in lines}

def symbols2digits(sentence:str, key:dict, swap:bool=False)->str:
    if swap:
        return ''.join([ str(key[l][1]) + str(key[l][0]) for l in sentence])
    return ''.join([ str(key[l][0]) + str(key[l][1]) for l in sentence])


def make_grid(key:dict)->dict:
    res = {i:[None]*9 for i in range(1,10)}
    for k in key:
        res[key[k][0]][key[k][1]-1] = k
    for k in res:
        res[k] = ''.join(res[k])

    return res

def digits2symbols(sequence:str, key:dict, swap:bool=False)->str:
    len_digit = int(len(sequence) / 2)
    if swap:

        return ''.join(key[int(i[1])][int(i[0])-1] for i in [sequence[(2 * i): (2 * i) + 2] for i in range(len_digit)])
    return ''.join(key[int(i[0])][int(i[1])-1] for i in [sequence[(2 * i): (2 * i) + 2] for i in range(len_digit)])


def encode(plaintext:str, key:dict)->str:
    return digits2symbols(symbols2digits(plaintext,key, True),make_grid(key))

def decode(plaintext:str, key:dict)->str:
    return digits2symbols(symbols2digits(plaintext,key, ),make_grid(key),True)


def main_test():
    '''
    >>> key = read_key('valknut.txt')
    >>> key['W']
    (2, 6)
    >>> key['h']
    (3, 8)
    >>> key[' ']
    (6, 8)
    >>> key['.']
    (2, 7)

    >>> symbols2digits("Where wolf's ears are, wolf's teeth are near.", key)
    '263863356368227752646124686325352468253563876822775264612468326363323868253563689463253527'
    >>> symbols2digits("Where wolf's ears are, wolf's teeth are near.", key, swap=True)
    '628336533686227725461642863652534286525336788622772546164286233636238386525336864936525372'

    >>> grid = make_grid(key)
    >>> grid
    {1: 'mZkqUpMKE', 2: 'BwRsaW.DQ', 3: '|tVCr7Th"', 4: 'yG%_u#L(&', 5: '3lXHIcOPi', 6: "'-efY9$ 2", 7: 'jS80@zo:b', 8: ')g;N54,xd', 9: 'J1Fn?Av6!'}

    >>> digits2symbols('263863356368227752646124686325352468253563876822775264612468326363323868253563689463253527', grid)
    "Where wolf's ears are, wolf's teeth are near."
    >>> digits2symbols('628336533686227725461642863652534286525336788622772546164286233636238386525336864936525372', grid, swap=True)
    "Where wolf's ears are, wolf's teeth are near."

    >>> encode("Where wolf's ears are, wolf's teeth are near.", key)
    '-;7X74woa#pG47lXG4lX7:4woa#pG4R77R;4lX74&7lXS'

    >>> decode('-;7X74woa#pG47lXG4lX7:4woa#pG4R77R;4lX74&7lXS', key)
    "Where wolf's ears are, wolf's teeth are near."
    '''


if __name__ == '__main__':
    import doctest
    doctest.testmod()

