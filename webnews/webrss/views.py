# import json to load json data to python dictionary 
import json 
# urllib.request to make a request to api 
import urllib.request 
from django.shortcuts import render
import feedparser
from bs4 import BeautifulSoup
import requests
import urllib3
import urllib.request
import urllib.parse

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
       
    return render(request, 'pages/index.html', {"item_rss": item_rss})

# Rss thời sự
def index_new(request):
    rss_feed_url_vnexpress = 'https://vnexpress.net/rss/thoi-su.rss'
    feed_vnexpress = feedparser.parse(rss_feed_url_vnexpress)
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
    return render(request, 'pages/news.html', {"item_rss": item_rss})

# Rss thế giới
def index_wolrd(request):
    rss_feed_url_vnexpress = 'https://vnexpress.net/rss/the-gioi.rss'
    feed_vnexpress = feedparser.parse(rss_feed_url_vnexpress)
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
    return render(request, 'pages/world.html', {"item_rss": item_rss})

#Rss kinh doanh
def index_business(request):
    rss_feed_url_vnexpress = 'https://vnexpress.net/rss/kinh-doanh.rss'
    feed_vnexpress = feedparser.parse(rss_feed_url_vnexpress)
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
    return render(request, 'pages/business.html', {"item_rss": item_rss})

#Rss thể thao
def index_sport(request):
    rss_feed_url_vnexpress = 'https://vnexpress.net/rss/the-thao.rss'
    feed_vnexpress = feedparser.parse(rss_feed_url_vnexpress)
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
    return render(request, 'pages/sport.html', {"item_rss": item_rss})

#Rss giải trí
def index_entertainment(request):
    rss_feed_url_vnexpress = 'https://vnexpress.net/rss/giai-tri.rss'
    feed_vnexpress = feedparser.parse(rss_feed_url_vnexpress)
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
    return render(request, 'pages/entertainment.html', {"item_rss": item_rss})

#Rss sức khỏe
def index_health(request):
    rss_feed_url_vnexpress = 'https://vnexpress.net/rss/suc-khoe.rss'
    feed_vnexpress = feedparser.parse(rss_feed_url_vnexpress)
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
    return render(request, 'pages/health.html', {"item_rss": item_rss})

#Rss đời sống
def index_life(request):
    rss_feed_url_vnexpress = 'https://vnexpress.net/rss/gia-dinh.rss'
    feed_vnexpress = feedparser.parse(rss_feed_url_vnexpress)
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
    return render(request, 'pages/life.html', {"item_rss": item_rss})

#Rss khoa học
def index_science(request):
    rss_feed_url_vnexpress = 'https://vnexpress.net/rss/khoa-hoc.rss'
    feed_vnexpress = feedparser.parse(rss_feed_url_vnexpress)
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
    return render(request, 'pages/science.html', {"item_rss": item_rss})

#Rss giáo dục
def index_education(request):
    rss_feed_url_vnexpress = 'https://vnexpress.net/rss/giao-duc.rss'
    feed_vnexpress = feedparser.parse(rss_feed_url_vnexpress)
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
    return render(request, 'pages/education.html', {"item_rss": item_rss})


# Api thời tiết
def weatherApi(request):
    if request.method == 'POST':
        city = request.POST['city']
        encoded_city = urllib.parse.quote(city)
        url = f'http://api.openweathermap.org/data/2.5/weather?q={encoded_city}&appid=26cd5325bb694c8bcf9659a9ab0d60e2'
        source = urllib.request.urlopen(url).read()
  
        list_of_data = json.loads(source) 
  
        data = { 
            "name": str(list_of_data['name']),
            "country_code": str(list_of_data['sys']['country']), 
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                        + str(list_of_data['coord']['lat']), 
            "temp": str(round(list_of_data['main']['temp'] - 273.15, 2)) + '°C', 
            "pressure": str(list_of_data['main']['pressure']), 
            "humidity": str(list_of_data['main']['humidity']), 
        } 
    else: 
        data ={} 
    return render(request, "pages/weather.html", data)

def coin_list(request):
    coin_url = 'https://apiforlearning.zendvn.com/api/get-coin'
    coin_response = requests.get(coin_url)
    items_coin = coin_response.json()

    return render(request, 'pages/coin.html', {"items_coin": items_coin})

def gold_list(request):
    gold_url = 'https://apiforlearning.zendvn.com/api/get-gold'
    gold_response = requests.get(gold_url)
    items_gold = gold_response.json()

    return render(request, 'pages/gold.html', {"items_gold": items_gold})