import re

def find(patern, args, commit=''):
    if commit:
        print(f'Need find\n"{commit}"')
    for text in args:
        res = re.findall(patern, text)
        print(f'In "{text}". ', end='') 
        if res:
              print(f'Finded: "{res}"')
        else:
            print('Nothing find')
    print('-'*40)


find(r'ruby1\..',
     ['java \ python ruby1.9 javascript c#'],
     'ruby1. and some simbol'
     )
find(r'\d\d/[^a-z]',
     ['java \ python ruby1.9 11/& javascript c#, 54/f, 55/F'],
     'two digit "/" and something simbol without "a-z"')
find(r'^support@hexlet\.io$',
     ['something here support@hexlet.io',
      'support@hexlet.io something here',
      'support@hexlet.io'],
     'Find only \'support@hexlet.io\''
     )
find(r'(o|t)(n|w|hre)(e|o)',
     ['one','two','three', 'four','five',
      'one, two', 'one two three']
     )
