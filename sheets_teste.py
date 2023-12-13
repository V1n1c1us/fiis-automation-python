import requests
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from bs4 import BeautifulSoup as bs
from lxml import etree
from typing import List

URL = "https://statusinvest.com.br/fundos-imobiliarios/hctr11"
HEADERS = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
URLS = [
    "https://statusinvest.com.br/fundos-imobiliarios/hctr11",
    "https://statusinvest.com.br/fundos-imobiliarios/mxrf11",
    "https://statusinvest.com.br/fundos-imobiliarios/vslh11",
    "https://statusinvest.com.br/fundos-imobiliarios/irdm11"
    ]

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = "177JBV5htm4YzmLIILYSBJN29KmBRRWuhztbtGsC9Hm4"
SAMPLE_RANGE_NAME = "Automation!A2:B12"

HEADERS = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def main():
  """Shows basic usage of the Sheets API.
  Prints values from a sample spreadsheet.
  """
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
    service = build("sheets", "v4", credentials=creds)

    # Ler informações Call the Sheets API
    sheet = service.spreadsheets()
    result = (
        sheet.values()
        .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
        .execute()
    )

    values = result.get("values", [])
    
    dados = []
    for valores in values:
        page = requests.get(valores[1], headers=HEADERS)
        soup = bs(page.content, "html.parser")
        
        dados.append({
            # "Valor Atual": soup.find("strong", {"class":"value"}).text,
            "Dividend Yield": soup.find_all("strong", {"class":"value"})[3].text,
            # "Valorização (12M)": soup.find_all("strong", {"class":"value"})[4].text,
        })
      
    print(dados)

    result_list = [[key, value] for item in dados for key, value in item.items()]

    valores_adicionar = [
      ['YIELD'],
    ]
    
    for i, linha in enumerate(result_list):
      if i > 0:
        field = linha[1]
        valores_adicionar.append([field])
        res = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="Automation!C1", valueInputOption="RAW", body={'values': valores_adicionar}).execute()  
    
    
    
    print(result_list)
  
   
    # with open('dados.txt', 'w') as file:
    #     file.write(str(dados))
    # add = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="Automation!A14", valueInputOption="RAW", body={'dados': [['opa']]}).execute()  

    if not values:
      print("No data found.")
      return

    print("Name, Major:")
    # for row in values:
    #   # Print columns A and E, which correspond to indices 0 and 4.
    #   print(f"{row[0]}, {row[4]}")
  except HttpError as err:
    print(err)


if __name__ == "__main__":
  main()
