# -----Regular Expressions-----
""" Refer RegEx.txt for more information """
import re

# The search() Function
txt = "The rain in Spain"
x = re.search(r"\s", txt)
print("The first white-space character is located in position:", x.start())
x = re.search("Portugal", txt)
print(x)

regex = r"([a-zA-Z]+) (\d+)"
match = re.search(regex, "I was born on June 24")
if match is not None:
    print("Match at index %s, %s" % (match.start(), match.end()))
    print("Full match: %s" % (match.group()))
    print("Month: %s" % (match.group(1)))
    print("Day: %s" % (match.group(2)))
else:
    print("The regex pattern does not match.")
print("")


# The match() Function
def findMonthAndDate(string):
    regex1 = r"([a-zA-Z]+) (\d+)"
    match1 = re.match(regex1, string)

    if match1 is None:
        print("Not a valid date")
        return

    print("Given Data: %s" % (match.group()))
    print("Month: %s" % (match.group(1)))
    print("Day: %s" % (match.group(2)))


findMonthAndDate("Jun 24")
findMonthAndDate("I was born on June 24")
print("")

# The split() Function
txt = "The rain in Spain"
x = re.split(r"\s", txt)
print(x)
x = re.split(r"\s", txt, 1)
print(x)

print(re.split(r'\W+', 'Words, words , Words'))
print(re.split(r'\W+', "Word's words Words"))
print(re.split(r'\W+', 'On 12th Jan 2016, at 11:02 AM'))
print(re.split(r'\d+', 'On 12th Jan 2016, at 11:02 AM'))
print(re.split(r'\d+', 'On 12th Jan 2016, at 11:02 AM', 1))
print(re.split('[a-f]+', 'Aey, Boy oh boy, come here', flags=re.IGNORECASE))
print(re.split('[a-f]+', 'Aey, Boy oh boy, come here'))
print("")

# The sub() & subn() Function
txt = "The rain in Spain"
x = re.sub(r"\s", "9", txt)
print(x)
x = re.sub(r"\s", "9", txt, 2)
print(x)

print(re.sub('ub', '~*', 'Subject has Uber booked already', flags=re.IGNORECASE))
print(re.sub('ub', '~*', 'Subject has Uber booked already'))
print(re.sub('ub', '~*', 'Subject has Uber booked already', count=1, flags=re.IGNORECASE))
print(re.sub(r'\sAND\s', ' & ', 'Baked Beans And Spam', flags=re.IGNORECASE))
print(re.subn('ub', '~*', 'Subject has Uber booked already'))
print(re.subn('ub', '~*', 'Subject has Uber booked already', flags=re.IGNORECASE))
print("")

# The findall() Function
string = """Hello my Number is +91 123456789 and my friend's number is +91 987654321"""
regex = r'91 \d+'
match = re.findall(regex, string)
print(match)
print("")

# The compile() Function
p = re.compile('[a-e]')
print(p.findall("Aye, said Mr. Gibson Stark"))

p = re.compile(r'\d')
print(p.findall("I went to him at 11 A.M. on 4th July 1886"))

p = re.compile(r'\d+')
print(p.findall("I went to him at 11 A.M. on 4th July 1886"))

p = re.compile(r'\w')
print(p.findall("He said * in some_lang."))

p = re.compile(r'\w+')
print(p.findall("I went to him at 11 A.M., he said *** in some_language."))

p = re.compile(r'\W')
print(p.findall("he said *** in some_language."))

p = re.compile('ab*')
print(p.findall("ababbaabbb"))
print("")


# The finditer() Function
def match_itr(regex, my_str):
    pattern = re.compile(regex)
    matches = pattern.finditer(my_str)
    for match in matches:
        print(match)
    print("")


myStr = '''Tata Limited
    Dr. David Landsman, executive director
    18, Grosvenor Place
    London SW1X 7HSc
    Phone: +44 (20) 7235 8281
    Fax: +44 (20) 7235 8727
    Email: tata@tata.co.uk
    Website: www.europe.tata.com
    Directions: View map

    Tata Sons, North America
    1700 North Moore St, Suite 1520
    Arlington, VA 22209-1911
    USA
    Phone: +1 (703) 243 9787
    Fax: +1 (703) 243 9791
    66-66
    455-4545
    Email: northamerica@tata.com 
    Website: www.northamerica.tata.com
    Directions: View map fass
    harry bhai lekin
    bahut hi badia aadmi haiaiinaiiiiiiiiiiii'''

match_itr(r'fass', myStr)
match_itr(r'.adm', myStr)
match_itr(r'^Tata', myStr)
match_itr(r'iin$', myStr)
match_itr(r'ai*', myStr)
match_itr(r'ai+', myStr)
match_itr(r'ai{2}', myStr)
match_itr(r'(ai){1}', myStr)
match_itr(r'ai{1}|Fax', myStr)
match_itr(r'Fax\b', myStr)
match_itr(r'27\b', myStr)
match_itr(r'\d{5}-\d{4}', myStr)
