from bs4 import BeautifulSoup
from openpyxl import Workbook
import requests

# Make a request to the web page
#page = requests.get("https://example.com")
season = '2024'
month = 'october'
url = 'https://www.basketball-reference.com/leagues/NBA_{}_games-{}.html'.format(season,month)
# Open the HTML file
save_dir = r"C:\Users\PSY\Documents\NEBA\python\pfgamelog"
headers = {
         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
     }
session = requests.session()
html = session.get(url,headers=headers).content
# with open(r'C:\Users\PSY\Documents\NEBA\python\pbp\202303050BRK.html', 'r') as file:
#     html = file.read()

# Parse the HTML content of the page
#soup = BeautifulSoup(page.content, 'html.parser')
soup = BeautifulSoup(html, 'html.parser')
game_link = []
# Find the table in the HTML content
table = soup.find('table', id='schedule')
for i in range(2,len(soup.find('table',id='schedule').find_all('tr'))):
    try:
        game = soup.find('table',id='schedule').find_all('tr')[i].find_all('td')[5].find('a')['href']
        game_link.append(game)
    except:
        pass

b = open(r"C:\Users\PSY\Documents\NEBA_new\gamelist\gamelinks_{}_{}.txt".format(season, month), 'w')
for link in game_link:
    b.write(link + '\n')
b.close()

# with open(r'C:\Users\PSY\Documents\NEBA_new\gamelist\gamelinks_{}_{}.txt'.format(season, month), 'w') as b:
#  for link in game_link:
#      b.write(link + '\n')

# with open('gamelinks_{}_{}.txt'.format(season, month), 'w') as b:
#  for link in game_link:
#      b.write(link + '\n')

# #Extract the data from the table
# rows = table.find_all('tr')
# for row in rows:
#     cells = row.find_all('td')
#     for cell in cells:
#         print(cell.text)
# #Create a new workbook and worksheet
# wb = Workbook()
# ws = wb.active
#
# # Write the data to the worksheet
# rows = table.find_all('tr')
# for row_idx, row in enumerate(rows, 1):
#     cells = row.find_all('td')
#     for col_idx, cell in enumerate(cells, 1):
#         ws.cell(row=row_idx, column=col_idx, value=cell.text)
#
# # Save the workbook to a file
# wb.save(r'C:\Users\PSY\Documents\NEBA\python\pbp\test.xlsx')