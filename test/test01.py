from bs4 import BeautifulSoup

html = '''<table>
            <tr data-row="0"><td>Row 0</td></tr>
            <tr data-row="1"><td>Row 1</td></tr>
            <tr data-row="2"><td>Row 2</td></tr>
         </table>'''

soup = BeautifulSoup(html, 'html.parser')
tr_tag = soup.find('tr', {'data-row': '0'})
print(tr_tag)