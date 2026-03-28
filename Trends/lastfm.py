#!/usr/bin/env/python3
from collections import Counter

def get_stats(data):
    try:
        tracks = data['recenttracks']['track']
        artists = [t['artist']['#text'] for t in tracks]
        counts = Counter(artists)
        
        total = len(tracks)
        unique = len(counts)
        diversity = unique / total

        # THIS IS THE PART THAT PRINTS TO YOUR TTY
        print(f"Total History  : {total} scrobbles")
        print(f"Unique Artists : {unique}")
        print(f"Diversity Score: {diversity:.2f}")
        
    except Exception as e:
        print(f"Stats Error: {e}")
