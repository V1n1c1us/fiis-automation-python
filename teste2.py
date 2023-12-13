import requests
import pandas as pd
import os.path
from bs4 import BeautifulSoup as bs

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

url = "https://www.fundsexplorer.com.br/ranking"

HEADERS = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = "177JBV5htm4YzmLIILYSBJN29KmBRRWuhztbtGsC9Hm4"
SAMPLE_RANGE_NAME = "Class Data!A2:E"


creds = None
# The file token.json stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("credentials.json", SCOPES)

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