import re

txt = "https://thehill.com/policy/transportation/aviation"

regex = "/policy.*-.*"

x = re.search(regex,txt)

if x:
    print("yes indeed")
else:
    print("no indeed")