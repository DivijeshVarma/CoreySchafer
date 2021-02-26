# Regular Expressions allow us to search for and
# match specific patterns of text. to use RE we need to
# import re module
# raw string (r) tells python not to handle back slash(\) in
# any special way like tabs, new lines. because we want RE to
# interpret the strings we passing in not python to do anything
# first, to write patterns we use re.compile method, compile
# method allows to seperate our patterns into variable and make
# it reusable for multiple searches

import re

print('\ttab')
print(r'\ttab')


text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'

pattern = re.compile(r'abc')
# pattern = re.compile(r'\.')

# finditer method returns iterator contains all of matches.
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

print(text_to_search[1:4])


# pattern = re.compile(r'^Start')
pattern = re.compile(r'end$')
matches2 = pattern.finditer(sentence)

for match in matches2:
    print(match)

pattern3 = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
# matches3 = pattern3.finditer(text_to_search)

# for match in matches3:
    # print(match)

#########################

with open('DataRE', 'r') as f:
    content = f.read()

    matches = pattern3.finditer(content)
    for match in matches:
        print(match)