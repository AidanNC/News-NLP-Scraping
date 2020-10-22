import requests
from bs4 import BeautifulSoup

#this gets the html content of whatever webpage you want
page = requests.get('https://www.foxnews.com/politics/mcconnell-urges-white-house-not-to-make-coronavirus-deal-with-pelosi')
contents = page.content

all_urls = []

stem = 'https://www.foxnews.com/politics'
url = 'https://www.foxnews.com/politics/mcconnell-urges-white-house-not-to-make-coronavirus-deal-with-pelosi'
depth = 0
def link_stem_finder(url, stem, depth):
    if depth > 25 or len(all_urls) > 1000:
        return
    page = requests.get(url)
    contents = page.content

    soup = BeautifulSoup(contents, 'html.parser')

    links = soup.findAll('a')

    
    for link in links:
        if link.has_attr('href') and len(link['href']) > len(stem) and link['href'][:len(stem)] == stem:
            if link['href'] not in all_urls:
                all_urls.append(link['href'])
                link_stem_finder(link['href'],stem, depth+1)

link_stem_finder(url,stem,depth)

print(len(all_urls))

file = open('fox_urls.txt','w')
for url in all_urls:
    file.write(url + '\n')