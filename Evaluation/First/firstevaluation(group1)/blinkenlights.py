# https://dodona.be/nl/courses/4157/series/46292/activities/1482478081

def digit_count(key:str)->int:
    return len([ch for ch in key if ch.isdigit()])

def digit_position(digit:int, integer:int, key:str)->int:
    occurs = [(pos, ch) for pos, ch in enumerate(key) if ch.isdigit() if int(ch)==digit ]

    return occurs[integer-1][0] if len(occurs) >= integer else -1

def decrypt(ciphertext:str, key:str):
    res = ''
    for i in range(1, digit_count(key)):
        for j in range(10):
            if digit_position(j, i, key) != -1:
                res += ciphertext[digit_position(j, i, key)]

    return res


def main_test():
    '''
    >>> ciphertext = '28 ZsTpaumnrhsrkotDscf nameggi cit rhi reenfeie  tüd enomntpeikadrtnenbu !g'
    >>> key = 'e = 2.718281828459045235360287471352662497757247093699959574966967627724076'

    >>> digit_count(key)
    70

    >>> digit_position(3, 2, key)
    24
    >>> digit_position(6, 3, key)
    37
    >>> digit_position(9, 42, key)
    -1

    >>> decrypt(ciphertext, key)
    'Das komputermaschine ist nicht für der gefingerpoken und mittengraben!'

    >>> ciphertext = ' ftLsrnUisyTelvWya les   Kahen  Eu9ocr RRll 5ochyV.!s ynle5ITiRta'
    >>> key = '6630295(160n897o0338533q1=884868J7Z624$fJ035W3375E13016898B4X9.74'
    >>> decrypt(ciphertext, key)
    'Listen very carefully. I shall say this only once!'
    '''


if __name__ == "__main__":
    import doctest
    doctest.testmod()
