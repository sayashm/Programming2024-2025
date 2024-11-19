# https://dodona.be/nl/courses/4157/series/46295/activities/70570533

def cross_section(r:int, s:str ):
    '''
    >>> cross_section(4, 'NSSWNSSWNWNWEWSWNSSEEWSWEWSENSSWNENWNSNEEWEWSWSENWNESEEWNWNWSESW')
    [['NS', 'SW', 'NS', 'SW', 'NW', 'NW', 'EW', 'SW'], ['NS', 'SE', 'EW', 'SW', 'EW', 'SE', 'NS', 'SW'], ['NE', 'NW', 'NS', 'NE', 'EW', 'EW', 'SW', 'SE'], ['NW', 'NE', 'SE', 'EW', 'NW', 'NW', 'SE', 'SW']]
    >>> cross_section(4, 'NSSWNSSWNWNWEWSWNSS')
    Traceback (most recent call last):
    AssertionError: invalid cross-section
    '''
    c = len(s) // r // 2
    n = len(s) // 2
    if (r == 0 and n != 0) or (r != 0 and n % r != 0):
        raise AssertionError("invalid cross-section")

    return [[s[2*i : (2*i)+2] for i in range(len(s)//2)][(c)*i: (c)*i+(c)] for i in range(r)]




def depth(cave):
    '''
    >>> cave = cross_section(4, 'NSSWNSSWNWNWEWSWNSSEEWSWEWSENSSWNENWNSNEEWEWSWSENWNESEEWNWNWSESW')
    >>> depth(cave)
    11
    '''
    if not cave or not cave[0]:
        return 0
    rows, cols = len(cave), len(cave[0])
    position = (0, 0)
    came_from = 'N'
    depth_counter = 0
    visited = set()

    # Direction mappings
    delta = {'N': (-1, 0), 'S': (1, 0), 'E': (0, 1), 'W': (0, -1)}
    opposite = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}

    while True:
        i, j = position
        if position in visited:
            break  # Avoid cycles
        visited.add(position)

        corridor = cave[i][j]
        if came_from not in corridor:
            break  # Can't enter from this side

        # Determine exit direction
        sides = set(corridor)
        sides.remove(came_from)
        if not sides:
            break  # Dead end
        exit_side = sides.pop()

        # Move to next position
        di, dj = delta[exit_side]
        new_i, new_j = i + di, j + dj

        # Increment depth
        depth_counter += 1

        # Check if we've exited the cave
        if not (0 <= new_i < rows and 0 <= new_j < cols):
            break

        position = (new_i, new_j)
        came_from = opposite[exit_side]

    return depth_counter







    


