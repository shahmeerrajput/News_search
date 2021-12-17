import requests
import pandas as pd
from bs4 import BeautifulSoup
import re
import time

def Geo():
    resp = requests.get('https://www.geo.tv/category/pakistan')
    soup = BeautifulSoup(resp.text, 'html.parser')
    top_stories = soup.select('[class="video-list laodMoreCatNews"] a')
    data = pd.read_excel('LiveDataSetOfNews.xlsx').values.tolist()
    for top_story in top_stories:
        link = top_story.get('href')
        headline = top_story.getText()
        headline = re.sub('[^a-zA-Z]', ' ', headline)
        headline = headline.lower()
        headline = headline.strip()
        if headline == "":
            continue
        if [link, headline] not in data:
            data.append([link, headline])
    df = pd.DataFrame(data)
    df.dropna()
    df.columns = ['Link', 'Headline']
    df.to_excel('LiveDataSetOfNews.xlsx', index=False, header=True)

def dawn():
    resp = requests.get('https://www.dawn.com/pakistan')
    soup = BeautifulSoup(resp.text, 'html.parser')
    top_stories = soup.select('[class="container"] h2 a ')
    data =pd.read_excel('LiveDataSetOfNews.xlsx').values.tolist()
    for top_story in top_stories:
        link = top_story.get('href')
        headline = top_story.getText()
        headline = re.sub('[^a-zA-Z]', ' ', headline)
        headline = headline.lower()
        headline = headline.strip()
        if headline == "":
            continue
        if [link, headline] not in data:
            data.append([link, headline])
    df = pd.DataFrame(data)
    df.columns = ['Link', 'Headline']
    df.to_excel('LiveDataSetOfNews.xlsx', index=False, header=True)

def aaj():
    resp = requests.get('https://www.aaj.tv/english/pakistan')
    soup = BeautifulSoup(resp.text, 'html.parser')
    top_stories = soup.select('[class="w-full mt-8 border-t pt-4"] h2 a')
    data =pd.read_excel('LiveDataSetOfNews.xlsx').values.tolist()
    for top_story in top_stories:
        link = top_story.get('href')
        headline = top_story.getText()
        headline = re.sub('[^a-zA-Z]', ' ', headline)
        headline = headline.lower()
        headline = headline.strip()
        if headline == "":
            continue
        if [link, headline] not in data:
            data.append([link, headline])
    df = pd.DataFrame(data)
    df.columns = ['Link', 'Headline']
    df.to_excel('LiveDataSetOfNews.xlsx', index=False, header=True)

def sama():
    resp = requests.get('https://www.samaa.tv/news/')
    soup = BeautifulSoup(resp.text, 'html.parser')
    top_stories = soup.select('[class="container"] p a')
    data =pd.read_excel('LiveDataSetOfNews.xlsx').values.tolist()
    for top_story in top_stories:
        link = top_story.get('href')
        headline = top_story.getText()
        headline = re.sub('[^a-zA-Z]', ' ', headline)
        headline = headline.lower()
        headline = headline.strip()
        if headline == "":
            continue
        if [link, headline] not in data:
            data.append([link, headline])
    df = pd.DataFrame(data)
    df.columns = ['Link', 'Headline']
    df.to_excel('LiveDataSetOfNews.xlsx', index=False, header=True)

def dunya():
    resp = requests.get('https://dunyanews.tv/en/Pakistan')
    soup = BeautifulSoup(resp.text, 'html.parser')
    top_stories = soup.select('[id="categoryTabs"] h3 a')
    data =pd.read_excel('LiveDataSetOfNews.xlsx').values.tolist()
    for top_story in top_stories:
        link = top_story.get('href')
        headline = top_story.getText()
        headline = re.sub('[^a-zA-Z]', ' ', headline)
        headline = headline.lower()
        headline = headline.strip()
        if headline == "":
            continue
        if [link, headline] not in data:
            data.append([link, headline])
    df = pd.DataFrame(data)
    df.columns = ['Link', 'Headline']
    df.to_excel('LiveDataSetOfNews.xlsx', index=False, header=True)

def allNews():
    Geo()
    dawn()
    aaj()
    sama()
    dunya()

if __name__ == '__main__':
    df1 = pd.DataFrame(list())
    df1.to_excel("LiveDataSetOfNews.xlsx",index= False)  
    while True:
        allNews()
        time_wait = 10800
        print(f'Waiting {time_wait} seconds...')
        time.sleep(time_wait)