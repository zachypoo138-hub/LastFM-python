#!/usr/bin/env python3
import sys
import requests
import lastfm
import lastfm2
import lastfm3
import lastfm4

# Keep the API Key hardcoded (or move to an environment variable later)
API_KEY = "06706dd5607746739fbd1ed356d6ad42"

def main():
    # --- PORTABILITY LOGIC ---
    # Check if a username was passed as an argument (e.g., ./lastfm_mgr.py zector1981)
    if len(sys.argv) > 1:
        user = sys.argv[1]
    else:
        # Fallback: Ask the user manually
        user = input("Enter Last.fm Username: ").strip()

    if not user:
        print("Error: No username provided.")
        return

    # Dynamic URL based on the input user
    url = f"https://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user={user}&api_key={API_KEY}&format=json&limit=200"

    try:
        print(f"\n📡 Fetching Recent Activity for {user.upper()}...")
        r = requests.get(url)
        json_payload = r.json()

        if 'error' in json_payload:
            print(f"API Error: {json_payload['message']}")
            return

        print("=" * 40)
        lastfm.get_stats(json_payload)
        
        print("-" * 40)
        lastfm2.get_bulls(json_payload)
        
        print("-" * 40)
        lastfm3.get_weekly_champ(user, API_KEY) 
        
        print("-" * 40)
        lastfm4.get_weekly_history(user, API_KEY, limit=5)
        print("=" * 40)

    except Exception as e:
        print(f"Manager Error: {e}")

if __name__ == "__main__":
    main()
