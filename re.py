import re

def find(patern, args, commit=''):
    res = re.compile(patern)
    if commit:
        print('Need find'.center(80))
        print(f'"{commit}"'.center(80)+'\n')
    for text in args:
        tmp = transform(res.finditer(text))
        print(f'In "{text}". ') 
        if tmp:
              print(f'\tFinded: "{tmp}"')
        else:
            print('\tNothing find')
    print('-'*80)

def transform(args):
    elements = map(lambda x: x.group(), args)
    res = ', '.join(elements)
    return res
    
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
      'one, two', 'one two three'],
     'Regular expression for word: "one", "two", "three"'
     )
find(r'\w+@.{3,}\..{2,5}$',
     ['info@helxet.io','Oleganin@gmail.com','Olegik_dnepr@mail.ru',
      'Olegik_dnepr@mail.remember','Olegik_dnepr@m.ru',
      'Olegik_dnepr@mail.r',
      'Hello, my email is : info@helxet.io, Oleganin@gmail.com'],
     'Regular expression find email'
     )
find(r'\(.+\)',
     ['()','decart (0,2),(4,4)','it impossible (never)',
      '(_)(-)(.)','Olegik_dnepr@m.ru'],
     'Find "(" least one simbol ")"'
     )
find(r'(?P<group1>[a-z]{3})\:(?P=group1)',
     ['aaa:fff','is bad:bad good,(4,4)','aa:. aaa:.dfsg gih:fit, boy:boy'
      ],
     'Find three char "a-z" ":" and again three char'
     )
find(r'80\:(?=[^a-z]+)',
     ['80:8080, 80:!@#$','80:','80','80:d123f',
      ],
     'Find 80: any symbol without a-z'
     )
