# --- NOVÉ NASTAVENIA PRE MAXIMÁLNY ZISK ---
from flask import Flask
STARTING_BALANCE = 14.00
CURRENT_BALANCE = STARTING_BALANCE
MIN_SAFE_LIMIT = 0.05       # Bezpečnostná rezerva nad úplnou nulou
STRATEGY_AGGRESSION = 0.8  # Bot reinvestuje 80% zisku do rastu

class AutonomousAgent:
    def __init__(self, balance):
        self.balance = balance
        self.total_earned = 0.0
        self.iteration = 1

    def reinvest(self):
        # Ak sme v zisku, bot agresívne investuje do škálovania
        if self.balance > STARTING_BALANCE:
            available_profit = self.balance - STARTING_BALANCE
            investment = available_profit * STRATEGY_AGGRESSION
            
            # Kontrola, či po investícii zostaneme nad nulou
            if (self.balance - investment) >= MIN_SAFE_LIMIT:
                print(f"Balančný update: Reinvestujem {investment:.2f}€ pre maximálny rast...")
                self.balance -= investment
                return True
        return False

    def run(self):
        print("BOT SPUSTENÝ V REŽIME 'MAXIMÁLNY ZISK'")
        while True:  # Nekonečná slučka - zarába, koľko to pôjde
            self.report_status()
            job = self.find_opportunity()
            profit = self.execute_action(job)
            self.balance += profit
            self.total_earned += profit
            self.reinvest()
            
            self.iteration += 1
            # Na Renderi odporúčam nechať 3600 (1 hodina), aby ho nezablokovali

            time.sleep(3600)
            from flask import Flask
import threading

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot beží!"

def run_web():
    app.run(host='0.0.0.0', port=10000)

# Spustíme web na pozadí, aby Render videl port
threading.Thread(target=run_web).start()

