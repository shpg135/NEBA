from bs4 import BeautifulSoup

path = "I:\\test\\plumus\\201112260DAL.html"
htmlfile = open(path, 'r', encoding='utf-8')
html = htmlfile.read()


# parse the HTML code
soup = BeautifulSoup(html, 'html.parser')

# find all the player-plusminus divs
plusminus_divs = soup.find_all('div', {'class': 'player-plusminus'})

# initialize the sum of the widths to zero
sum_widths = 0

# initialize the quarter to 1
quarter = 1

# loop through all the player-plusminus divs
for div in plusminus_divs:
    # get the widths of the divs
    widths = [int(w['style'].split(':')[1].strip('px;')) for w in div.find_all('div') if w.has_attr('style')]
    # calculate the sum of the widths
    sum_widths += sum(widths)
    # check if the sum of the widths has changed
    if sum_widths % 1005 != 0:
        # if the sum has changed, print the substitution
        if sum_widths // 1005 != quarter:
            quarter = sum_widths // 1005
            if sum_widths % 1005 < 500:
                print(f'Substitution at the end of Q{quarter-1}: {div.previous_sibling.text} off, {div.previous_sibling.previous_sibling.text} on')
            else:
                print(f'Substitution at the start of Q{quarter}: {div.previous_sibling.text} on, {div.previous_sibling.previous_sibling.text} off')
