# https://dodona.be/nl/courses/4157/series/46298/activities/292564648


def read_network(location:str)->dict:
    with open(location, 'r', encoding='utf-8') as reader:
        lines = reader.readlines()
    N_dict = {}
    for inx, line in enumerate(lines):
        l_dict = {}
        for jinx, j in enumerate(line.rstrip()):
            if j !='0':
                l_dict[jinx+1] = int(j)
        N_dict[inx+1] = l_dict

    return N_dict



def complementary_group(group:list|set|tuple, capacity:dict)->set:
    if len(group) == len(set(group))  and isNatural(group) and len(capacity) >= max(group):
        return set(capacity.keys()).difference(set(group))

    raise AssertionError('invalid group')


def isNatural(l : list) -> bool:
    return all(isinstance(i, int) and i > 0 for i in l)

def flow(group:list|set|tuple, capacity:dict)->int:
    if len(group) == len(set(group)) and isNatural(group) and len(capacity) >= max(group):
        g_bar = complementary_group(group,capacity)
        g = set(group)

        return sum(capacity[i][j] for i in g for j in g_bar if j in capacity[i])

    raise AssertionError('invalid group')



def main_tests():
    '''
    >>> network = read_network('karate.txt')
    >>> network[11]
    {1: 2, 5: 3, 6: 3}
    >>> network[24]
    {26: 5, 28: 4, 30: 2, 33: 5, 34: 4}

    >>> group = [1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 13, 14, 17, 18, 20, 22]
    >>> complementary_group(group, network) # doctest: +SKIP
    {9, 10, 15, 16, 19, 21, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34}
    >>> complementary_group((1, 2, 3, 2), network)
    Traceback (most recent call last):
    AssertionError: invalid group

    >>> flow(group, network)
    23
    >>> flow(set(group) | {9}, network)
    26
    >>> flow((1, 2, 3, 2), network)
    Traceback (most recent call last):
    AssertionError: invalid group
    '''


if __name__ == "__main__":
    import doctest
    doctest.testmod()
