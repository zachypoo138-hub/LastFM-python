import os
import json
import requests
import numpy as np
from datetime import datetime
from sklearn.linear_model import LinearRegression

# --- CONFIGURATION (Add your details here) ---
API_KEY = "d145101568913b6164e37a078437408b"
USER = "zector1981"

# --- PRO PATHING ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HISTORY_FILE = os.path.join(BASE_DIR, "scrobble_history.json")

def get_today_from_api():
    """Pulls the real scrobble count from Last.fm for today."""
    today_start = int(datetime.now().replace(hour=0, minute=0, second=0, microsecond=0).timestamp())
    url = f"http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user={USER}&api_key={API_KEY}&from={today_start}&format=json"
    try:
        r = requests.get(url).json()
        return int(r['recenttracks']['@attr']['total'])
    except Exception as e:
        print(f"❌ API Error: {e}")
        return None

def run_ai_logic(history):
    """Performs the Linear Regression on the history data."""
    if len(history) < 2:
        return "Need at least 2 days of data to trend."
    
    X, y = [], []
    for date_str, count in history.items():
        try:
            date_obj = datetime.strptime(date_str, "%Y-%m-%d")
            X.append(date_obj.toordinal())
            y.append(int(count))
        except ValueError:
            continue # Ignore bad data
            
    X = np.array(X).reshape(-1, 1)
    y = np.array(y)
    
    model = LinearRegression().fit(X, y)
    tomorrow = datetime.now().toordinal() + 1
    prediction = model.predict(np.array([[tomorrow]]))
    # Ensure the prediction never goes below 0
    final_guess = int(prediction[0])
    return max(0, final_guess)

def main():
    # 1. Sync with Last.fm
    actual_today = get_today_from_api()
    if actual_today is None: return

    # 2. Update the "Vault"
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'r') as f:
            history = json.load(f)
    else:
        history = {}

    today_str = datetime.now().strftime("%Y-%m-%d")
    history[today_str] = actual_today

    with open(HISTORY_FILE, 'w') as f:
        json.dump(history, f, indent=4)

    # 3. Predict & Report
    prediction = run_ai_logic(history)
    
    print(f"\n--- 🛰️  SYSTEM SYNC: {today_str} ---")
    print(f"Current Scrobble Count : {actual_today}")
    print(f"AI Prediction (Tomorrow): {prediction}")
    print("-" * 30)

if __name__ == "__main__":
    main()
