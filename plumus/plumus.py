from bs4 import BeautifulSoup
import pandas as pd

# Open the HTML file
with open(r'C:\Users\PSY\Documents\NEBA\python\plumus\202303050BRK.html', 'r') as file:
    html = file.read()

# Parse the HTML content
soup = BeautifulSoup(html, 'html.parser')

# Find all the players
players = soup.find_all('div', class_='player')

# Find all the plus/minus stats
stats = soup.find_all('div', class_='player-plusminus')

# Extract the player names
names = [player.find('span').text for player in players]

# Extract the plus/minus stats for each quarter
plusminus = []
for stat in stats:
    quarter_stats = [cell.text for cell in stat.find_all('div')]
    plusminus.append(quarter_stats)

# Create a pandas DataFrame
columns = ['Player', '1st Qtr', '2nd Qtr', '3rd Qtr', '4th Qtr']
df = pd.DataFrame(columns=columns)

for i in range(len(names)):
    player_stats = [names[i]] + plusminus[i]
    df.loc[i] = player_stats

# Print the DataFrame
print(df)
