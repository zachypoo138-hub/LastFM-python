#!/usr/bin/env/python3
import requests
import datetime

def get_weekly_history(user, api_key, limit=5):
    # 1. Get the list of "Time Periods" (Weeks) available
    LIST_URL = f"https://ws.audioscrobbler.com/2.0/?method=user.getweeklychartlist&user={user}&api_key={api_key}&format=json"
    
    try:
        r = requests.get(LIST_URL)
        periods = r.json().get('weeklychartlist', {}).get('chart', [])
        
        # We want the most recent weeks, so we look at the end of the list and reverse it
        recent_periods = periods[-limit:][::-1]

        print(f"📅 WEEKLY TOP ARTIST")
        print("-" * 40)

        for p in recent_periods:
            start_ts = p['from']
            end_ts = p['to']
            
            # Convert timestamp to a readable date
            date_str = datetime.datetime.fromtimestamp(int(end_ts)).strftime('%m/%d/%Y')

            # 2. Get the #1 Artist for THIS specific period
            CHART_URL = f"https://ws.audioscrobbler.com/2.0/?method=user.getweeklyartistchart&user={user}&api_key={api_key}&from={start_ts}&to={end_ts}&format=json"
            
            chart_r = requests.get(CHART_URL)
            chart_data = chart_r.json().get('weeklyartistchart', {}).get('artist', [])

            if chart_data:
                winner = chart_data[0] # The #1 spot
                print(f"Week of {date_str}: {winner['name']} ({winner['playcount']} plays)")
            else:
                print(f"Week of {date_str}: [No Data]")

    except Exception as e:
        print(f"History Error: {e}")
