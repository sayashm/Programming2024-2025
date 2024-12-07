# https://dodona.be/nl/courses/4157/series/46298/activities/1865922943

def read_key(location: str)->dict:
    reader = open(location, 'r')
    lines = reader.readlines()
    return {line.rstrip()[:1]: line.rstrip()[2:] for line in lines}


def symbols2bits(message:str, key:dict)->str:
    return ''.join(key[l] for l in message)

def bits2symbols(bitstring:str, key:dict)->str:
    res = []
    while bitstring:
        for k, v in key.items():
            match = None
            if bitstring.startswith(v):
                match = k
                res.append(match)
                bitstring = bitstring[len(v):]
                break

    return ''.join(res)


def flip(bitstring:str)->str:

    return ''.join(['0' if i == '1' else '1' for i in bitstring ])


def issymmetric(representation:dict)->bool:

    return set(representation.values()) == {flip(i) for i in representation.values()}


def encode(message:str, representation:dict)->str:
    if not issymmetric(representation):
        raise AssertionError('asymmetric key')

    return ''.join([bits2symbols(flip(symbols2bits(i, representation)), representation) for i in message])

def decode(message:str, representation:dict)->str:
    return encode(message, representation)

def main_tests():
    """
    >>> key = read_key('key.01.txt')
    >>> key['A']
    '10'
    >>> key['R']
    '010'
    >>> key['C']
    '1100'
    >>> symbols2bits('ABRACADABRA', key)
    '1000010101100101101100001010'
    >>> bits2symbols('1000010101100101101100001010', key)
    'ABRACADABRA'
    >>> flip('1000010101100101101100001010')
    '0111101010011010010011110101'
    >>> issymmetric(key)
    False
    >>> encode('ABRACADABRA', key)
    Traceback (most recent call last):
    AssertionError: asymmetric key

    >>> key = read_key('key.02.txt')
    >>> key['G']
    '100101'
    >>> key['e']
    '110'
    >>> key[' ']
    '010'
    >>> key['.']
    '1001000010'
    >>> symbols2bits('Get me off your fucking mailing list.', key)
    '1001011100000101111100101000001001010011011010000111100100101000101110110111010010001101011001001101011101101111110101101010101100100110100110101011001000000001001000010'
    >>> bits2symbols('1001011100000101111100101000001001010011011010000111100100101000101110110111010010001101011001001101011101101111110101101010101100100110100110101011001000000001001000010', key)
    'Get me off your fucking mailing list.'
    >>> flip('1001011100000101111100101000001001010011011010000111100100101000101110110111010010001101011001001101011101101111110101101010101100100110100110101011001000000001001000010')
    '0110100011111010000011010111110110101100100101111000011011010111010001001000101101110010100110110010100010010000001010010101010011011001011001010100110111111110110111101'
    >>> issymmetric(key)
    True
    >>> encode('Get me off your fucking mailing list.', key)
    'lfmitfiueeiruoyieokc gnits G gniG amT'
    >>> decode('lfmitfiueeiruoyieokc gnits G gniG amT', key)
    'Get me off your fucking mailing list.'
    """
    pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()
