# https://dodona.be/nl/courses/4157/series/46296/activities/1158810383


def is_serial(serial: int | str):
    if not serial.isdigit() or int(serial) == 0:
        raise AssertionError("invalid serial number")


def serial_number(serial: int | str):
    '''
    >>> serial_number(834783)
    '00834783'
    >>> serial_number('47839')
    '00047839'
    >>> serial_number(834783244839184)
    '834783244839184'
    >>> serial_number('4783926132432*')
    Traceback (most recent call last):
    AssertionError: invalid serial number
    '''
    serial = str(serial)
    l = len(serial)

    is_serial(serial)
    return (8 - l) * '0' + serial if l < 8 else serial



def solid(serial: int | str):
    '''
    >>> solid(44444444)
    True
    >>> solid('44544444')
    False
    '''
    serial = serial_number(serial)

    return len(set(serial)) < 2


def radar(serial: int | str):
    '''
    >>> radar(1133110)
    True
    >>> radar('83289439')
    False
    '''
    serial = serial_number(serial)
    if solid(serial):
        return False
    return serial == serial[-1::-1]


def repeater(serial: int | str):
    '''
    >>> repeater(20012001)
    True
    >>> repeater('83289439')
    False
    >>> repeater('77777777')
    False
    '''
    serial = serial_number(serial)

    if solid(serial):
        return False

    l = len(serial)//2
    return serial[:l] == serial[l:]

def radar_repeater(serial: int | str):
    '''
    >>> radar_repeater('12211221')
    True
    >>> radar_repeater('83289439')
    False
    '''
    serial = serial_number(serial)

    return radar(serial) and repeater(serial)

def numismatist(serials: list | tuple, kind = solid ):
    '''
    >>> numismatist([33333333, 1133110, '77777777', '12211221'])
    [33333333, '77777777']
    >>> numismatist([33333333, 1133110, '77777777', '12211221'], radar)
    [1133110, '12211221']
    >>> numismatist([33333333, 1133110, '77777777', '12211221'], kind=repeater)
    ['12211221']
    '''

    return [serial for serial in serials if kind(serial_number(serial))]