import requests
from bs4 import BeautifulSoup

#CNN
#New York Times
#--Huffington Post
#Fox News
#USA Today
#Reuters US news
#Politico
#Yahoo News
#--Npr news
#--LA Times
#Breitbart
#Wall street journal

url_cnn = 'https://www.cnn.com/2020/10/27/politics/justice-amy-coney-barrett-sworn-in-supreme-court/index.html'
url_fox = 'https://www.foxnews.com/politics/supreme-court-strikes-down-state-ban-on-taxpayer-funding-for-religious-schools'
url_nyt = 'https://www.nytimes.com/2020/10/26/us/politics/trump-barrett.html'
url_usatoday = 'https://www.usatoday.com/story/news/politics/2020/10/27/cincinnati-columbus-lawsuit-seek-overturn-house-bill-6-bailout-tax/3748629001/'
url_reuters = 'https://www.reuters.com/article/us-usa-election-pence/political-adviser-sparked-covid-19-outbreak-on-vice-president-pence-team-sources-idUSKBN27C2X5'
url_politico = 'https://www.politico.com/news/2020/10/27/no-apologies-mcconnell-says-barrett-a-huge-success-for-the-country-432828'
url_yahoo = 'https://news.yahoo.com/wisconsin-decision-supreme-court-foreshadows-020446094.html'
url_yahoo2 = 'https://news.yahoo.com/i-purely-vote-for-my-actual-interests-black-men-could-be-critical-bloc-in-presidential-election-174237805.html'
url_breitbart = 'https://www.breitbart.com/radio/2020/10/08/greg-pence-biden-harris-raise-taxes-defund-police-eliminate-2a-open-borders-green-new-deal/'
url_thehill = 'https://thehill.com/homenews/campaign/527832-https-covidtrackingcom-data'
url_epochtimes = ''

def getArticle(url, site):
    page = requests.get(url)
    contents = page.content
    soup = BeautifulSoup(contents, 'html.parser')
    if (site == 'cnn'):
        #Get title
        title = soup.find("div",{"class": "l-container"}).find("h1",{"class": "pg-headline"}).getText()

        #Get article
        paragraphs = soup.findAll("div",{"class": "zn-body__paragraph"})
        returner = ""
        for val in paragraphs:
            returner += val.getText() + " "
        return (title, returner)
    if(site == 'fox'):
        #Get title
        title = soup.find('h1', {"class": 'headline'}).getText()
        #Get article
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
        return (title, returner)

    if (site == 'nyt'):
        #Get title
        title = soup.find('h1', {"itemprop": 'headline'}).getText()
        #Get article

        paragraphs = soup.find('section', {"name": 'articleBody'}).findAll('p')
        returner = ""
        for paragraph in paragraphs:
            temp = paragraph.getText()
            returner += temp + " " 
        return (title, returner)

    if (site == 'usatoday'):
        #Get title
        title = soup.find('h1', {"class": 'gnt_ar_hl'}).getText()
        #Get article
        paragraphs = soup.find('div', {"class": 'gnt_ar_b'}).findAll('p')
        returner = ""
        for paragraph in paragraphs:
            temp = paragraph.getText()
            #filter out bold
            if not paragraph.find('strong'):
                returner += temp + " "
        return (title, returner)

    if (site == 'reuters'):
        #Get title
        title = soup.find('h1', {"class": 'Headline-headline-2FXIq'}).getText()
        #Get article
        paragraphs = soup.find('div', {"class": 'ArticleBodyWrapper'}).findAll('p')
        returner = ""
        for paragraph in paragraphs:
            temp = paragraph.getText()
            returner += temp + " " 
        return (title, returner)

    if (site == 'politico'):

        #Get title
        title = soup.find('h2', {"class": 'headline'}).getText()
        #Get article
        storytexts = soup.findAll('div', {"class": 'story-text'})
        returner = ""
        for storytext in storytexts:
            #paragraphs = storytext.findAll('p')
            paragraphs = storytext.findAll('p', {"class": 'story-text__paragraph'})
            for paragraph in paragraphs:
                temp = paragraph.getText()
                returner += temp + " " 
        
        return (title, returner)

    if (site == 'yahoo'):
        #Get title
        title = soup.find('h1', {"data-test-locator": 'headline'}).getText()
        #Get article
        #paragraphs = soup.find('article', {"itemprop": 'articleBody'}).findAll('p')
        #link_bullet = soup.find('article', {"itemprop": 'articleBody'}).findAll(href=True)

        paragraphs = soup.find('div', {"class": 'caas-body'}).findAll('p')
        link_bullet = soup.find('div', {"class": 'caas-body'}).findAll(href=True)
        returner = ""
        for i in range(0, len(link_bullet)):
            link_bullet[i] = link_bullet[i].getText()
        
        for paragraph in paragraphs:
            temp = paragraph.getText()
            #remove 'Read more from Yahoo News:' plus links at the end of yahoo original articles
            if (not temp == 'Read more from Yahoo News:' and temp not in link_bullet):
                returner += temp + " " 
        return (title, returner)

    if (site == 'breitbart'):
        #Get title
        title = soup.find('article', {"class": 'the-article'}).find('header').find('h1').getText()
        #Get article
        paragraphs = soup.find('div', {"class": 'entry-content'}).findAll('p')
        returner = ""
        for paragraph in paragraphs:
            temp = paragraph.getText()
            returner += temp + " " 
        return (title, returner)

    if (site == 'thehill'):
        #Get title
        title = soup.find('h1', {"class": 'title'}).getText()
        #Get article
        paragraphs = soup.find('div', {"class": 'field-item'}).findAll('p')
        returner = ""
        for paragraph in paragraphs:
            #Find and replace annoying link hovers
            spans = paragraph.findAll('span')
            for span in spans:
                #replace with link text
                a = span.find('a')
                if a is not None:
                    span.replace_with(a.getText())
            temp = paragraph.getText()
            returner += temp + " " 
        return (title, returner)

    if (site == 'epochtimes'):
        #Get title
        #title = soup.find('article', {"class": 'the-article'}).find('header').find('h1').getText()
        #Get article
        #paragraphs = soup.find('div', {"class": 'entry-content'}).findAll('p')
        #returner = ""
        #for paragraph in paragraphs:
            #temp = paragraph.getText()
            #returner += temp + " " 
        #return (title, returner)



    # paragraphs = soup.findAll("div",{"class": html_class})
    # this is the basic format of returning the paragarphs
    '''
    returner = ""
    for val in paragraphs:
        returner += val.getText() + " " 
    return returner
    '''

#print(getArticle(url_fox,'fox')[0])
#print(getArticle(url_nyt, 'nyt')[0])
#print(getArticle(url_usatoday, 'usatoday')[0])
#print(getArticle(url_reuters, 'reuters')[0])
#print(getArticle(url_politico, 'politico')[0])
#print(getArticle(url_yahoo2, 'yahoo')[0])
#print(getArticle(url_cnn, 'cnn')[0])
#print(getArticle(url_breitbart, 'breitbart')[0])
print(getArticle(url_thehill, 'thehill')[1])
#print(getArticle(url_epochtimes, 'epochtimes')[0])

