from django.shortcuts import render
import feedparser
from bs4 import BeautifulSoup

def index(request):
    rss_feed_url_vnexpress = 'https://vnexpress.net/rss/tin-moi-nhat.rss'
    rss_feed_url_thanhnien = 'https://thanhnien.vn/rss/home.rss'
    
    feed_vnexpress = feedparser.parse(rss_feed_url_vnexpress)
    feed_thanhnien = feedparser.parse(rss_feed_url_thanhnien)

    item_rss = []

    for item in feed_vnexpress.entries:
        title = item.get('title')
        pub_date = item.get('published')
        link = item.get('link')

        description = item.get('summary')
        description_soup = BeautifulSoup(description, 'html.parser')
        description_text = description_soup.get_text()

        img_tag = description_soup.find('img')
        img_src = "https://hanghoaphaisinhdalat.com/wp-content/uploads/2021/01/120121.png"

        if img_tag:
            img_src = img_tag['src']
        
        item ={
            "title": title,
            "pub_date": pub_date,
            "link": link,
            "description": description_text,
            "image": img_src
        }

        item_rss.append(item)
    
    for item in feed_thanhnien.entries:
        title = item.get('title')
        pub_date = item.get('published')
        link = item.get('link')

        description = item.get('summary')
        description_soup = BeautifulSoup(description, 'html.parser')
        description_text = description_soup.get_text()

        img_tag = description_soup.find('img')
        img_src = "https://hanghoaphaisinhdalat.com/wp-content/uploads/2021/01/120121.png"

        if img_tag:
            img_src = img_tag['src']
        
        item ={
            "title": title,
            "pub_date": pub_date,
            "link": link,
            "description": description_text,
            "image": img_src
        }

        item_rss.append(item)
       
    return render(request, 'index.html', {"item_rss": item_rss})