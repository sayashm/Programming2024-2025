# https://dodona.be/nl/courses/4157/series/46299/activities/1405884908


class Eureka:
    '''
    >>> game = Eureka('RPG,G,PR')
    >>> game
    Eureka('RPG,G,PR', maximum=4)

    >>> print(game)
    = = = = = =
    | | | | | |
    |G| | | | |
    |P| | | |R|
    |R| |G| |P|
    === === ===
    >>> game.transfer(0, 1, 1)
    Eureka('RP,GG,PR', maximum=4)
    >>> print(game)
    = = = = = =
    | | | | | |
    | | | | | |
    |P| |G| |R|
    |R| |G| |P|
    === === ===
    >>> game.transfer(1, 2, 2)
    Eureka('RP,,PRGG', maximum=4)
    >>> print(game)
    = = = = = =
    | | | | |G|
    | | | | |G|
    |P| | | |R|
    |R| | | |P|
    === === ===
    >>> game.transfer(0, 1, 1)
    Eureka('R,P,PRGG', maximum=4)
    >>> print(game)
    = = = = = =
    | | | | |G|
    | | | | |G|
    | | | | |R|
    |R| |P| |P|
    === === ===
    >>> game.transfer(2, 1, 1).transfer(2, 0, 1)
    Eureka('RG,PG,PR', maximum=4)
    >>> print(game)
    = = = = = =
    | | | | | |
    | | | | | |
    |G| |G| |R|
    |R| |P| |P|
    === === ===
    >>> game.flip(2)
    Eureka('RG,PG,RP', maximum=4, flipped=2)
    >>> print(game)
    = = = = ===
    | | | | | |
    | | | | | |
    |G| |G| |P|
    |R| |P| |R|
    === === = =
    >>> game == Eureka('RP,RG,PG')
    True
    >>> game == Eureka('PR,RG,PG')
    False

    >>> game.flip(100)                     # wrong tube index
    Traceback (most recent call last):
    AssertionError: invalid move
    >>> game.flip(0)                       # another tube is already flipped over
    Traceback (most recent call last):
    AssertionError: invalid move
    >>> game.transfer(0, 1)                # a tube is flipped over
    Traceback (most recent call last):
    AssertionError: invalid move

    >>> game.flip(2)
    Eureka('RG,PG,PR', maximum=4)
    >>> print(game)
    = = = = = =
    | | | | | |
    | | | | | |
    |G| |G| |R|
    |R| |P| |P|
    === === ===
    >>> game.transfer(0, 100)              # wrong tube index
    Traceback (most recent call last):
    AssertionError: invalid move
    >>> game.transfer(100, 0)              # wrong tube index
    Traceback (most recent call last):
    AssertionError: invalid move
    >>> game.transfer(0, 0)                # tube cannot be transferred into itself
    Traceback (most recent call last):
    AssertionError: invalid move
    >>> game.transfer(0, 1)
    Eureka(',PGGR,PR', maximum=4)
    >>> print(game)
    = = = = = =
    | | |R| | |
    | | |G| | |
    | | |G| |R|
    | | |P| |P|
    === === ===
    >>> game.transfer(2, 1)                # capacity of tube 1 would be exceeded
    Traceback (most recent call last):
    AssertionError: invalid move
    >>> game.transfer(0, 1)
    Eureka(',PGGR,PR', maximum=4)
    >>> print(game)
    = = = = = =
    | | |R| | |
    | | |G| | |
    | | |G| |R|
    | | |P| |P|
    === === ===
    '''

    def __init__(self, balls:str, maximum:int = 4, flipped:int = None):


        self.maximum = maximum
        self.balls = balls
        self.flipped = flipped
        self._tubes = [list(t) for t in balls.split(',')]
        for tube in self._tubes:
            if len(tube) > maximum:
                raise AssertionError("invalid configuration")
        if flipped is not None:
            if flipped < 0 or flipped >= len(self._tubes):
                raise AssertionError("invalid configuration")



    def balls_list(self):
        return self.balls.split(',')

    def tubes(self):
        return [(' ' * (self.maximum - len(ball))) + ball[::-1]
                for ball in self.balls_list()]



    def __str__(self):
        t = '= ='
        b = '==='
        top = [t] * len(self.balls_list())
        button = [b] * len(self.balls_list())
        if self.flipped is not None:
            top[self.flipped] = b
            button[self.flipped] = t

        output = [' '.join(top)]
        for i in range(self.maximum):
            output.append(' '.join([f'|{tube[i]}|' for tube in self.tubes()]))

        output.append(' '.join(button))

        return '\n'.join(output)

    def __repr__(self):
        if self.flipped is None:
            return f"Eureka('{self.balls}', maximum={self.maximum})"
        return f"Eureka('{self.balls}', maximum={self.maximum}, flipped={self.flipped})"

    def transfer(self, source, destination, number = None):
        # Check general conditions
        assert (
            self.flipped is None and
            0 <= source < len(self._tubes)
        ), 'invalid move'

        res = self.balls_list()
        if len(res[source]) == 0:
            # No balls to transfer; this does nothing but is allowed
            return self

        assert (
            0 <= destination < len(self._tubes) and
            source != destination
        ), 'invalid move'

        # Determine how many balls to transfer
        if number is None:
            number = len(res[source])

        # Check if source has enough balls
        if len(res[source]) < number:
            raise AssertionError('invalid move')

        # Check capacity before moving ANY balls
        if len(res[destination]) + number > self.maximum:
            raise AssertionError('invalid move')

        # Perform the transfer
        for _ in range(number):
            res[destination] += res[source][-1]
            res[source] = res[source][:-1]
        self.balls = ','.join(res)
        return self


    def flip(self, number:int):
        ball_list = self.balls_list()

        assert (
            0 <= number < len(self._tubes) and
            (self.flipped == number or self.flipped is None)

        ), 'invalid move'

        ball_list[number] =  ball_list[number][::-1]
        self.balls = ','.join(ball_list)
        if self.flipped is None:
            self.flipped = number
        elif self.flipped == number:
            self.flipped = None
        else:
            raise AssertionError('invalid move')
        return self




    def __eq__(self, other):
        if not isinstance(other, Eureka):
            return False
        return set(self.balls_list()) == set(other.balls_list())

if __name__ == '__main__':
    import doctest
    doctest.testmod()