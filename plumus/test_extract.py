from bs4 import BeautifulSoup

path = "I:\\test\\plumus\\201112260DAL.html"

def getstarter(path):

    htmlfile = open(path, 'r', encoding='utf-8')
    html = htmlfile.read()


    # parse the HTML code
    soup = BeautifulSoup(html, 'html.parser')
    head_div = soup.find('div', {'class': 'header'})
    widths = [int(w['style'].split(':')[1].strip('px;')) for w in head_div.find_all('div')]
    quarter_break = []
    for i in range(len(widths)):
        if i == 0:
            #quarter_break.append(widths[i])
            quarter_break.append(0)
        else:
            quarter_break.append(widths[i]+quarter_break[i-1])
    quarter_break = [x + 1 for x in quarter_break]
    # find all the player-plusminus divs
    plusminus_divs = soup.find_all('div', {'class': 'player-plusminus'})

    # initialize the sum of the widths to zero
    sum_widths = 0

    # initialize the quarter to 1
    quarter = 1
    result = []
    # loop through all the player-plusminus divs
    for div in plusminus_divs:

        width = []
        count = 0
        for w in div.find_all('div'):
            if w.has_attr('style'):
                if w.has_attr('class'):
                    width.append([w['style'].split(':')[1].strip('px;'),'on'])
                else:
                    width.append([w['style'].split(':')[1].strip('px;'), 'off'])

        is_on_court = []

        time_on_court = 0
        i = 0
        name = div.previous_sibling.previous_sibling.text.split('(')[0]
        if name[-1] == " ":
            name = name[:-1]
        for slot in quarter_break:
            # if i == 0:
            #     is_on_court.append(width[i][1] == 'on' if i == 0 else False)
            #     time_on_court += int(width[i][0])
            #     i += 1
            #     continue
            while i < len(width) and time_on_court + int(width[i][0]) <= slot:
                # if player_schedule[i][1] == 'on':
                time_on_court += int(width[i][0])
                i += 1


            is_on_court.append(width[i][1] == 'on' if i >= 0 else False)
        result.append([name,is_on_court])
    return result

result = getstarter(path)
quarter_len = len(result[0][1])
for i in range(quarter_len):
    print('quarter{}:'.format(i+1))
    for item in result:
        if item[1][i] == True:
            print(item[0])


