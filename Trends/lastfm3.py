#!/usr/bin/env/python3
import requests

def get_weekly_champ(user, api_key):
    # This script needs its own API call because "Weekly" data is a different bucket
    URL = f"https://ws.audioscrobbler.com/2.0/?method=user.getweeklyartistchart&user={user}&api_key={api_key}&format=json"
    
    try:
        r = requests.get(URL)
        data = r.json()
        
        # Grab the list of artists
        chart = data.get('weeklyartistchart', {}).get('artist', [])
        
        if not chart:
            print("No weekly data found yet for this period.")
            return

        print("🏆 WEEKLY LEADERBOARD")
        # Show Top 5
        for i, artist in enumerate(chart[:5], 1):
            name = artist['name']
            count = artist['playcount']
            print(f"{i}. {name} — {count} plays")
            
    except Exception as e:
        print(f"Weekly Chart Error: {e}")
