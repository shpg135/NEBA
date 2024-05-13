import requests
from bs4 import BeautifulSoup
import pandas as pd

with open(r'C:\Users\PSY\Documents\NEBA\python\pbp\test\202303050BRK.html', 'r') as file:
    html = file.read()
soup = BeautifulSoup(html, "html.parser")

# target pbp table
pbp_table = soup.find("table", {"id": "pbp"})
# Read table into a pandas DataFrame
df = pd.read_html(str(pbp_table))[0]

# # Split the "Time" column into "Quarter" and "Time"
# df[['Quarter', 'Time']] = df['Time'].str.split(' ', expand=True)
#
# # Extract the relevant information from the "Action" column
# df[['Action', 'Assist']] = df['Action'].str.extract(r'^(.*)(?:\((.*?)\))?$', expand=True)
#
# # Clean up the "Action" and "Assist" columns
# df['Action'] = df['Action'].str.strip()
# df['Assist'] = df['Assist'].str.strip().str.replace('assist by ', '', case=False)
#
# # Rename the columns to match the desired output
# df = df.rename(columns={'Player': 'player', 'Quarter': 'quarter', 'Time': 'time', 'Action': 'action'})

# Export the DataFrame to a CSV file
df.to_csv(r'C:\Users\PSY\Documents\NEBA\python\pbp\test\NBA_Play_By_Play_Data.csv', index=False)
# thead = pbp_table.find("thead")
# header_rows = thead.find_all("tr")
# headers = []
# for row in header_rows:
#     header_cols = row.find_all("th")
#     header_row = []
#     for col in header_cols:
#         header_row.append(col.text)
#     headers.append(header_row)
# extract the lineup changes with time in the game





    #pbp_line['quarter'] =
    #time_str = row.find("td", {"class": "left"}).text.strip()
    #print(row.text)

    #lineup_str = row.find("td", {"class": "right"}).text.strip()
    #lineup_changes.append((time_str, lineup_str))

#print(lineup_changes)
