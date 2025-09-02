# regular expression
# Search the string to see if it starts with "The" and ends with "Spain":
import re
s =  "The rain in Spain"

# search(): retrun first accurance
res = re.search('^The .* Spain$', s)
if res:
    print('yes', res)
r2 = re.search('a', s)
print(r2.start(), r2.end())

# findall: return all the matched value
r1 = re.findall('a', s)
# print(r1)<re.Match object; span=(0, 17), match='The rain in Spain'>
r2.start(), r2.end()

# match: is an obj contaning result about the search
# <re.Match object; span=(0, 17), match='The rain in Spain'> that contain information about the result

# sub(): replace to any specific character
rep = re.sub('\s', "_", s, 2)
print(rep)

# re for email validation
email = "ravinabirla66@gmil.com"
ans = re.match('^[a-z0-9]+\@[a-z]+\.[a-z]{2,}$', email)
print(ans)