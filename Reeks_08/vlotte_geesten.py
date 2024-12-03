# https://dodona.be/nl/courses/4157/series/46297/activities/1400092306

def isitem(arg)->bool:
    '''
    >>> table = [('red', 'chair'), ('blue', 'book'), ('green', 'bottle'), ('gray', 'mouse'), ('white', 'ghost')]
    >>> card1 = [('blue', 'book'), ('green', 'chair')]
    >>> card2 = (('white', 'bottle'), ('gray', 'mouse'))
    >>> card3 = {('red', 'ghost'), ('green', 'bottle')}
    >>> card4 = [('blue', 'ghost'), ('gray', 'chair')]
    >>> card5 = (('white', 'mouse'), ('red', 'book'))

    >>> isitem(('blue', 'book'))
    True
    >>> isitem(['green', 'ghost'])
    False
    >>> isitem(('white', 'lang', 'bottle'))
    False
    >>> isitem((666, 'chair'))
    False
    '''

    if not isinstance(arg, tuple):
        return False
    if len(arg) != 2:
        return False
    if not all(isinstance(prop, str) for prop in arg):
        return False
    return True

def iscollection(arg)->bool:
    '''
    # >>> table = [('red', 'chair'), ('blue', 'book'), ('green', 'bottle'), ('gray', 'mouse'), ('white', 'ghost')]
    # >>> card1 = [('blue', 'book'), ('green', 'chair')]
    # >>> card2 = (('white', 'bottle'), ('gray', 'mouse'))
    # >>> card3 = {('red', 'ghost'), ('green', 'bottle')}
    # >>> card4 = [('blue', 'ghost'), ('gray', 'chair')]
    # >>> card5 = (('white', 'mouse'), ('red', 'book'))
    #
    # >>> iscollection(table)
    # True
    # >>> iscollection(card1)
    # True
    # >>> iscollection(card2)
    # True
    # >>> iscollection(frozenset(table))
    # False
    # >>> iscollection([666] + table)
    # False
    # >>> iscollection([('white', 'ghost'), ('white', 'ghost')])
    # False
    # >>> iscollection([('white', 'ghost'), ('white', 'chair')])
    # False
    # >>> iscollection([('white', 'chair'), ('red', 'chair')])
    # False
    >>> iscollection({('red', 'grape'), ('gray', 'banana'), ('white', 'chair'), ('green', 'pumpkin'), ('pink', 'ghost'), ('purple', 'cow'), ('blue', 'bottle'), ('yellow', 'flamingo')})
    True
    '''

    if not isinstance(arg, (list, tuple, set)):
        return False

    items = list(arg)

    for elem in items:
        if not isitem(elem):
            return False

    if len(set(items)) != len(items):
        return False

    colors = [color for color, shape in items]
    shapes = [shape for color, shape in items]

    if len(set(colors)) != len(colors):
        return False
    if len(set(shapes)) != len(shapes):
        return False

    return True

def istable(arg):
    """
    >>> table = [('red', 'chair'), ('blue', 'book'), ('green', 'bottle'), ('gray', 'mouse'), ('white', 'ghost')]
    >>> card1 = [('blue', 'book'), ('green', 'chair')]
    >>> istable(table)
    True
    >>> istable(card1)
    False
    """
    if not iscollection(arg):
        return False
    items = list(arg)
    if len(items) != 5:
        return False
    return True

def iscard(card, table):
    '''
    >>> table = [('red', 'chair'), ('blue', 'book'), ('green', 'bottle'), ('gray', 'mouse'), ('white', 'ghost')]
    >>> card1 = [('blue', 'book'), ('green', 'chair')]
    >>> card2 = (('white', 'bottle'), ('gray', 'mouse'))
    >>> card3 = {('red', 'ghost'), ('green', 'bottle')}
    >>> card4 = [('blue', 'ghost'), ('gray', 'chair')]
    >>> card5 = (('white', 'mouse'), ('red', 'book'))
    >>> iscard(card1, table)
    True
    >>> iscard(card2, table)
    True
    >>> iscard([('blue', 'book'), ('green', 'chair'), ('white', 'bottle')], table)
    False
    >>> iscard([('blue', 'book'), ('green', 'kikker')], table)
    False
    >>> iscard(table, card1)
    Traceback (most recent call last):
    AssertionError: invalid table
    '''
    if not istable(table):
        raise AssertionError("invalid table")

    if not isinstance(card, (list, tuple, set)):
        return False

    card_items = list(card)

    if len(card_items) != 2:
        return False

    for item in card_items:
        if not isitem(item):
            return False

    table_items = list(table)
    table_shapes = set(shape for color, shape in table_items)
    table_colors = set(color for color, shape in table_items)

    card_shapes = set(shape for color, shape in card_items)
    card_colors = set(color for color, shape in card_items)

    for color, shape in card_items:
        if shape not in table_shapes or color not in table_colors:
            return False

    matching_items = set(table_items) & set(card_items)
    num_matching_items = len(matching_items)

    num_non_matching_items = 0
    for color, shape in table_items:
        if color not in card_colors and shape not in card_shapes:
            num_non_matching_items += 1

    condition1 = (num_matching_items == 1)
    condition2 = (num_non_matching_items == 1)

    if (condition1 and not condition2) or (condition2 and not condition1):
        return True
    else:
        return False

def grab(table, card):
    '''
    >>> table = [('red', 'chair'), ('blue', 'book'), ('green', 'bottle'), ('gray', 'mouse'), ('white', 'ghost')]
    >>> card1 = [('blue', 'book'), ('green', 'chair')]
    >>> card2 = (('white', 'bottle'), ('gray', 'mouse'))
    >>> card3 = {('red', 'ghost'), ('green', 'bottle')}
    >>> card4 = [('blue', 'ghost'), ('gray', 'chair')]
    >>> card5 = (('white', 'mouse'), ('red', 'book'))

    >>> grab(table, card1)
    ('blue', 'book')
    >>> grab(table, card2)
    ('gray', 'mouse')
    >>> grab(table, card3)
    ('green', 'bottle')
    >>> grab(table, card4)
    ('green', 'bottle')
    >>> grab(table, card5)
    ('green', 'bottle')
    >>> grab(card1, table)
    Traceback (most recent call last):
    AssertionError: invalid table
    >>> grab(table, [('blue', 'book'), ('green', 'kikker')])
    Traceback (most recent call last):
    AssertionError: invalid card
    '''
    if not istable(table):
        raise AssertionError("invalid table")

    if not iscard(card, table):
        raise AssertionError("invalid card")

    card_items = list(card)
    table_items = list(table)

    card_shapes = {shape for _, shape in card_items}
    card_colors = {color for color, _ in card_items}

    matching_items = set(table_items) & set(card_items)
    if len(matching_items) == 1:
        return matching_items.pop()

    non_matching_items = [
        item for item in table_items
        if item[0] not in card_colors and item[1] not in card_shapes
    ]
    if len(non_matching_items) == 1:
        return non_matching_items[0]

    return None