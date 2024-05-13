from bs4 import BeautifulSoup

path = r"I:\ssd\playoffs\2002\boxscore\200204200SAC.html"
htmlfile = open(path, 'r', encoding='utf-8')
html = htmlfile.read()
# parse the HTML code
soup = BeautifulSoup(html, 'html.parser')
head_div = soup.find_all('div', {'class': 'scores'})
away_series = head_div[0].next_sibling.text
home_series = head_div[1].next_sibling.text
print(away_series)
print(home_series)


# import requests
# from bs4 import BeautifulSoup
#
# # URL of the game to scrape
# #url = "https://www.basketball-reference.com/boxscores/202008180IND.html"
# path = r"I:\ssd\playoffs\2002\boxscore\200204200SAC.html"
# htmlfile = open(path, 'r', encoding='utf-8')
# html = htmlfile.read()
# soup = BeautifulSoup(html, 'html.parser')
# # Make a GET request to the URL
# #response = requests.get(url)
#
# # Parse the HTML content using BeautifulSoup
# #soup = BeautifulSoup(response.content, 'html.parser')
#
# # Find the <div> element that contains the final score
# score_div = soup.find_all('div', {'class': 'score'})
#
# # Extract the final score from the <div> element
# final_score = score_div[0].get_text()
#
# print("Final Score:", final_score)
