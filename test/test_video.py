from bs4 import BeautifulSoup

path = r"H:\NBA\video.html"
htmlfile = open(path, 'r', encoding='utf-8')
html = htmlfile.read()
# parse the HTML code
soup = BeautifulSoup(html, 'html5lib')
head_div = soup.find_all('div')
test = 0
if 'Full' in head_div.title:
    print(head_div.title)

    #.find('div', {'id': 'meta'}).find('a')
