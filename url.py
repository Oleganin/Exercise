import urllib.parse

def make(url):
    return urllib.parse.urlparse(url)

def get_scheme(data):
    return data.scheme

def set_scheme(data, scheme):
    new_url = to_string(data._replace(scheme=scheme))
    return make(new_url)

def get_host(data):
    return data.hostname

def set_host(data, host):
    new_url = to_string(data._replace(netloc=host))
    return make(new_url)

def get_path(data):
    return data.path

def set_path(data, path):
    new_url = to_string(data._replace(path=path))
    return make(new_url)

def get_query_param(data, param_name, default = None):
    if not data.query:
        return default
    return urllib.parse.parse_qs(data.query)[param_name]

def set_query_param(data, key, value):
    pass

def to_string(data):
    return urllib.parse.urlunparse(data)

if __name__ == '__main__':
    u = make('https://hexlet.io/community?q=low')
    u = set_scheme(u, 'http')
    print(to_string(u))
    print(get_query_param(u, 'q'))
    '''u = set_query_param(u, 'page', 5)
    print(to_string(u))
    u = set_query_param(u, 'q', 'high')
    print(to_string(u))
    u = set_query_param(u, 'q', None)
    print(to_string(u))'''
