from time import sleep
import re, os
from bs4 import BeautifulSoup as bsp
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
t = open(r'H:\NEBA_new\name_list_2023.txt','r')
name_links = [x.replace('\n','') for x in t.readlines()]
t.close()
result_list = []
for name in name_links:
    alphabet = name[0]
    path = r'H:\NEBA_new\name\{}.html'.format(alphabet)
    htmlfile = open(path, 'r', encoding='utf-8')
    htmlhandle = htmlfile.read()
    soup = bsp(htmlhandle, 'html.parser')
    th_label = soup.find('th',{'data-append-csv': '{}'.format(name)})
    if th_label is not None:
        # Find the hyperlink in the th label
        hyperlink = th_label.find('a')
        result_list.append(hyperlink.contents)
c = open(r'H:\NEBA_new\result_list_2023.txt','w')
for item in result_list:
    c.write(''.join(item))
    c.write('\n')
c.close()