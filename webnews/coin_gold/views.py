from django.shortcuts import render
import requests 
# Create your views here.
def index(request):
    coin_url = 'https://apiforlearning.zendvn.com/api/get-coin'
    coin_response = requests.get(coin_url)
    items_coin = coin_response.json()

    return render(request, 'coin.html', {"items_coin": items_coin})

def gold_list(request):
    gold_url = 'https://apiforlearning.zendvn.com/api/get-gold'
    gold_response = requests.get(gold_url)
    items_gold = gold_response.json()

    return render(request, 'gold.html', {"items_gold": items_gold})
