import requests
from bs4 import BeautifulSoup

#page = requests.get('https://www.cnn.com/2020/10/20/politics/republican-senate-reaction-trump/index.html')
#contents = page.content
#####use the sitemap !!!!!!!!!!!!!
#soup = BeautifulSoup(contents, 'html.parser')
#paragraphs = soup.find_all('zn-body__paragraph')
#paragraphs = soup.findAll("div", {"class": "zn-body__paragraph"})
#print(paragraphs[0].getText())

page = requests.get('https://www.cnn.com/politics/article/sitemap-2020-1.html')
contents = page.content

soup = BeautifulSoup(contents, 'html.parser')
links = soup.findAll("a")
good_links = []
for link in links:
    if link.has_attr('href') and len(link['href']) > 20 and link['href'][:20] == 'https://www.cnn.com/' :
        #print(link['href'])
        good_links.append(link['href'])

def getArticle(url):
    page = requests.get(url)
    contents = page.content
    soup = BeautifulSoup(contents, 'html.parser')
    paragraphs = soup.findAll("div",{"class": "zn-body__paragraph"})
    returner = ""
    for val in paragraphs:
        returner += val.getText() + " " 
    return returner

print(len(good_links))
articles = []
for url in good_links[:1]:
    articles.append(getArticle(url))


for article in articles:
    print(article)


