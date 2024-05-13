from bs4 import BeautifulSoup as bsp
import sys
import io
import string
import os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
#alphabet = 'c'
output = '/ssd/NEBA_new/output/namelist.csv'
try:
    # 尝试删除文件
    os.remove(output)
except OSError as e:
    print()

alphabet_list = list(string.ascii_lowercase[0:])
for alphabet in alphabet_list:
    path = "/ssd/NEBA_new/name/{}.html".format(alphabet)
    htmlfile = open(path, 'r', encoding='utf-8')
    htmlhandle = htmlfile.read()
    result_list = []
    soup = bsp(htmlhandle, 'html.parser')
    table = soup.find('table',id='players')
    list = table.find_all('th', {'class': 'left'})
    for th_label in list:
        hyperlink = th_label.find('a')
        key = hyperlink.attrs.get('href').split('/')[3].split('.')[0]
        value = str(hyperlink.contents)
        result_list.append([key,value])

    y = open(output,'a')
    for line in result_list:
        y.write('\n' + ','.join([str(d) for d in line]))