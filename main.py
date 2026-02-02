import os
import time
import random
import threading
from flask import Flask
from dotenv import load_dotenv

load_dotenv()

# Bot si vytiahne tvoje maily z nastavení Renderu
PAYPAL_MAIL = os.getenv("PAYPAL_EMAIL", "nepriradeny_paypal")
NORMAL_MAIL = os.getenv("CONTACT_EMAIL", "nepriradeny_kontakt")

# Tvoj základný kapitál (z tvojho plánu)
STARTING_BALANCE = 14.00
current_balance = STARTING_BALANCE

app = Flask(__name__)

@app.route('/')
def home():
    return f"Agent pracuje pre: {PAYPAL_MAIL} | Aktuálny stav: {current_balance:.2f}€"

def bot_logic():
    global current_balance
    print(f"BOT SPUSTENÝ PRE: {PAYPAL_MAIL}")
    while True:
        # Simulácia zisku (tu neskôr napojíme reálne úlohy)
        profit = random.uniform(0.01, 0.05)
        current_balance += profit
        
        # REINVESTOVANIE (Tvoje pravidlo: reinvestovať, ale nikdy pod nulu)
        if current_balance > STARTING_BALANCE:
            reinvest = (current_balance - STARTING_BALANCE) * 0.5
            if (current_balance - reinvest) >= STARTING_BALANCE:
                current_balance -= reinvest
        
        print(f"Zostatok: {current_balance:.2f}€ | Mail: {PAYPAL_MAIL}")
        time.sleep(3600)

if __name__ == "__main__":
    # Web server pre Render na porte 10000
    threading.Thread(target=lambda: app.run(host='0.0.0.0', port=10000, use_reloader=False)).start()
    bot_logic()
