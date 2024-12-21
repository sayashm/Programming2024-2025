# https://dodona.be/nl/courses/4157/series/46299/activities/2066879933

class Formula:
    '''
    >>> wheel = Formula('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz')
    >>> wheel
    Formula('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz')
    >>> print(wheel)
    stabilis: ABCDEFGHIJKLMNOPQRSTUVWXYZ
    mobilis:  abcdefghijklmnopqrstuvwxyz
    >>> wheel.encode_symbol('K')
    'k'
    >>> wheel.decode_symbol('x')
    'X'
    >>> wheel.rotate(2)
    Formula('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'cdefghijklmnopqrstuvwxyzab')
    >>> print(wheel)
    stabilis: ABCDEFGHIJKLMNOPQRSTUVWXYZ
    mobilis:  cdefghijklmnopqrstuvwxyzab
    >>> wheel.encode_symbol('K')
    'm'
    >>> wheel.decode_symbol('x')
    'V'
    >>> wheel.rotate(11)
    Formula('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'nopqrstuvwxyzabcdefghijklm')
    >>> print(wheel)
    stabilis: ABCDEFGHIJKLMNOPQRSTUVWXYZ
    mobilis:  nopqrstuvwxyzabcdefghijklm
    >>> wheel.rotate(-5)
    Formula('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'ijklmnopqrstuvwxyzabcdefgh')
    >>> print(wheel)
    stabilis: ABCDEFGHIJKLMNOPQRSTUVWXYZ
    mobilis:  ijklmnopqrstuvwxyzabcdefgh
    >>> wheel.reset()
    Formula('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz')
    >>> print(wheel)
    stabilis: ABCDEFGHIJKLMNOPQRSTUVWXYZ
    mobilis:  abcdefghijklmnopqrstuvwxyz
    >>> wheel.encode('DECIFRIS', 1, 2, 3)
    'efdliunx'
    >>> wheel.decode('efdliunx', 1, 2, 3)
    'DECIFRIS'

    >>> Formula('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz') + 3
    Formula('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'defghijklmnopqrstuvwxyzabc')
    >>> 3 + Formula('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz')
    Formula('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'defghijklmnopqrstuvwxyzabc')
    >>> Formula('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz') - 3
    Formula('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'xyzabcdefghijklmnopqrstuvw')
    >>> 3 - Formula('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz')
    Formula('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'xyzabcdefghijklmnopqrstuvw')
    >>> wheel = Formula('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz')
    >>> wheel += 3
    >>> wheel
    Formula('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'defghijklmnopqrstuvwxyzabc')

    '''

    def __init__(self, stabilis, mobilis):
        # Validate input alphabets
        if len(stabilis) != len(mobilis):
            raise AssertionError("invalid wheel")
        if len(set(stabilis)) != len(stabilis) or len(set(mobilis)) != len(mobilis):
            raise AssertionError("invalid wheel")

        self._initial_stabilis = stabilis
        self._initial_mobilis = mobilis
        self._stabilis = stabilis
        self._mobilis = mobilis

    def __repr__(self):
        return f"Formula('{self._stabilis}', '{self._mobilis}')"

    def __str__(self):
        return f"stabilis: {self._stabilis}\nmobilis:  {self._mobilis}"

    def reset(self):
        self._stabilis = self._initial_stabilis
        self._mobilis = self._initial_mobilis
        return self

    def rotate(self, n):
        if not isinstance(n, int):
            raise AssertionError("invalid rotation")

        # Handle negative rotations (clockwise)
        actual_n = n % len(self._mobilis)
        self._mobilis = self._mobilis[actual_n:] + self._mobilis[:actual_n]
        return self

    def encode_symbol(self, symbol):
        if symbol not in self._stabilis:
            raise AssertionError("invalid symbol")
        idx = self._stabilis.index(symbol)
        return self._mobilis[idx]

    def decode_symbol(self, symbol):
        if symbol not in self._mobilis:
            raise AssertionError("invalid symbol")
        idx = self._mobilis.index(symbol)
        return self._stabilis[idx]

    def encode(self, plaintext, initial_rotation, periodic_rotation, period):
        # Save current state
        original_mobilis = self._mobilis

        try:
            # Reset and apply initial rotation
            self.reset()
            self.rotate(initial_rotation)

            result = ""
            for i, char in enumerate(plaintext):
                # Apply periodic rotation if needed (after first period)
                if i > 0 and period > 0 and i % period == 0:
                    self.rotate(periodic_rotation)
                result += self.encode_symbol(char)

            return result
        finally:
            # Restore original state
            self._mobilis = original_mobilis

    def decode(self, ciphertext, initial_rotation, periodic_rotation, period):
        # Save current state
        original_mobilis = self._mobilis

        try:
            # Reset and apply initial rotation
            self.reset()
            self.rotate(initial_rotation)

            result = ""
            for i, char in enumerate(ciphertext):
                # Apply periodic rotation if needed (after first period)
                if i > 0 and period > 0 and i % period == 0:
                    self.rotate(periodic_rotation)
                result += self.decode_symbol(char)

            return result
        finally:
            # Restore original state
            self._mobilis = original_mobilis

    def __add__(self, other):
        if not isinstance(other, int):
            raise AssertionError("invalid rotation")
        new_wheel = Formula(self._stabilis, self._mobilis)
        new_wheel.rotate(other)
        return new_wheel

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if not isinstance(other, int):
            raise AssertionError("invalid rotation")
        new_wheel = Formula(self._stabilis, self._mobilis)
        new_wheel.rotate(-other)
        return new_wheel

    def __rsub__(self, other):
        # For n - wheel, we want the same result as wheel - (-n)
        if not isinstance(other, int):
            raise AssertionError("invalid rotation")
        new_wheel = Formula(self._stabilis, self._mobilis)
        new_wheel.rotate(-other)
        return new_wheel

    def __iadd__(self, other):
        if not isinstance(other, int):
            raise AssertionError("invalid rotation")
        self.rotate(other)
        return self