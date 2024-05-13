import unittest
import random

import pandas as pd
import csv
import requests
import time
import os


if __name__ == '__main__':

    save_dir = r"C:\Users\PSY\Documents\NEBA\python\boxscore"
    headers = {
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
    }
    session = requests.Session()
    pbp_list = ['199703230LAC.html',
'200704180IND.html',
'200812180ORL.html',
'201410290CHO.html',
'201604010CHO.html',
'202104020POR.html',
'202203300OKC.html']


    for pbp in pbp_list:
        time.sleep(2)
        url = "https://www.basketball-reference.com/boxscores/plus-minus/" + pbp
        response = session.get(url, headers=headers)

        with open(os.path.join(save_dir, pbp), 'w', encoding='utf-8') as f:
            f.write(response.text)

