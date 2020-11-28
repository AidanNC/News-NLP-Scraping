import re

txt = "https://www.washingtontimes.com/news/2020/nov/28/obama-cia-chief-brennan-condemns-iranian-scientist/"

regex = "washingtontimes\.com/news/2020"

x = re.search(regex,txt)

if x:
    print("yes indeed")
else:
    print("no indeed")