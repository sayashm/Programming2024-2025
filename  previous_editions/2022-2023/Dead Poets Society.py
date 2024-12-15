# https://dodona.be/en/courses/1659/series/18382/activities/1506545778/
import datetime

def read_dates(location: str, registry: int) -> dict:
    lines = {}
    with open(location, 'r', encoding='utf-8') as reader:
        for line in reader:
            element = line.strip().split(',')
            if element[registry] != '':
                date_str = element[registry]
                # Assuming the date is in YYYY-MM-DD format.
                year, month, day = date_str.split('-')
                date_obj = datetime.date(int(year), int(month), int(day))
                lines[element[0]] = date_obj
    return lines


def lifespan(name:str, born:dict, died:dict)->list:
    if name not in born or name not in died:
        raise AssertionError('missing information')
    return list(range(born[name].year, died[name].year + 1))


def alive(birth_date:dict, death_date:dict)->dict:
    res = {}
    for name in birth_date:
        try:
            for year in lifespan(name,birth_date,death_date):
                if year in res:
                    res[year].add(name)
                else:
                    res[year] = {name}
        except:
            pass
    return res



def wonder_years(alive_dict:dict):
    max_alive = max((len(names) for names in alive_dict.values()), default=0)
    return {year for year, names in alive_dict.items() if len(names) == max_alive}


def summarized(collection:list|set|tuple)->str:
    if not collection:
        return ''
    sorted_years = sorted(collection)
    ranges = []
    start = prev = sorted_years[0]

    for year in sorted_years[1:]:
        if year != prev + 1:
            # Close off previous range
            ranges.append(str(start) if start == prev else f"{start}-{prev}")
            start = year
        prev = year

    # Append the final range
    ranges.append(str(start) if start == prev else f"{start}-{prev}")

    return ', '.join(ranges)


def main_test():
    '''
    >>> born = read_dates('poets.txt', 1)
    >>> born['Emily Brontë']
    datetime.date(1818, 7, 30)
    >>> born['Walt Whitman']
    datetime.date(1819, 5, 31)
    >>> born['Phillis Wheatley']
    Traceback (most recent call last):
    KeyError: 'Phillis Wheatley'

    >>> died = read_dates('poets.txt', 2)
    >>> died['Emily Brontë']
    datetime.date(1848, 12, 19)
    >>> died['Walt Whitman']
    Traceback (most recent call last):
    KeyError: 'Walt Whitman'
    >>> died['Phillis Wheatley']
    datetime.date(1784, 12, 5)

    >>> lifespan('Emily Brontë', born, died)
    [1818, 1819, 1820, 1821, 1822, 1823, 1824, 1825, 1826, 1827, 1828, 1829, 1830, 1831, 1832, 1833, 1834, 1835, 1836, 1837, 1838, 1839, 1840, 1841, 1842, 1843, 1844, 1845, 1846, 1847, 1848]
    >>> lifespan('Walt Whitman', born, died)
    Traceback (most recent call last):
    AssertionError: missing information
    >>> lifespan('Phillis Wheatley', born, died)
    Traceback (most recent call last):
    AssertionError: missing information

    >>> poets = alive(born, died)
    >>> poets[1798] == {'John Keats', 'Percy Bysshe Shelley'}
    True
    >>> poets[1895] == {'Guillaume Apollinaire', 'Rupert Brooke', 'Wilfred Owen'}
    True
    >>> poets[1952] == {'Sylvia Plath'}
    True


    >>> wonder_years(poets) == {1818, 1819, 1820, 1821, 1893, 1894, 1895, 1896, 1897, 1898, 1899, 1900, 1901, 1902, 1903, 1904, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915}
    True
    >>> wonder_years(poets)
    {1818, 1819, 1820, 1821, 1893, 1894, 1895, 1896, 1897, 1898, 1899, 1900, 1901, 1902, 1903, 1904, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915}
    >>> summarized({2001, 2002, 2003, 2004, 2012, 2015, 2018, 2019, 2020, 2022})
    '2001-2004, 2012, 2015, 2018-2020, 2022'
    >>> summarized(lifespan('Emily Brontë', born, died))
    '1818-1848'
    >>> summarized(wonder_years(poets))
    '1818-1821, 1893-1915'
    '''

if __name__ == '__main__':
    import doctest
    doctest.testmod()