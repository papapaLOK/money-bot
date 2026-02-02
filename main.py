import os
import time
import random
import threading
import requests
from flask import Flask
from dotenv import load_dotenv

load_dotenv()

PAYPAL_MAIL = os.getenv("PAYPAL_EMAIL", "nepriradeny_mail")
STARTING_BALANCE = 14.00
current_balance = STARTING_BALANCE

app = Flask(__name__)

@app.route('/')
def home():
    return f"<h1>Agent v práci</h1><p>Pracujem pre: {PAYPAL_MAIL}</p><p>Aktuálny stav: {current_balance:.2f}€</p>"

def search_for_deals():
    """Funkcia, kde bot sám 'surfuje' po webe a hľadá zisk"""
    global current_balance
    
    # Zoznam webov, ktoré bot 'skenuje' (simulujeme prístup k verejným dátam)
    sources = ["amazon_deals", "crypto_faucets", "ebay_errors", "ad_clicks"]
    
    while True:
        source = random.choice(sources)
        # Bot 'našiel' príležitosť a spracoval ju
        # V reálnom kóde tu bot sťahuje HTML stránky a hľadá ceny
        found_profit = random.uniform(0.02, 0.08) 
        
        current_balance += found_profit
        
        # TVOJE PRAVIDLO: Reinvestovať a neklesnúť pod nulu
        if current_balance > STARTING_BALANCE:
            reinvest_part = (current_balance - STARTING_BALANCE) * 0.5
            if (current_balance - reinvest_part) >= STARTING_BALANCE:
                # Bot reinvestuje do lepších serverov, aby skenoval rýchlejšie
                current_balance -= reinvest_part
        
        print(f"Bot skenoval {source}: Zisk +{found_profit:.2f}€ | Celkovo: {current_balance:.2f}€")
        
        # Pauza, aby ho weby nezablokovali
        time.sleep(3600)

if __name__ == "__main__":
    # Spustenie webu pre Render
    threading.Thread(target=lambda: app.run(host='0.0.0.0', port=10000, use_reloader=False)).start()
    # Spustenie hľadania biznisu
    search_for_deals()
