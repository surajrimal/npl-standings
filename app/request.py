from .models import Articles
from newsapi import NewsApiClient
from .config import Config
from datetime import datetime

import os
from hashlib import sha256

def generate_csrf_token():
    if '_csrf_token' not in session:
        session['_csrf_token'] = sha256(os.urandom(64)).hexdigest()
    return session['_csrf_token']

def publishedArticles():
    newsapi = NewsApiClient(api_key=Config.API_KEY)
    get_articles = newsapi.get_everything(q='Nepal Premier League', sort_by='publishedAt', page_size=40)

    all_articles = get_articles['articles']
    source = []
    title = []
    desc = []
    author = []
    img = []
    p_date = []
    url = []
    
    matches = [""]
    for article in all_articles:
        # Debugging step to inspect image URLs and headlines
        #print(f"Processing article: {article['title']}, Image URL: {article['urlToImage']}")

        # Filter for articles with images and the word "NPL" in the title
        if any(x in article['description'].upper() for x in matches):
            source.append(article['source']['name'] if article['source'] else "Unknown")
            title.append(article['title'])
            desc.append(article['description'])
            author.append(article['author'] if article['author'] else "Unknown Author")
            img.append(article['urlToImage'])
            date_obj = datetime.strptime(article['publishedAt'], '%Y-%m-%dT%H:%M:%SZ')
            formatted_date = date_obj.strftime('%B %d, %Y')
            p_date.append(formatted_date)
            url.append(article['url'])

    # Create zipped content
    contents = zip(source, title, desc, author, img, p_date, url)
    return contents

def publishedArticlesFive():
    articles = list(publishedArticles())
    return articles[:5]
