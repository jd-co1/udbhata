from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By 
import pandas as pd
url="https://www.bseindia.com/stock-share-price/sun-pharmaceutical-industries-ltd/sunpharma/524715/corporate-governance/"
driver = webdriver.Chrome()
driver.get(url)
html = driver.page_source
driver.maximize_window()

soup = BeautifulSoup(html, 'lxml')

div = soup.find_all("div",class_ = "largetable")

table=div[1].find_all('table',class_ ="ng-scope")

row=table[1].find_all('tr')
td=row[0].find_all('td')

tenure=td[11].text

data=[]
for i in range(2,len(row)):
    td=row[i].find_all("td")
    k=td[15].text
    data.append({'Tenure': k})
df=pd.DataFrame(data)

df['Tenure'] = pd.to_numeric(df['Tenure'], errors='coerce')
# print(df)
average_tenure = df['Tenure'].mean()
print("average tenure of Sun Pharma directors:",average_tenure)
    



