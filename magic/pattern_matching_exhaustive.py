
import re

# search for number like 12-23-34
num = "12-23-34"
reobj = re.compile(r"(\d\d)-(\d\d)-(\d\d)")

# here we are grouping with parenthesis , without parenthesis u can search

mo=reobj.search(num)
print(mo.group(0))
print(mo.group(1))
print(mo.group(2))
print(mo.group(3))
print(mo.groups())

# search batwoman or batman from sentence
# + means atleast one , * means zero or more , ? zero or one

pat1= re.compile(r"bat(wo)?man")
if pat1.search("i am batwoman"):
    print("yes")
else:
    print("no")


# Matching specific repetitions with Curly Brackets {}

pat2 = re.compile(r"(Ha){3}")
if pat2.search("HaHaHa"):
    print("yes found it ",pat2.search("HaHaHa").group())
else:
    print("no")


# Greedy and non-greedy matching
# Python’s regular expressions are greedy by default: in ambiguous situations they will match the longest string possible. The non-greedy version of the curly brackets, which matches the shortest string possible, has the closing curly bracket followed by a question mark.
#
# >>> greedy_ha_regex = re.compile(r'(Ha){3,5}')
#
# >>> mo1 = greedy_ha_regex.search('HaHaHaHaHa')
# >>> mo1.group()
# # 'HaHaHaHaHa'
#
# >>> non_greedy_ha_regex = re.compile(r'(Ha){3,5}?')
# >>> mo2 = non_greedy_ha_regex.search('HaHaHaHaHa')
# >>> mo2.group()
# # 'HaHaHa'


# find all matches
pat3 = re.compile(r"\d-\d")
print(pat3.findall("2-3 4-5"))

# match vowels with full frequency

pat4 = re.compile(r"[aeiouAEIOU]")
print(pat4.findall("abc def xyz uvi mnoo"))

# search  - will return span also

pat5 = re.compile(r"^Hello$")
print(pat5.search("Hello"))

 # >>> newline_regex = re.compile('.*', re.DOTALL) . with \n

# >>> robocop = re.compile(r'robocop', re.I) # it will ignore case.

#substitution method

# >>> names_regex = re.compile(r'Agent \w+')
#
# >>> names_regex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
# # 'CENSORED gave the secret documents to CENSORED.'

pat6 = re.compile(r"spiderman")
print(pat6.sub("hanuman","spiderman is my fav"))













