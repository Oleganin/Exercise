def find_where(list_elements, dict_of_element):
    k = len(dict_of_element)
    for element in list_elements:
        i=0
        for paramtr in dict_of_element:
            if element[paramtr] == dict_of_element[paramtr]:
                i+=1
        if i==k:
            return element
    else:
        return None
    
if __name__ == '__main__':
    books = [
        dict(title = 'Book of Fooos', author = 'Foo', year = 1111),
        dict(title = 'Cymbeline', author = 'Shakespeare', year = 1611),
        dict(title = 'The Tempest', author = 'Shakespeare', year = 1611),
        dict(title = 'Book of Fooos Barrrs', author = 'FooBar', year = 2222),
        dict(title = 'Still fooooeng', author = 'FooBar', year = 333),
        dict(title = 'Happy Foo', author = 'FooBar', year = 4444)
        ]

    print(find_where(books, {'author': 'Shakespeare',  'year': 1611}))
    print(find_where(books, {'author': 'Shakespeare',  'year': 1621}))
    print(find_where(books, {'title': 'The Tempest',  'year': 1611}))
