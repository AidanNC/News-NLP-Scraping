import requests
from bs4 import BeautifulSoup


url = 'https://www.foxnews.com/politics/supreme-court-strikes-down-state-ban-on-taxpayer-funding-for-religious-schools'
url_nyt = 'https://www.nytimes.com/2020/10/26/us/politics/trump-barrett.html'
url_usatoday = 'https://www.usatoday.com/story/news/politics/2020/10/27/cincinnati-columbus-lawsuit-seek-overturn-house-bill-6-bailout-tax/3748629001/'
url_reuters = 'https://www.reuters.com/article/us-usa-election-pence/political-adviser-sparked-covid-19-outbreak-on-vice-president-pence-team-sources-idUSKBN27C2X5'

def getArticle(url, site):
    page = requests.get(url)
    contents = page.content
    soup = BeautifulSoup(contents, 'html.parser')
    if(site == 'fox'):
        paragraphs = soup.find('div', {"class": 'article-body'}).findAll('p')
        bad_paragraphs = soup.find('div', {"class": 'article-body'}).findAll(href=True)

        # we want to get rid of the annoying links in the middle of the articles
        for i in range(0, len(bad_paragraphs)):
            bad_paragraphs[i] = bad_paragraphs[i].getText()
        returner = ""
        for paragraph in paragraphs:
            temp = paragraph.getText()
            if temp not in bad_paragraphs:
                returner += temp + " "
        return returner

    if (site == 'nyt'):
        paragraphs = soup.find('section', {"name": 'articleBody'}).findAll('p')
        returner = ""
        for paragraph in paragraphs:
            temp = paragraph.getText()
            returner += temp + " " 
        return returner

    if (site == 'usatoday'):
        paragraphs = soup.find('div', {"class": 'gnt_ar_b'}).findAll('p')
        returner = ""
        for paragraph in paragraphs:
            temp = paragraph.getText()
            #filter out bold
            if not paragraph.find('strong'):
                returner += temp + " "
        return returner

    if (site == 'reuters'):
        paragraphs = soup.find('div', {"class": 'ArticleBodyWrapper'}).findAll('p')
        returner = ""
        for paragraph in paragraphs:
            temp = paragraph.getText()
            returner += temp + " " 
        return returner
    # paragraphs = soup.findAll("div",{"class": html_class})
    # this is the basic format of returning the paragarphs
    '''
    returner = ""
    for val in paragraphs:
        returner += val.getText() + " " 
    return returner
    '''

#print(getArticle(url,'fox'))
#print(getArticle(url_nyt, 'nyt'))
#print(getArticle(url_usatoday, 'usatoday'))
print(getArticle(url_reuters, 'reuters'))
# getArticle(url,'fox')
