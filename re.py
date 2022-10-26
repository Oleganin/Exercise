import re

text = 'java \ python ruby1.9 javascript c#'
patern = r'ruby1\..'
need = 'ruby1. and simbol'
result = re.findall(patern, text)
print(f'need find\n"{need}"\nin\n"{text}"\nThe result: "{result}"')
print('-'*40)

text = 'java \ python ruby1.9 11/& javascript c#, 54/f, 55/F'
patern = r'\d\d/[^a-z]'
need = 'two digit "/" and any simbol without "a-z"'
result = re.findall(patern, text)
print(f'need find\n"{need}"\nin\n"{text}"\nThe result: "{result}"')
print('-'*40)

