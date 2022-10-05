import urllib.parse

def make(url):
    return urllib.parse.urlparse(url)

def get_scheme(data):
    return data.scheme

def set_scheme(data, scheme):
    return data._replace(scheme=scheme)

def get_host(data):
    return data.hostname

def set_host(data, host):
    return data._replace(netloc=host)

def get_path(data):
    return data.path

def set_path(data, path):
    return data._replace(path=path)

def get_query_param(data, param_name, default = None):
    if not data.query:
        return default
    return urllib.parse.parse_qs(data.query)[param_name][-1]

def set_query_param(data, key, value):
    new_query_dict = urllib.parse.parse_qs(data.query)
    if value:
        new_query_dict.update({key: value})
    else:
        del new_query_dict[key]
    new_query = urllib.parse.urlencode(new_query_dict, doseq=True)
    return data._replace(query=new_query)
    

def to_string(data):
    return urllib.parse.urlunparse(data)

if __name__ == '__main__':
    u = make('https://hexlet.io/community?q=low')
    u = set_scheme(u, 'http')
    print(to_string(u))
    u = set_path(u, '/404')
    print(to_string(u))
    print(get_query_param(u, 'q'))
    u = set_query_param(u, 'page', 5)
    print(to_string(u))
    u = set_query_param(u, 'q', 'high')
    print(to_string(u))
    u = set_query_param(u, 'q', None)
    print(to_string(u))
