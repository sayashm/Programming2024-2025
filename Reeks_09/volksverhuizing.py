# https://dodona.be/nl/courses/4157/series/46298/activities/1495781151


def property(location:str, index: int)->dict:

    with open(location, 'r', encoding='utf-8') as reader:
        lines = reader.readlines()

    return {line.rstrip().split('\t')[0]: float(line.rstrip().split('\t')[index].replace(',',''))  for line in lines}


def ascending(country_prop: dict) -> list:
    return sorted(country_prop, key=country_prop.get)


def staycation(d_from: dict, d_to: dict)->set:
    return {country1 for country1, country2 in zip(ascending(d_from),ascending(d_to)) if country1==country2}


def migration(d_from: dict, d_to: dict)->dict:
    return dict(zip(ascending(d_from), ascending(d_to)))


def circle(name:str, D:dict)->list:
    first_name = name
    if name not in D:
        return [name]

    l = [name]
    while True:
        if first_name == D[name]:
            break
        l.append(D[name])
        name = D[name]

    return l

def circles(countries : dict)->int:
    return len({frozenset(circle(countries[k], countries)) for k in countries})



def main_tests():
    '''
    >>> area = property('europe.txt', 3)
    >>> area['Belgium']
    30689.0
    >>> area['Italy']
    301338.0
    >>> area['United Kingdom']
    242495.0
    >>> ascending(area)
    ['Vatican City', 'Monaco', 'San Marino', 'Liechtenstein', 'Malta', 'Andorra', 'Luxembourg', 'Cyprus', 'Kosovo', 'Montenegro', 'Slovenia', 'North Macedonia', 'Albania', 'Belgium', 'Moldova', 'Switzerland', 'Netherlands', 'Denmark', 'Estonia', 'Slovakia', 'Bosnia and Herzegovina', 'Croatia', 'Latvia', 'Lithuania', 'Ireland', 'Czech Republic', 'Austria', 'Portugal', 'Hungary', 'Serbia', 'Iceland', 'Bulgaria', 'Greece', 'Belarus', 'Romania', 'United Kingdom', 'Italy', 'Poland', 'Finland', 'Germany', 'Norway', 'Sweden', 'Spain', 'France', 'Ukraine', 'Russia']


    >>> population = property('europe.txt', 4)
    >>> population['Belgium']
    11515793.0
    >>> population['Italy']
    60404355.0
    >>> population['United Kingdom']
    66040229.0
    >>> ascending(population)
    ['Vatican City', 'San Marino', 'Liechtenstein', 'Monaco', 'Andorra', 'Iceland', 'Malta', 'Luxembourg', 'Montenegro', 'Cyprus', 'Estonia', 'Kosovo', 'Latvia', 'Slovenia', 'North Macedonia', 'Moldova', 'Lithuania', 'Albania', 'Bosnia and Herzegovina', 'Croatia', 'Ireland', 'Norway', 'Slovakia', 'Finland', 'Denmark', 'Serbia', 'Bulgaria', 'Switzerland', 'Austria', 'Belarus', 'Hungary', 'Sweden', 'Portugal', 'Czech Republic', 'Greece', 'Belgium', 'Netherlands', 'Romania', 'Poland', 'Ukraine', 'Spain', 'Italy', 'United Kingdom', 'France', 'Germany', 'Russia']

    >>> staycation(population, area) == {'France', 'Russia', 'Vatican City'}
    True

    >>> destination = migration(population, area)
    >>> destination['Belgium']
    'United Kingdom'
    >>> destination['Italy']
    'Sweden'
    >>> destination['United Kingdom']
    'Spain'
    >>> destination['Belarus']
    'Serbia'
    >>> destination['Serbia']
    'Czech Republic'
    >>> destination['Czech Republic']
    'Belarus'

    >>> circle('Albania', destination)
    ['Albania', 'Denmark', 'Ireland', 'Bosnia and Herzegovina', 'Estonia', 'Slovenia', 'Belgium', 'United Kingdom', 'Spain', 'Norway', 'Croatia', 'Slovakia', 'Latvia']
    >>> circle('Andorra', destination)
    ['Andorra', 'Malta', 'Luxembourg', 'Cyprus', 'Montenegro', 'Kosovo', 'North Macedonia', 'Moldova', 'Switzerland', 'Portugal', 'Greece', 'Romania', 'Poland', 'Finland', 'Lithuania', 'Netherlands', 'Italy', 'Sweden', 'Bulgaria', 'Austria', 'Hungary', 'Iceland']
    >>> circle('Belarus', destination)
    ['Belarus', 'Serbia', 'Czech Republic']
    >>> circle('France', destination)
    ['France']
    >>> circle('Germany', destination)
    ['Germany', 'Ukraine']
    >>> circle('Liechtenstein', destination)
    ['Liechtenstein', 'San Marino', 'Monaco']
    >>> circle('Russia', destination)
    ['Russia']
    >>> circle('Vatican City', destination)
    ['Vatican City']

    >>> circles(destination)
    8
    '''


if __name__ == "__main__":
    import doctest
    doctest.testmod()