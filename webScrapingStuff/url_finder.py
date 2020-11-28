import requests
from bs4 import BeautifulSoup
import re

#this gets the html content of whatever webpage you want
page = requests.get('https://www.foxnews.com/politics/mcconnell-urges-white-house-not-to-make-coronavirus-deal-with-pelosi')
contents = page.content

all_urls = []
bad_urls = []

#regex = "www\.latimes\.com/politics/story"
regex = "/policy"
url = 'https://thehill.com/policy/transportation/527581-airlines-set-sights-on-digital-passports-for-covid-19-vaccine?utm_source=thehill&utm_medium=widgets&utm_campaign=es_recommended_content'
depth = 0
def link_stem_finder(url, regex, depth, add_link = True):
    #make sure that this url is accounted for
    if add_link:
        all_urls.append(url)
    print(len(all_urls))
    if depth > 100 or len(all_urls) > 2500:
        return
    page = requests.get(url)
    contents = page.content

    soup = BeautifulSoup(contents, 'html.parser')

    links = soup.findAll('a')
    for link in links:
        #if link.has_attr('href'):
            #print(link['href'])
        if link.has_attr('href') and re.search(regex,link['href']):
            if link['href'] not in all_urls and link['href'] not in bad_urls:
                try:
                    link_stem_finder(link['href'],regex, depth+1)
                except:
                    bad_urls.append(link['href'])

npr_good_links = []
def npr_stem_finder(url, regex, depth, add_link = True):
    page = requests.get(url)
    contents = page.content

    soup = BeautifulSoup(contents, 'html.parser')
    #see if it is a political article
    temp = soup.find('h3',{"class": 'slug'}).getText()
    print(temp)
    #make sure that this url is accounted for
    if add_link:
        if temp.strip() in ["Law", "Politics", "Elections"]:
            npr_good_links.append(url)
        all_urls.append(url)
    print("good links: " + str(len(npr_good_links)))
    #print("all urls: " + str(len(all_urls)))


    if depth > 10 or len(npr_good_links) > 1000:
        return
    

    links = soup.findAll('div',{"class": 'recommended-story__info'})
    temp_links = []
    print(links)
    for link in links:
        temp_links += link.findAll('a')
    links = temp_links
    for link in links:
        if link.has_attr('href') and re.search(regex,link['href']):
            if link['href'] not in all_urls and link['href'] not in bad_urls:
                try:
                    npr_stem_finder(link['href'],regex, depth+1)
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

def custom_politico():
    #reters articles don't really link to each other, so the recursive approach doesn't work, lets try this
    regex = "^https://www\.politico\.com/news/.*2020/"
    for i in range(1,100):
        for stem in ["https://www.politico.com/white-house/","https://www.politico.com/congress/"]:
            url =  stem + str(i)
            page = requests.get(url)
            contents = page.content

            soup = BeautifulSoup(contents, 'html.parser')
            links = soup.findAll('div',{"class": 'summary'})
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

def custom_breitbart():
    regex = "www\.breitbart\.com/politics|^/politics"
    for i in range(1,200):
        for stem in ["https://www.breitbart.com/politics/page/"]:
            url =  stem + str(i)
            page = requests.get(url)
            contents = page.content

            soup = BeautifulSoup(contents, 'html.parser')
            links = soup.findAll('article')
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

def custom_the_hill():
    regex = "/policy.*-.*"
    for i in range(1,200):
        for stem in ["https://thehill.com/policy?page="]:
            url =  stem + str(i)
            page = requests.get(url)
            contents = page.content

            soup = BeautifulSoup(contents, 'html.parser')
            links = soup.findAll('article')
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
#custom_reuters()
#reuters_one_page()

#link_stem_finder(url,regex,depth)
#all_urls = politico_cleanup()

#custom_politico()
#npr_stem_finder(url,regex,depth)

#custom_breitbart()

custom_the_hill()
if True:
    for url in all_urls:
        print(url)
        print()
print(len(all_urls))

if False:
    file = open('website_urls/fox_urls_big.txt','w')
    for url in all_urls:
        file.write(str(url) + '\n')
