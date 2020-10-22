import requests
from bs4 import BeautifulSoup


url = 'https://www.foxnews.com/politics/faith-and-family-a-look-at-judge-amy-coney-barrett'

def getArticle(url,site):
    page = requests.get(url)
    contents = page.content
    soup = BeautifulSoup(contents, 'html.parser')
    if(site == 'fox'):
        paragraphs = soup.find('div',{"class": 'article-body'}).findAll('p')
        bad_paragraphs = soup.find('div',{"class": 'article-body'}).findAll(href=True)
        #temp = soup.findAll('div',{"class": 'info'})
        #bad_paragraphs += temp
        #we want to get rid of the annoying links in the middle of the articles
        for i in range(0,len(bad_paragraphs)):
            bad_paragraphs[i] = bad_paragraphs[i].getText()
        returner = ""
        for paragraph in paragraphs:
            temp = paragraph.getText()
            #print(temp)
            #print(bad_paragraphs)
            if temp not in bad_paragraphs:
                returner += temp + " " 
        return returner
        #soup = BeautifulSoup(article_html,'html.parser')
        #return soup.findAll('p')
        
    #paragraphs = soup.findAll("div",{"class": html_class})
    
    returner = ""
    for val in paragraphs:
        returner += val.getText() + " " 
    return returner

print(getArticle(url,'fox'))
#getArticle(url,'fox')