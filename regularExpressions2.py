import re

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
900*555*1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
cat
mat
bat
'''

# pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
# use quantifier to match multiple characters at a time
# pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
# to match o or 1 (?)
# pattern = re.compile(r'Mr\.?\s[A-Z]')
# pattern = re.compile(r'M[rs]\.?\s[A-Z]\w+')
# pattern = re.compile(r'Mr\.?\s[A-Z]\w*')
# matches = pattern.finditer(text_to_search)

# for match in matches:
#     print(match)

# groups allow to match several different patterns

pattern2 = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')
matches2 = pattern2.finditer(text_to_search)

for match in matches2:
    print(match)

mails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''
# pattern3 = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)')
pattern3 = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
matches3 = pattern3.finditer(mails)

for match in matches3:
    print(match)

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''
# use groups to capture info from url
# 3 different groups www, domain, top level domain
pattern4 = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
# matches4 = pattern4.finditer(urls)
# we want to replace urls with domain name and top level
# after matching pattern to substitute group 2 and group 3
# after matches in urls.
subbed_urls = pattern4.sub(r'\2\3', urls)

print(subbed_urls)

# for match in subbed_urls:
    # group zero is entire match
    # print(match.group(0))
    # print(match)
