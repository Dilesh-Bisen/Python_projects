# without regular expression
# tweet = "Hey there! Call me @ gpm # Pune # cwc2023"

# hashtags = [w for w in tweet.split() if w.startswith("#")]
# print(hashtags)

# callouts = [w for w in tweet.split() if w.startswith("@")]
# print(callouts)


# use of regular expression

import re

s = re.search(r"rat", "cat and rat can't be good friends")
print(s)
print(s.group())
a = re.search(r"dilesh", "cat and rat can't be good friends")
print(a)
# print(a.group()) # attribute error


# Meta characters :

# search pattern at the start of string
s = re.search(r".", "cat and rat can't be good friends")
print(s)
a = re.search(r".od", "cat and rat can't be good friends")
print(a)

# search pattern at the start of string
s = re.search(r"^cat", "cat and rat can't be good friends")
print(s)
a = re.search(r"^good", "cat and rat can't be good friends")
print(a)

# search pattern at the end of string
s = re.search(r"$cat", "cat and rat can't be good friends")
print(s)
a = re.search(r"$good", "cat and rat can't be good friends")
print(a)

