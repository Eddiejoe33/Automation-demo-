#!/usr/bin/env python3

import subprocess
from datetime import datetime

# -------------------
# 1️⃣ 
result = subprocess.run(['/home/userland/today.sh'], capture_output=True, text=True)
# -------------------
try:
    result = subprocess.run(['/home/userland/today.sh'], capture_output=True, text=True)
    tip_today = result.stdout.strip()
    if not tip_today:
        tip_today = "No matches today."
except Exception as e:
    tip_today = f"Failed to generate tip ({e})"

# -------------------
# 2️⃣ Add date to tip
# -------------------
date_today = datetime.now().strftime('%Y-%m-%d')
tip_with_date = f"{date_today} Tip: {tip_today}"

# -------------------
# 3️⃣ Write tip to a file (local “sheet”)
# -------------------
file_path = "/home/userland/daily_tips.txt"  # change path if you want
with open(file_path, "a") as f:  # use "a" to append each day
    f.write(tip_with_date + "\n")

print(f"✅ Tip saved to {file_path}: {tip_with_date}")
