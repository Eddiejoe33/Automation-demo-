#!/usr/bin/env python3

import tweepy
import subprocess
from datetime import datetime

# X API credentials
API_KEY = "YOUR_API_KEY"
API_SECRET = "YOUR_API_SECRET"
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ACCESS_SECRET = "YOUR_ACCESS_SECRET"

# Authenticate
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# Get tip from today.sh
try:
    result = subprocess.run(['/home/userland/today.sh'], capture_output=True, text=True)
    tip_today = result.stdout.strip()
    if not tip_today:
        tip_today = "No matches today."
    tip_with_date = f"{datetime.now().strftime('%Y-%m-%d')} Tip: {tip_today}"
except Exception as e:
    tip_with_date = f"{datetime.now().strftime('%Y-%m-%d')} Tip: Failed to generate tip ({e})"

# Post to X
try:
    api.update_status(tip_with_date)
    print("✅ Tip posted successfully:", tip_with_date)
except Exception as e:
    print("❌ Failed to post tip:", e)
