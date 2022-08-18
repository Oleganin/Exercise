def make_user(name, age):
    return {'name':name, 'age':age}

def format_user(d):
    return f'{d["name"]}, {d["age"]}'


phil = make_user('Phyl', 23)
print(type(phil))
print(format_user(phil))
