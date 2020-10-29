import re

txt = "https://www.politico.com/news/2020/10/26/in-wisconsin-ruling-supreme-court-foreshadows-election-night-cliffhanger-432725"

regex = "^https://www\.politico\.com/news/.*2020/"

x = re.search(regex,txt)

if x:
    print("yes indeed")
else:
    print("no indeed")