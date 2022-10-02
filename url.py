import urllib.parse

def make(url):
    return urllib.parse.urlparse(url)

def get_scheme(data):
    pass

def set_schem(data, scheme):
    pass

def get_host(data):
    pass

def set_host(data, host):
    pass

def get_path(data):
    pass

def set_path(data, path):
    pass

def get_query_rapam(dat, param_name, default = None):
    pass

def set_query_param(data, key, value):
    pass

def to_string(data):
    return urllib.parse.urlunparse(data)

if __name__ == '__main__':
    u = make('https://hexlet.io/community?q=low')
    u = set_scheme(u, 'http')
    print(to_string(u))
    print(get_query_aram(u, 'q'))
    u = set_query_param(u, 'page', 5)
    print(to_string(u))
    u = set_query_param(u, 'q', 'high')
    print(to_string(u))
    u = set_query_param(u, 'q', None)
    print(to_string(u))
