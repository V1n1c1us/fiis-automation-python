import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

url = "https://www.fundsexplorer.com.br/ranking"

HEADERS = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

page = requests.get(url, headers=HEADERS)
soup = bs(page.content, "html.parser")

table = soup.find('table')

df = pd.DataFrame(columns=['Código'])

for row in table.find_all('tr'):
    columns = row.find_all('td')
    if(columns != []):
        cot = columns[0].text.strip(' ')
        df = pd.concat([df, pd.DataFrame.from_records([{ 'Cotação': cot }])])

df.head()        

breakpoint()
# import requests
# import pandas as pd
# from bs4 import BeautifulSoup as bs

# url = "https://www.fundamentus.com.br/detalhes.php?papel=MXRF11"

# HEADERS = {
#     'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 \
#         (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
# }

# page = requests.get(url, headers=HEADERS)
# soup = bs(page.content, "html.parser")

# table = soup.find('table')

# df = pd.DataFrame(columns=['Cotação', 'teste', 'teste2'])

# for row in table.find_all('tr'):
#     columns = row.find_all('td')
#     if(columns != []):
#         fii = columns[1].text.strip(' ')
#         nome = columns[2].text.strip(' ')
#         te = columns[3].text.strip(' ')
#         te2 = columns[0].text.strip(' ')
#         df = pd.concat([df, pd.DataFrame.from_records([{ 'Cotação': nome, 'teste': te, 'teste2': te2 }])])

# df.head(20)        

# breakpoint()