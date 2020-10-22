import requests
from bs4 import BeautifulSoup

#this gets the html content of whatever webpage you want
page = requests.get('https://www.cnn.com/politics/article/sitemap-2020-1.html')
contents = page.content

#create the soup object using the content of the page we loaded
soup = BeautifulSoup(contents, 'html.parser')

#this finds all links on the page 
links = soup.findAll("a")

good_links = []

#this loop makes sure to only select links that are actually leading to articles on the site
for link in links:
    if link.has_attr('href') and len(link['href']) > 20 and link['href'][:20] == 'https://www.cnn.com/' :
        good_links.append(link['href'])

def getArticle(url):
    page = requests.get(url)
    contents = page.content
    soup = BeautifulSoup(contents, 'html.parser')
    #this is the class that all the text in the articles have 
    paragraphs = soup.findAll("div",{"class": "zn-body__paragraph"})
    returner = ""
    #concatonate the text of the article together
    for val in paragraphs:
        returner += val.getText() + " " 
    return returner

articles = []
#get the text of the first 5 articles
for url in good_links[:5]:
    articles.append(getArticle(url))


for article in articles:
    print(article)


