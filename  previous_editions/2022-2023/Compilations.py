# https://dodona.be/en/courses/1659/series/18383/activities/1149379220/


def divide(compilation:str)->tuple:

    if compilation[0].isupper():
        first_part = ''.join(ch for ch in compilation if ch.isupper())

    else:
        first_part = ''.join(ch for ch in compilation if ch.islower())

    second_part = compilation.replace(first_part, '')

    return first_part, second_part



def recombine(sequence:list|tuple)->list:
    divided =[divide(word) for word in sequence]
    length = len(divided)
    return [divided[i%length][1]+divided[(i+1)%length][0] for i in range(length)]

def successors(compilation:str, sequence:list|tuple)->list:
    divided_com = divide(compilation)
    devided_seq = [divide(word) for word in sequence]

    return [first+second for first, second in devided_seq if divided_com[1].lower() == first.lower()]

def intertwine(sequence:list|tuple)->tuple:
    sequence = sorted(sequence, key = str.lower)

    l = int(len(sequence))
    if l%2 != 0 :
        raise AssertionError('invalid sequence')



    first_suc = successors(sequence[0], sequence)
    if len(first_suc)>1:
        raise AssertionError('invalid sequence')
    first_list = [sequence[0]]
    second_list = [first_suc[0]]
    res = (first_list,second_list)
    sequence.remove(sequence[0])
    sequence.remove(first_suc[0])
    while sequence:
        if len(successors(res[1][-1], sequence))>1:
            raise AssertionError('invalid sequence')
        res[0].append(successors(res[1][-1],sequence)[0])
        sequence.remove(successors(res[1][-1],sequence)[0])
        if len(successors(res[0][-1], sequence))>1:
            raise AssertionError('invalid sequence')
        res[1].append(successors(res[0][-1],sequence)[0])
        sequence.remove(successors(res[0][-1], sequence)[0])


    return res







def main_test():
    '''
    >>> divide('WOODSman')
    ('WOODS', 'man')
    >>> divide('billION')
    ('bill', 'ION')

    >>> recombine(['WOODSman', 'AGEing', 'RAINbow', 'MENtal', 'LOWdown', 'PLAYback'])
    ['manAGE', 'ingRAIN', 'bowMEN', 'talLOW', 'downPLAY', 'backWOODS']
    >>> recombine(('billION', 'isingLASS', 'oedEMA', 'nationWIDE', 'screenPLAY'))
    ['IONising', 'LASSoed', 'EMAnation', 'WIDEscreen', 'PLAYbill']

    >>> successors('WOODSman', ['backWOODS', 'manAGE', 'LOWdown', 'ingRAIN', 'AGEing', 'talLOW', 'MENtal', 'bowMEN', 'RAINbow', 'downPLAY', 'PLAYback', 'WOODSman'])
    ['manAGE']
    >>> successors('boardWALK', ('nationWIDE', 'PLAYbill', 'EMAnation', 'IONising', 'isingLASS', 'WIDEscreen', 'oedEMA', 'billION', 'LASSoed', 'screenPLAY'))
    []
    >>> successors('rocketMAN', ['manGROVE', 'roMANTIC', 'MANUscript', 'MANkind', 'HUman', 'MANtra', 'KLEPTOmania'])
    ['manGROVE', 'MANkind', 'MANtra']

    >>> intertwine(['backWOODS', 'manAGE', 'LOWdown', 'ingRAIN', 'AGEing', 'talLOW', 'MENtal', 'bowMEN', 'RAINbow', 'downPLAY', 'PLAYback', 'WOODSman'])
    (['AGEing', 'RAINbow', 'MENtal', 'LOWdown', 'PLAYback', 'WOODSman'], ['ingRAIN', 'bowMEN', 'talLOW', 'downPLAY', 'backWOODS', 'manAGE'])
    >>> intertwine(('nationWIDE', 'PLAYbill', 'EMAnation', 'IONising', 'isingLASS', 'WIDEscreen', 'oedEMA', 'billION', 'LASSoed', 'screenPLAY'))
    (['billION', 'isingLASS', 'oedEMA', 'nationWIDE', 'screenPLAY'], ['IONising', 'LASSoed', 'EMAnation', 'WIDEscreen', 'PLAYbill'])
    '''


if __name__ == '__main__':
    import doctest
    doctest.testmod()