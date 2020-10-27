import requests
from bs4 import BeautifulSoup
import re

#this gets the html content of whatever webpage you want
page = requests.get('https://www.foxnews.com/politics/mcconnell-urges-white-house-not-to-make-coronavirus-deal-with-pelosi')
contents = page.content

all_urls = []
bad_urls = []

regex = "/article/us"
url = 'https://www.reuters.com/article/us-usa-election-biden-unions/two-largest-u-s-airline-flight-attendant-unions-endorse-biden-idUSKBN27C2VY'
depth = 0
def link_stem_finder(url, regex, depth, add_link = True):
    #make sure that this url is accounted for
    if add_link:
        all_urls.append(url)
    print(len(all_urls))
    if depth > 2 or len(all_urls) > 1000:
        return
    page = requests.get(url)
    contents = page.content

    soup = BeautifulSoup(contents, 'html.parser')

    links = soup.findAll('a')
    for link in links:
        if link.has_attr('href') and re.search(regex,link['href']):
            if link['href'] not in all_urls and link['href'] not in bad_urls:
                try:
                    link_stem_finder(link['href'],regex, depth+1)
                except:
                    bad_urls.append(link['href'])

def custom_reuters():
    #reters articles don't really link to each other, so the recursive approach doesn't work, lets try this
    regex = "/article/us"
    for i in range(1,1000):
        url = 'https://www.reuters.com/news/archive/domesticnews?page=' + str(i)
        page = requests.get(url)
        contents = page.content

        soup = BeautifulSoup(contents, 'html.parser')
        links = soup.findAll('div',{"class": 'story-content'})
        temp_links = []
        for link in links:
            temp_links += link.findAll('a')
        links = temp_links
        for link in links:
            if link.has_attr('href') and re.search(regex,link['href']):
                #print("page: " + str(i))
                #print(link['href'])
                if link['href'] not in all_urls:
                    all_urls.append(link['href'])
                    print(len(all_urls))
        if len(all_urls) > 1000:
            return



custom_reuters()
#reuters_one_page()

#link_stem_finder(url,regex,depth)
if True:
    for url in all_urls:
        print(url)
        print()
print(len(all_urls))

if False:
    file = open('website_urls/reuters_urls.txt','w')
    for url in all_urls:
        file.write('https://www.reuters.com' + url + '\n')
