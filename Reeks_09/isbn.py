# https://dodona.be/nl/courses/4157/series/46298/activities/2055708402

def isISBN13(code: str):
    if not isinstance(code, str) or len(code) != 13:
        return False
    try:
        o = sum(int(code[i]) for i in range(0, 12, 2))
        e = sum(int(code[i]) for i in range(1, 12, 2))
        X13 = (10 - (o + 3 * e) % 10) % 10
        return X13 == int(code[-1])
    except:
        return False

def display_book_info(isbn:str):
    '''
    >>> display_book_info('9780136110675')
    Title: The Practice of Computing using Python
    Authors: William F Punch, Richard Enbody
    Publisher: Addison Wesley
    >>> display_book_info('9780136110678')
    Wrong ISBN-13 code
    '''

    if isISBN13(isbn):
        from urllib.request import urlopen
        import xml.etree.ElementTree as ET

        url = 'https://pythia.ugent.be/pythia-share/exercises/isbn9/books.php?isbn='+isbn
        response = urlopen(url).read().decode('utf-8')
        root = ET.fromstring(response)

        title = root.find('.//BookData/Title').text
        authors = root.find(".//BookData/AuthorsText").text
        authors_list = ', '.join(author.strip() for author in authors.split(",") if author.strip())
        publisher = root.find(".//BookData/PublisherText").text

        print("Title:", title)
        print("Authors:", authors_list)
        print("Publisher:", publisher)

    else:
        print('Wrong ISBN-13 code')
