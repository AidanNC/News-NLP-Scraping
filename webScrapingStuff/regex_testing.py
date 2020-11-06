import re

txt = "https://www.usatoday.com/story/news/politics/2020/10/28/president-donald-trump-anthony-fauci-timeline-relationship-coronavirus-pandemic/3718797001/"

regex = "www\.usatoday\.com/story/.*politics/"

x = re.search(regex,txt)

if x:
    print("yes indeed")
else:
    print("no indeed")