import requests
import time
import os
#change url
url = 'https://www.basketball-reference.com/boxscores/202305090DEN.html'
#change file name
file_name = '202305090DEN.html'
#change target folder
target_folder ='/ssd/'
headers = {
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
    }
session = requests.Session()
response = session.get(url, headers=headers)
with open(os.path.join(target_folder, file_name), 'w', encoding='utf-8') as f:
    f.write(response.text)