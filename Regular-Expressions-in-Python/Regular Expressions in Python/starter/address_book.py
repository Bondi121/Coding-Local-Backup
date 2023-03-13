import re

names_file = open("names.txt", encoding="utf-8")
data = names_file.read()
names_file.close()

#print(data)

last_name = r'Love'
first_name = r'Kenneth'


#print(re.match(last_name, data))
#print(re.search(r'Kenneth', data))
#print(re.findall(r'\(?\d{3}\)?-?\s?\d{3}-\d{4}', data))


def first_number(string):
    return(re.search(r'\d',string))

def numbers(count,string):
    string = string
    count = int(count) * "\d"
    integer = r"{}".format(count)
    return re.search(integer,string)

#print(re.findall(r'\w*, \w+', data))


import re

# EXAMPLE:
# >>> find_words(4, "dog, cat, baby, balloon, me")
# ['baby', 'balloon']

def find_words(count, string):
    return re.findall(r'\w{' + str(count) + ',}', string)


import re

# Example:
# >>> find_email("kenneth.love@teamtreehouse.com, @support, ryan@teamtreehouse.com, test+case@example.co.uk")
# ['kenneth@teamtreehouse.com', 'ryan@teamtreehouse.com', 'test@example.co.uk']

def find_emails(email_list):
    a = (re.findall(r'[-\w\d+.]+@[-\w\d.]+', email_list))
    return(a)



#print(re.findall(r'\b[trehous]{9}\b', data, re.I))
#print(re.findall(r'''
#   \b@[-\w\d.]*  # First a word boundary,  an @, and then any number of characters 
#   [^gov\t]+  # Ignore 1+ instances of the letter 'g', 'o' or 'v' and a tab.
#   \b  # Match another word boundary
#''', data, re.VERBOSE|re.I))

#print(re.findall(r"""
#    \b[-\w]+,  # Find a word boundary, 1+ hyphens or characters, and a comma
#    \s #  Find 1 whitespace   
#    [-\w ]+  # 1+ hyphens and characters and explicit spaces
#    [^\t\n]  # Ignore tabs and newines
#""", data, re.X))

line = re.search(r'''
    ^(?P<name>[-\w ]*,\s[-\w ]+)\t  # Last and first names
    (?P<email>[-\w\d.+]+@[-\w\d.]+)\t  # Email
    (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t  # Phone
    (?P<job>[\w\s]+,\s[\w\s.]+)\t?  # Job and company
    (?P<twitter>@[\w\d]+)?$  # Twitter
''', data, re.X|re.M)

#print(line)
#print(line.groupdict())

#names = re.match(r'([\w\s]+), ([\w\s]+)', string)

import re

string = '''Love, Kenneth, kenneth+challenge@teamtreehouse.com, 555-555-5555, @kennethlove
Chalkley, Andrew, andrew@teamtreehouse.co.uk, 555-555-5556, @chalkers
McFarland, Dave, dave.mcfarland@teamtreehouse.com, 555-555-5557, @davemcfarland
Kesten, Joy, joy@teamtreehouse.com, 555-555-5558, @joykesten'''

contacts = re.search(r'''
    (?P<email>[-\w\d.+]+@[-\w\d.]+),\s
    (?P<phone>\d{3}-\d{3}-\d{4}),\s
''',string,re.X|re.M)

twitters = re.search(r'''
    (?P<twitter>@[^t][\w\d]+)
''',string ,re.X|re.M)

line = re.compile(r'''
    ^(?P<name>(?P<last>[-\w ]*),\s(?P<first>[-\w ]+))\t  # Last and first names
    (?P<email>[-\w\d.+]+@[-\w\d.]+)\t  # Email
    (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t  # Phone
    (?P<job>[\w\s]+,\s[\w\s.]+)\t?  # Job and company
    (?P<twitter>@[\w\d]+)?$  # Twitter
''', re.X|re.M)

#print(re.search(line, data).groupdict())
#print(line.search(data).groupdict())

for match in line.finditer(data):
    print('{first} {last} <{email}>'.format(**match.groupdict()))



players = re.match(r'''
        (?P<last_name>^[\w ]+)
        ,\s
        (?P<first_name>[\w ]+)
        :\s
        (?P<score>[\d]+$)
        ''', string, re.M|re.X)

class Player: 
    def __init__(self, first_name, last_name, score):
        self.first_name = first_name
        self.last_name = last_name
        self.score = score