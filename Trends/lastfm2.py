#!/usr/bin/env/python3
from collections import Counter

def get_bulls(data):
    try:
        tracks = data['recenttracks']['track']
        artists = [t['artist']['#text'] for t in tracks]
        
        recent = Counter(artists[:50])
        older = Counter(artists[50:])
        
        top_artist = recent.most_common(1)[0][0]
        diff = (recent[top_artist]/50 - older[top_artist]/150) * 100

        # MAKE SURE THESE PRINT STATEMENTS EXIST
        print(f"Top Asset: {top_artist}")
        print(f"Trend    : {'🚀 BULLISH' if diff > 5 else '📉 BEARISH' if diff < -5 else '↔️ STABLE'} ({diff:+.1f}%)")
        
    except Exception as e:
        print(f"Bulls Error: {e}")
