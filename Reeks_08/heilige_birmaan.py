# https://dodona.be/nl/courses/4157/series/46297/activities/463104583


def color(genotype:str)->str:
    '''
    >>> color('CcDd')
    'seal'
    >>> color('ccdd')
    'lilac'
    '''

    Dgene = ['DD', 'Dd', 'dD', 'dd']
    Cgene = ['CC', 'Cc', 'cC', 'cc']
    colors = [
        ['seal','seal','seal','blue'],
        ['seal','seal','seal','blue'],
        ['seal','seal','seal','blue'],
        ['chocolate','chocolate','chocolate','lilac']
     ]
    return colors[Cgene.index(genotype[:2])][Dgene.index(genotype[2:])]

def combinations(genotype:str)->list:
    '''
    >>> combinations('CcDd')
    ['CD', 'Cd', 'cD', 'cd']
    >>> combinations('ccdd')
    ['cd', 'cd', 'cd', 'cd']
    '''

    return [i+j for i in genotype[:2] for j in genotype[2:]]

def punnett(male_genotypes:str, female_genotypes :str, pprint:bool = False):
    '''
    >>> punnett('CcDd', 'CcDd')
    [['CCDD', 'CCDd', 'CcDD', 'CcDd'], ['CCdD', 'CCdd', 'CcdD', 'Ccdd'], ['cCDD', 'cCDd', 'ccDD', 'ccDd'], ['cCdD', 'cCdd', 'ccdD', 'ccdd']]
    >>> print(punnett('CcDd', 'CcDd', pprint=True))
    CCDD CCDd CcDD CcDd
    CCdD CCdd CcdD Ccdd
    cCDD cCDd ccDD ccDd
    cCdD cCdd ccdD ccdd
    >>> print(punnett('cCDd', 'CcdD', pprint=True))
    cCDd cCDD ccDd ccDD
    cCdd cCdD ccdd ccdD
    CCDd CCDD CcDd CcDD
    CCdd CCdD Ccdd CcdD
    '''

    firstMalegenotype = male_genotypes[:2]
    secondMalegenotype = male_genotypes[2:]
    firstFemalegenotype = female_genotypes[:2]
    secondfemalegenotype = female_genotypes[2:]


    out = [i+j+k+l for i in firstMalegenotype for k in secondMalegenotype for j in firstFemalegenotype  for l in secondfemalegenotype]
    out = [out[i:i + 4] for i in range(0, len(out), 4)]
    if not pprint:
        return out
    else:
        return '\n'.join([' '.join(row) for row in out])


def color_distribution(male_genotypes:str, female_genotypes :str)->dict:
    '''
    >>> color_distribution('CcDd', 'CcDd')
    {'blue': 3, 'seal': 9, 'lilac': 1, 'chocolate': 3}
    >>> color_distribution('cCDD', 'cCDD')
    {'seal': 12, 'chocolate': 4}
    >>> color_distribution('ccDD', 'ccDD')
    {'chocolate': 16}
    >>> color_distribution('ccdd', 'CcDd')
    {'blue': 4, 'lilac': 4, 'seal': 4, 'chocolate': 4}
    '''

    geno_list = punnett(male_genotypes, female_genotypes)

    color_list = [color(j) for i in geno_list for j in i]
    color_dict = {}
    for i in color_list:
        if i not in color_dict:
            color_dict[i] = 1
        else:
            color_dict[i] += 1
    return color_dict