"""
Using names.txt (right click and 'Save Link/Target As...'),
a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order.
Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order,
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""
#  Build alpha dict
import string

alpha = {}
i = 1
for char in string.ascii_uppercase:
    alpha[char] = i
    i += 1

#  Import text into file, with each name as a list item
with open('p022_names.txt') as f:
    names = f.read().replace('\"', '')
    names = sorted(names.split(','))
print(names)
#  Iterate over each name
total = 0
for name in names:
    #  Get sum of character scores
    name_total = 0
    for char in name:
        name_total += alpha[char]
    #  Return that, multiplied by name.index()
    total += name_total * (names.index(name) + 1)

print(total)
