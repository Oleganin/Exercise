def build_query_string(query):
    return '&'.join((sorted([f'{x}={query[x]}' for x in query])))

if __name__ == '__main__':
    print(build_query_string({'per':10,'page':1}) == 'page=1&per=10')
