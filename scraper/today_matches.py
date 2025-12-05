import requests
import csv
import io
from datetime import datetime

# URL of EPL 2022/23 CSV file
url = "https://www.football-data.co.uk/mmz4281/2223/E0.csv"

# Download CSV data
response = requests.get(url)
data = response.content.decode('utf-8')

# Parse CSV
reader = csv.DictReader(io.StringIO(data))

# Get today’s date in format used in CSV (dd/mm/yyyy)
today_str = datetime.today().strftime('%d/%m/%Y')

# Open CSV file to save today’s matches
with open('today_matches.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR'])
    
    found = False  # Flag to check if any match today
    for row in reader:
        if row['Date'] == today_str:
            writer.writerow([row['Date'], row['HomeTeam'], row['AwayTeam'],
                             row['FTHG'], row['FTAG'], row['FTR']])
            print(row['Date'], row['HomeTeam'], row['AwayTeam'], row['FTHG'], row['FTAG'], row['FTR'])
            found = True

if not found:
    print("No matches today.")
