# https://dodona.be/nl/courses/4157/series/46296/activities/1453551005


def encode_letter(c:str, p: str = None) -> str:
    '''
    >>> encode_letter('H')
    'H'
    >>> encode_letter('e', 'H')
    'l'
    >>> encode_letter('W', 'y')
    'U'
    '''
    if p is not None:
        c_upper = ord(c.upper()) - ord('A')
        p_upper = ord(p.upper()) - ord('A')
        total = (c_upper + p_upper)%26
        res = chr(total + ord('A'))
        return res if c.isupper() else res.lower()

    return c


def decode_letter(c:str, p: str = None) -> str:
    '''
    >>> decode_letter('H')
    'H'
    >>> decode_letter('l', 'H')
    'e'
    >>> decode_letter('U', 'p')
    'F'
    '''
    if p is not None:
        c_upper = ord(c.upper()) - ord('A')
        p_upper = ord(p.upper()) - ord('A')
        total = (c_upper - p_upper)%26
        res = chr(total + ord('A'))
        return res if c.isupper() else res.lower()

    return c

def find_last_alpha(message: str, current_index: int) -> str:
    """
    Helper function to find the last alphabetic character before current_index.
    Returns None if no such character exists.
    """
    for j in range(current_index - 1, -1, -1):
        if message[j].isalpha():
            return message[j]
    return None

def encode(message:str) -> str:
    '''
    >>> encode('Henry Walton Jones Jr.')
    'Hlrep Uwlehb Wxbrw Ba.'
    '''
    res = []
    punctuation = {' ', '.', ',', "'", '!', '?', ';', ':', '-', '"', '(', ')'}

    for i, char in enumerate(message):
        if char in punctuation or not char.isalpha():
            res.append(char)
        else:
            if i == 0:
                # First character, encode without a previous character
                res.append(encode_letter(char))
            else:

                last_alpha = find_last_alpha(message, i)
                if last_alpha:
                    res.append(encode_letter(char, last_alpha))
                else:

                    res.append(encode_letter(char))

    return ''.join(res)



def find_last_alpha_decode(message: str, current_index: int, decoded_res: list) -> str:

    for j in range(current_index - 1, -1, -1):
        if message[j].isalpha():
            if j < len(decoded_res):
                return decoded_res[j]
            else:
                return None
    return None


def decode(message: str) -> str:

    res = []
    punctuation = {' ', '.', ',', "'", '!', '?', ';', ':', '-', '"', '(', ')'}

    for i, char in enumerate(message):
        if char in punctuation or not char.isalpha():
            res.append(char)
        else:
            if i == 0:

                res.append(decode_letter(char))
            else:

                last_alpha = find_last_alpha_decode(message, i, res)
                if last_alpha:
                    res.append(decode_letter(char, last_alpha))
                else:

                    res.append(decode_letter(char))

    return ''.join(res)


