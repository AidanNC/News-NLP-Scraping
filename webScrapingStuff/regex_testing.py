import re

txt = "https://www.oann.com/president-trumps-must-read-article-outlines-bidens-peculiar-election-performance/"

regex = "oann.com/.*-"

x = re.search(regex,txt)

if x:
    print("yes indeed")
else:
    print("no indeed")