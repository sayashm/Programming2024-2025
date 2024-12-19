# https://dodona.be/nl/courses/4157/series/46299/activities/2145526972
import math


class Block:
    '''
    >>> rock = Block(5, 2, 3)
    >>> rock
    Block(length=5, height=2, width=3, position=(0, 0))
    >>> rock.area()
    62.0
    >>> rock.volume()
    30.0
    >>> rock.diagonal()
    6.164414002968976
    >>> rock2 = rock.slide('R')
    >>> rock2
    Block(length=5, height=2, width=3, position=(0, 5))
    >>> rock is rock2
    True
    >>> rock.slide('F')
    Block(length=5, height=2, width=3, position=(3, 5))
    >>> rock.tilt('L')
    Block(length=2, height=5, width=3, position=(3, 3))
    >>> rock.tilt('B')
    Block(length=2, height=3, width=5, position=(0, 3))
    >>> rock.tilt('B').slide('L').tilt('L').slide('B')
    Block(length=5, height=2, width=3, position=(-8, -4))
    >>> rock.sail('SB')
    Block(length=5, height=2, width=3, position=(-11, -4))
    >>> rock.sail('TR')
    Block(length=2, height=5, width=3, position=(-11, 1))
    >>> rock.sail('SFSFTLSLTBTBSRSFTRTFTRTRSBSF')
    Block(length=2, height=3, width=5, position=(-2, 6))

    >>> rock.tilt('X')
    Traceback (most recent call last):
    AssertionError: invalid direction
    >>> rock.sail('XY')
    Traceback (most recent call last):
    AssertionError: invalid movement
    >>> rock.sail('TY')
    Traceback (most recent call last):
    AssertionError: invalid direction
    '''
    def __init__(self, length:int, height:int, width:int, position: list|tuple = None):
        self.length = length
        self.height = height
        self.width = width

        if position is None:
            self.position = (0, 0)
        else:
            self.position = tuple(position)

    def __str__(self):
        return f'Block(length={self.length}, height={self.height}, width={self.width}, position={self.position})'

    def __repr__(self):
        return self.__str__()

    def area(self):
        return float(2 * ((self.length * self.height)+(self.height * self.width)+(self.width * self.length)))

    def volume(self):
        return float(self.length * self.height * self.width)

    def diagonal(self):
        return float(math.sqrt(self.length**2 + self.height**2 + self.width**2))

    def slide(self, direction:str):

        def tuple_sum(first_tuple, second_tuple):
            return tuple(first_tuple[i] + second_tuple[i] for i in range(len(first_tuple)))

        offsets = {
            'R': (0, self.length),
            'L': (0, -self.length),
            'F': (self.width, 0),
            'B': (-self.width, 0)
        }

        direction = direction.upper()
        if direction not in offsets:
            raise AssertionError('invalid direction')

        self.position = tuple_sum(self.position, offsets[direction])

        return self

    def tilt(self, direction:str):

        def tuple_sum(first_tuple, second_tuple):
            return tuple(first_tuple[i] + second_tuple[i] for i in range(len(first_tuple)))

        direction = direction.upper()
        if direction not in 'RLBF':
            raise AssertionError('invalid direction')

        if direction == 'L':

            self.position = tuple_sum(self.position , (0 ,  -self.height))
            self.length, self.height = self.height, self.length

        elif direction == 'R' :

            self.length, self.height = self.height, self.length
            self.position = tuple_sum(self.position , (0 ,  +self.height))

        elif direction == 'B':
            self.position = tuple_sum(self.position, (-self.width, 0))
            self.width, self.height = self.height, self.width

        elif direction == 'F':
            self.width, self.height = self.height, self.width
            self.position = tuple_sum(self.position, (+self.width, 0))


        return self

    def sail(self, movements:str):

        assert len(movements) % 2 == 0 , 'invalid movement'
        assert all(movements[(i * 2)] in 'ST' for i in range(len(movements) // 2)), 'invalid movement'
        assert all(movements[(i*2)+1] in 'RBFL' for i in range(len(movements)//2)), 'invalid direction'


        for m , d in ((movements[(i*2)],movements[(i*2)+1]) for i in range(len(movements)//2)):
            if m  == 'S':
                self.slide(d)
            elif m == 'T':
                self.tilt(d)
        return self

