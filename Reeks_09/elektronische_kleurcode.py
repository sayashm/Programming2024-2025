# https://dodona.be/nl/courses/4157/series/46298/activities/668507685

def read_specification(location:str)->dict:
    with open(location, 'r', encoding='utf-8') as reader:
        reader.readline()
        lines = reader.readlines()

    firstline = ['name','digit','multiplier','tolerance']
    lines = [line.rstrip().split(',') for line in lines]

    main_dict = {}
    for line in lines:
        sub_dict = {}
        for i in range(3):

            if line[1:][i] != '-':
                if firstline[1:][i] == 'tolerance':
                    sub_dict[firstline[1:][i]] = float(line[1:][i])
                else:
                    sub_dict[firstline[1:][i]] = int(line[1:][i])

            main_dict[line[0].lower()] = sub_dict

    return main_dict

def lookup(color:str, name:str, code:dict)->int|float:
    try:
        return code[color.lower()][name.lower()]
    except:
        raise AssertionError('invalid code')

def resistance(bands: str, code: dict) -> str:
    try:
        bands = bands.lower().split()
        band_count = len(bands)

        if band_count == 3:  # 3-band resistor
            digit1 = code[bands[0]]['digit']
            digit2 = code[bands[1]]['digit']
            multiplier = code[bands[2]]['multiplier']
            resistance_value = (digit1 * 10 + digit2) * (10 ** multiplier)
            tolerance = code['none']['tolerance']  # Default tolerance for 3-band resistors (no tolerance band)
        elif band_count == 4:  # 4-band resistor
            digit1 = code[bands[0]]['digit']
            digit2 = code[bands[1]]['digit']
            multiplier = code[bands[2]]['multiplier']
            tolerance = code[bands[3]]['tolerance']
            resistance_value = (digit1 * 10 + digit2) * (10 ** multiplier)
        elif band_count == 5:  # 5-band resistor
            digit1 = code[bands[0]]['digit']
            digit2 = code[bands[1]]['digit']
            digit3 = code[bands[2]]['digit']
            multiplier = code[bands[3]]['multiplier']
            tolerance = code[bands[4]]['tolerance']
            resistance_value = (digit1 * 100 + digit2 * 10 + digit3) * (10 ** multiplier)
        else:
            raise AssertionError('invalid code')

        return f"{resistance_value:.3f}Ω (±{tolerance:.2f}%)"

    except KeyError:
        raise AssertionError('invalid code')


def main_tests():
    '''
    >>> specs = read_specification('IEC60062_2016.csv')
    >>> specs
    {'none': {'tolerance': 20.0}, 'pink': {'multiplier': -3}, 'silver': {'multiplier': -2, 'tolerance': 10.0}, 'gold': {'multiplier': -1, 'tolerance': 5.0}, 'black': {'digit': 0, 'multiplier': 0}, 'brown': {'digit': 1, 'multiplier': 1, 'tolerance': 1.0}, 'red': {'digit': 2, 'multiplier': 2, 'tolerance': 2.0}, 'orange': {'digit': 3, 'multiplier': 3}, 'yellow': {'digit': 4, 'multiplier': 4}, 'green': {'digit': 5, 'multiplier': 5, 'tolerance': 0.5}, 'blue': {'digit': 6, 'multiplier': 6, 'tolerance': 0.25}, 'violet': {'digit': 7, 'multiplier': 7, 'tolerance': 0.1}, 'gray': {'digit': 8, 'multiplier': 8, 'tolerance': 0.05}, 'white': {'digit': 9, 'multiplier': 9}}

    >>> lookup('BLUE', 'digit', specs)
    6
    >>> lookup('black', 'MULTIPLIER', specs)
    0
    >>> lookup('PINK', 'TOLERANCE', specs)
    Traceback (most recent call last):
    AssertionError: invalid code
    >>> lookup('none', 'tolerance', specs)
    20.0

    >>> resistance('yellow violet red gold', specs)
    '4700.000Ω (±5.00%)'
    >>> resistance('orange orange brown', specs)
    '330.000Ω (±20.00%)'
    >>> resistance('GRAY RED ORANGE GOLD', specs)
    '82000.000Ω (±5.00%)'
    >>> resistance('green red brown black brown', specs)
    '521.000Ω (±1.00%)'
    >>> resistance('green gold brown', specs)
    Traceback (most recent call last):
    AssertionError: invalid code
    '''

if __name__ == "__main__":
    import doctest
    doctest.testmod()
