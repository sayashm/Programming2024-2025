# https://dodona.be/nl/courses/4157/series/46299/activities/657937938

class Necklace:
    '''
    >>> necklace = Necklace('Jessica')
    >>> necklace
    Necklace('Jessica')
    >>> print(necklace)
    Jessica
    >>> len(necklace)
    7
    >>> necklace.slide(1)
    Necklace('essicaJ')
    >>> necklace
    Necklace('essicaJ')
    >>> necklace.slide(-2)
    Necklace('aJessic')
    >>> necklace.slide(11)
    Necklace('sicaJes')
    >>> necklace.forms() == {'SICAJES', 'ESSICAJ', 'AJESSIC', 'JESSICA', 'CAJESSI', 'SSICAJE', 'ICAJESS'}
    True
    >>> necklace
    Necklace('sicaJes')
    >>> necklace.normal_form()
    'AJESSIC'

    >>> necklace == Necklace('Louise')
    False
    >>> Necklace('Louise') == Necklace('Elouis')
    True

    >>> necklace = Necklace('Emily')
    >>> necklace
    Necklace('Emily')
    >>> necklace + 1
    Necklace('milyE')
    >>> necklace
    Necklace('Emily')
    >>> -2 + necklace
    Necklace('lyEmi')
    >>> necklace + 9
    Necklace('yEmil')
    >>> necklace + 'spam'
    Traceback (most recent call last):
    AssertionError: invalid operation
    '''
    def __init__(self, string:str):
        self.string = string

    def __str__(self):
        return self.string

    def __repr__(self):
        return f"Necklace('{self.string}')"

    def __len__(self):
        return len(self.string)

    def slide(self, m:int):

        def one_slide( d:int = 1):
            if d >= 0:
                self.string = (self.string + self.string[0])[1:]
            else:
                self.string = (self.string[-1] + self.string)[:-1]

        for _ in range(abs(m)):
            one_slide(m)

        return self

    def forms(self):

        res = set()
        s = self.string
        for _ in range(abs(len(self))):
            res.add(s.upper())
            s = (s + s[0])[1:]
        return res

    def normal_form(self):
        # Convert the necklace string to uppercase for case insensitivity
        necklace_upper = self.string.upper()

        # Generate all possible rotations of the string
        rotations = [necklace_upper[i:] + necklace_upper[:i] for i in range(len(necklace_upper))]

        # Return the lexicographically smallest rotation
        return min(rotations)

    def __eq__(self, other):
        if not isinstance(other, Necklace):
            return False
        if len(self.string) != len(other.string):
            return False

        return self.string.upper() in (other.string.upper()+other.string.upper())

    def __add__(self, other):
        # Adding an integer should return a new rotated necklace, not modify the original
        if isinstance(other, int):
            new_necklace = Necklace(self.string)
            new_necklace.slide(other)
            return new_necklace
        # If not int, raise error as per the examples
        raise AssertionError("invalid operation")

    def __radd__(self, other):
        # Handling cases like -2 + necklace
        if isinstance(other, int):
            new_necklace = Necklace(self.string)
            new_necklace.slide(other)
            return new_necklace
        # If not int, raise error
        raise AssertionError("invalid operation")

if __name__ == '__main__':
    import doctest
    doctest.testmod()