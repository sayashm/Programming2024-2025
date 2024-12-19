# https://dodona.be/nl/courses/4157/series/46299/activities/341848809


class ISBN13:
    '''
    >>> code = ISBN13(9780136110675)
    >>> print(code)
    978-0-13611067-5
    >>> code
    ISBN13(9780136110675, 1)
    >>> code.isvalid()
    True
    >>> code.asISBN10()
    '0-13611067-3'
    '''

    def __init__(self, code, length = 1):
        assert (
            isinstance(code, int)
            and isinstance(length, int)
            and 1<= length <=5
        ), 'invalid ISBN code'

        self.code = f'{code:013d}'
        self.length = length

    def __int__(self):
        return int(self.code)

    def __str__(self):
        code = self.code
        return f'{code[:3]}-{code[3:3+self.length]}-{code[3+self.length:-1]}-{code[-1]}'

    def __repr__(self):
        return f'ISBN13({self.code}, {self.length})'

    def isvalid(self):

        def checkdigit(code):

            check = sum(
                (3 if index %2 else 1) * int(digit)
                for index, digit in enumerate(code[:12])
            )

            return str((10 - check)%10)

        return self.code[12] == checkdigit(self.code)

    def asISBN10(self):

        def checkdigit(code):

            check = sum(
                index * int(digit)
                for index,digit in enumerate(code[:9], start = 1)
            ) % 11

            return 'X' if check == 10 else str(check)

        if not self.isvalid() or not self.code.startswith('978'):
            return None

        code = self.code[3:-1]
        check = checkdigit(code)

        return f'{code[:self.length]}-{code[self.length:]}-{check}'

    if __name__ == '__main__':
        import doctest
        doctest.testmod()