import re

text = 'aaa(gdopn12)bbb'
text = re.sub('((?<=\().*(?=\)))|([()])', '', text)
print(text)