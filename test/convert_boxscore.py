import csv
import re, os
import datetime
from datetime import datetime
from bs4 import BeautifulSoup as bsp
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
season = 'test'
season_list = list(range(1997, 2023))
file = "201104160CHI.html"
# for season in season_list:
#     box_dir = "/ssd/ssd/playoffs/{}/boxscore".format(season)
#     files = os.listdir(box_dir)

def convert_box(file):
    f_name = str(season-1) + '-' + str(season)
    path = r"I:/NEBA_new/boxscore/season/{}/".format(f_name)


    path = path + file
    result = []
    htmlfile = open(path, 'r', encoding='utf-8')
    htmlhandle = htmlfile.read()
    soup = bsp(htmlhandle, 'html.parser')
    awayTeam, homeTeam = [x.split('/')[2] for x in
                                  [a['href'] for a in soup.find('div', class_='scorebox').find_all('a') if
                                   'teams' in a['href']]]
    awayFinScore = soup.find_all('div', class_='score')[0].get_text()
    homeFinScore = soup.find_all('div', class_='score')[1].get_text()
    if int(awayFinScore) > int(homeFinScore):
        winningTeam = awayTeam
        losingTeam = homeTeam
    elif int(awayFinScore) < int(homeFinScore):
        winningTeam = homeTeam
        losingTeam = awayTeam
    dog = ' '.join(
        soup.find('div', class_='scorebox').find('div', class_='scorebox_meta').find('div').get_text().split(', ')[
        1:]).replace(',', '')
    datetime_object = datetime.strptime(dog, "%B %d %Y")
    dog = datetime_object.strftime("%Y-%m-%d")
    #print (dog)
    awayFullTable = soup.find('table',id ='box-{}-game-basic'.format(awayTeam)).find_all('tr')
    homeFullTable = soup.find('table',id ='box-{}-game-basic'.format(homeTeam)).find_all('tr')

    for tr in awayFullTable:
        try:
            th_label = tr.find('th', {'class', 'left'})
            hyperlink = th_label.find('a')
            content = hyperlink.contents[0]
            print (content)
        except:
            continue
        try:
            player = tr.contents[0].text
            mp = tr.contents[1].text
            mp_convert = round((int(mp.split(':')[0])+int(mp.split(':')[1])/60),1)
            fg = tr.contents[2].text
            fga = tr.contents[3].text
            fg_pct = tr.contents[4].text
            fg3 = tr.contents[5].text
            fg3a = tr.contents[6].text
            fg3_pct = tr.contents[7].text
            ft = tr.contents[8].text
            fta = tr.contents[9].text
            ft_pct = tr.contents[10].text
            orb = tr.contents[11].text
            drb = tr.contents[12].text
            trb = tr.contents[13].text
            ast = tr.contents[14].text
            stl = tr.contents[15].text
            blk = tr.contents[16].text
            tov = tr.contents[17].text
            pf = tr.contents[18].text
            pts = tr.contents[19].text
            plus_minus = tr.contents[20].text
            belong_team = awayTeam
            result.append([file,dog,homeTeam,awayTeam,homeFinScore,awayFinScore,winningTeam,losingTeam,belong_team,player,mp_convert,fg,fga,fg_pct,fg3,fg3a,fg3_pct,ft,fta,ft_pct,orb,drb,trb,ast,stl,blk,tov,pf,pts,plus_minus])
        except:
            pass

        for tr in homeFullTable:
            try:
                th_label = tr.find('th', {'class', 'left'})
                hyperlink = th_label.find('a')
                content = hyperlink.contents[0]
                print(content)
            except:
                continue
            try:
                player = tr.contents[0].text
                mp = tr.contents[1].text
                mp_convert = round((int(mp.split(':')[0]) + int(mp.split(':')[1]) / 60), 1)
                fg = tr.contents[2].text
                fga = tr.contents[3].text
                fg_pct = tr.contents[4].text
                fg3 = tr.contents[5].text
                fg3a = tr.contents[6].text
                fg3_pct = tr.contents[7].text
                ft = tr.contents[8].text
                fta = tr.contents[9].text
                ft_pct = tr.contents[10].text
                orb = tr.contents[11].text
                drb = tr.contents[12].text
                trb = tr.contents[13].text
                ast = tr.contents[14].text
                stl = tr.contents[15].text
                blk = tr.contents[16].text
                tov = tr.contents[17].text
                pf = tr.contents[18].text
                pts = tr.contents[19].text
                plus_minus = tr.contents[20].text
                belong_team = homeTeam
                result.append(
                    [file, dog, homeTeam, awayTeam, homeFinScore, awayFinScore, winningTeam, losingTeam, belong_team,
                     player, mp_convert, fg, fga, fg_pct, fg3, fg3a, fg3_pct, ft, fta, ft_pct, orb, drb, trb, ast, stl,
                     blk, tov, pf, pts, plus_minus])
            except:
                pass
        test = 0
        #print(mp)
    return result

season_folder = r"I:/ssd/regular/{}/boxscore/".format(season)
os.makedirs(season_folder, exist_ok=True)
y = open('{}{}_boxscore.csv'.format(season_folder,season),'a')
if os.stat('{}{}_boxscore.csv'.format(season_folder,season)).st_size == 0:
    y.write('URL,Date,HomeTeam,AwayTeam,HomeScore,AwayScore,WinningTeam,LosingTeam,Belong_Team,Player,Minute,FG,FGA,FG%,FG3,FG3A,FG3%,FT,FTA,FT%,ORB,DRB,TRB,AST,STL,BLK,TOV,PF,PTS,PLUMUS')

result = convert_box(file)
for play in result:
    y.write('\n' + ','.join([str(d) for d in play]))