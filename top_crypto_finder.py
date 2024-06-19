from bs4 import BeautifulSoup
import requests

url = "https://coinmarketcap.com/"

def input_():
    num = int(input("Top ___ Crypto Coins at the moment are: "))
    while num > 10 or num < 1:
        print("Enter a number between 1-10")
        num = int(input("Top ___ Crypto Coins at the moment are: "))
    return num 

def top_crypto():
    num = input_()
    result = requests.get(url).text
    doc = BeautifulSoup(result, "html.parser")
    tbody = doc.find('tbody')
    trs = tbody.find_all('tr')
    
    count = 1
    for tr in trs[:num]:
        tds = tr.find_all('td')
        
        name = tds[2].find('a', class_='cmc-link')
        price = tds[3].find('span')

        try:
            coin = name.contents[1].text
        except:
            coin = name.find('p').text
        
        price_num = price.text if price else 'N/A'
        
        print("#", count, " ", coin, ': ', price_num)
        print()
        count += 1

top_crypto()
3