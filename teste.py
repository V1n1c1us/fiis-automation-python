import requests
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



def ws(urls: List[str]) -> list:
    # page = requests.get(url, headers=HEADERS)
    # soup = bs(page.content, "html.parser")
    
    
    dados = []
    for url in urls:
         page = requests.get(url, headers=HEADERS)
         soup = bs(page.content, "html.parser")
        
         dom = etree.HTML(str(soup)) 
         
         dados.append({
            "Nome": dom.xpath('//*[@id="main-header"]/div[2]/div/div[1]/h1')[0].text,
            "Valor Atual": soup.find("strong", {"class":"value"}).text,
            "Dividend Yield": soup.find_all("strong", {"class":"value"})[3].text,
            "Valorização (12M)": soup.find_all("strong", {"class":"value"})[4].text,
         })
        
    with open('dados.txt', 'w') as file:
        file.write(str(dados))
        # tickersBox2 = soup.find("strong", {"class":"value"}).text

    # tickersBox = soup.find("div", {"class":"d-md-inline-block"})
    # tickersBox2 = soup.find("strong", {"class":"value"}).text


    # te = soup.find('div', {'id':'dy-info'}),
    # te2 = soup.find_all('div', {'id':'dy-info'}),
    
#dy-info > div > div.d-flex.align-items-center > strong
    # teste = {
    #     "Valor Atual": soup.find("strong", {"class":"value"}).text,
    #     "Dividend Yield": soup.find_all("strong", {"class":"value"})[3].text,
    #     "Valorização (12M)": soup.find_all("strong", {"class":"value"})[4].text,
    #     "Ultimo Rendimento": {
    #         "Valor": soup.find_all('div', {'class':'info'})[0].text,
    #         "Rendimento": soup.find_all('b', {'class':'sub-value'})[0].text,
    #         "Cotação Base": soup.find_all('b', {'class':'sub-value'})[0].text,
    #         "Data Base": soup.find_all('b', {'class':'sub-value'})[0].text,
    #         "Data Pagamento": soup.find_all('b', {'class':'sub-value'})[4].text,
    #     },
    #     "Dividendos": {
    #         "Tipo": soup.find_all('td')[0].text,
    #         "Data COM": soup.find_all('td')[1].text,
    #         "Pagamento": soup.find_all('td')[2].text,
    #         "Valor": soup.find_all('td')[3].text,
    #     }
    # }

    

    # print(dados)
    # _fiss = []
    # for fii in tickersBox:
    #     _fiss.append(
    #         {
    #             "ticker": fii.find("div", {"class":"tickerBox__title"}).text,
    #             "dy": fii.find_all("div", {"class":"tickerBox__info__box"})[0].text
    #         }
    #     )
    


def main():
    fiis = ws(URLS)


if __name__ == "__main__":
    main()

# response = requests.get('https://www.fundsexplorer.com.br/funds/vilg11').content

# dados = BeautifulSoup(response, 'html.parser')

# price = dados.find('div > p', class_ ="headerTicker__content__price")
# print(price)

# # <div class="headerTicker__content__price">
# # <p>R$ 93,30</p><span class="alta">2,11%</span>
# # </div>