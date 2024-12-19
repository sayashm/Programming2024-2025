# https://dodona.be/en/courses/4157/series/52181/activities/541023107/


def read_key (location:str)->dict:
    with open(location, 'r', encoding='utf-8') as reader:
        lines = reader.readlines()
    # remove \n from end of lines
    lines  = [line.rstrip() for line in lines]
    # make an empty dictionary
    key = {}
    for line in lines:
        if len(line)<=3: # consider if we have ' ' at the end of strings
            line += ' '
        key[line[-1]] = line[:3]
    return key


def encode(plaintext:str, location:str)->str:
    # make key:dict from the location
    key = read_key(location)
    # to avoiding errors if a letter is not in key:dict I used try and expect method
    try:
        return ''.join([key[letter] for letter in plaintext])
    except:
        raise AssertionError('invalid key')

def invert_key(key:dict)->dict:
    # invert key:dict by for loop
    return {key[k]: k for k in key}


def decode(code:str, location:str)->str:
    length = len(code)//3 # each code has 3 character, so I divided code to 3
    key = read_key(location) # make key:dict by using the location address
    inv_ket = invert_key(key) # make invert_key by using key
    # to avoiding errors if a letter is not in key:dict I used try and expect method
    try:
        # each 3 letters in the code goes to find there value in inverted key in a for loop
        return ''.join([inv_ket[code[i*3 : (i+1)*3]] for i in range(length)])
    except:
        raise AssertionError('invalid ciphertext')



def main_test():
    '''
    >>> key = read_key('kenny.01.txt')
>>> key['O']
'FFM'
>>> key['h']
'pmm'
>>> key[' ']
'PMm'

>>> encode('Oh my god! They killed Kenny.', 'kenny.01.txt')
'FFMpmmPMmpfpPPmPMmMPFFMFmFpmmPPMmmpFpmmMfFPPmPMmpmPFFPmfPmfPMfFmFpPMmFffMfFmmMmmMPPmFMm'
>>> encode("Don't lie, Stan. Lying makes you sterile.", 'kenny.02.txt')
'FfPFMfmFFPPFpmFpMMmPFfPPfpPPPfpMMFFfpmFpFFmFFpPFpMMpFfPPmfPPmFFMPfpMMMpPpFFMFffpPMMPpMMPPmFMfFpMpMMMMPpmFfpPMFPfPPmPFfpPpPF'
>>> encode('Oh my god! They killed Kenny.', 'kenny.02.txt')
Traceback (most recent call last):
AssertionError: invalid key

>>> inverted_key = invert_key(key)
>>> inverted_key['FFM']
'O'
>>> inverted_key['pmm']
'h'
>>> inverted_key['PMm']
' '

>>> decode('FFMpmmPMmpfpPPmPMmMPFFMFmFpmmPPMmmpFpmmMfFPPmPMmpmPFFPmfPmfPMfFmFpPMmFffMfFmmMmmMPPmFMm', 'kenny.01.txt')
'Oh my god! They killed Kenny.'
>>> decode('FfPFMfmFFPPFpmFpMMmPFfPPfpPPPfpMMFFfpmFpFFmFFpPFpMMpFfPPmfPPmFFMPfpMMMpPpFFMFffpPMMPpMMPPmFMfFpMpMMMMPpmFfpPMFPfPPmPFfpPpPF', 'kenny.02.txt')
"Don't lie, Stan. Lying makes you sterile."
>>> decode('FFMpmmPMmpfpPPmPMmMPFFMFmFpmmPPMmmpFpmmMfFPPmPMmpmPFFPmfPmfPMfFmFpPMmFffMfFmmMmmMPPmFMm', 'kenny.02.txt')
Traceback (most recent call last):
AssertionError: invalid ciphertext

    '''

if __name__ == '__main__':
    import doctest
    doctest.testmod()