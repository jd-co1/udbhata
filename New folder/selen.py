from bs4 import BeautifulSoup
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
import pandas as pd
chrome_options = Options()
chrome_options.add_argument("--headless=new")
driver = webdriver.Chrome(options=chrome_options)
# driver = webdriver.Chrome()
url="https://www.bseindia.com/"

driver.get(url)
driver.maximize_window()
time.sleep(3)
search=driver.find_element(by=By.XPATH,value="/html/body/div[1]/div[5]/div/div/div[3]/div/section/form/div[1]/input")
time.sleep(2)
search.send_keys("Drreddys")
time.sleep(1)
search.send_keys(Keys.ENTER)
time.sleep(2)
# driver.execute_script("return documet.body.scrollHeight")
driver.execute_script("window.scrollTo(0,1000)")
time.sleep(1)
# print(driver.page_source.encode("utf-8"))
driver.find_element(by=By.XPATH,value="/html/body/div[1]/div[4]/div[5]/div[7]/aside/div/div[3]/div[5]/div/div/h1/a").click()
time.sleep(6)
tbody=driver.find_element(by=By.XPATH,value="/html/body/div[1]/div[4]/div[5]/div[7]/div/div/ng-view/div/div[3]/div[1]/div[2]/div[1]/div[3]/table/tbody/tr/td/table/tbody")
time.sleep(2)
# print(tbody.text)
row=driver.find_elements(by=By.XPATH,value="/html/body/div[1]/div[4]/div[5]/div[7]/div/div/ng-view/div/div[3]/div[1]/div[2]/div[1]/div[3]/table/tbody/tr/td/table/tbody/tr")
# print(len(row))
column_values = [rows.find_elements(By.XPATH, ".//td")[15].text for rows in row]

# print(column_values)
df = pd.DataFrame({'Tenure': column_values})

# Print the DataFrame
print(df)
df['Tenure'] = pd.to_numeric(df['Tenure'], errors='coerce')
# print(df)
average_tenure = df['Tenure'].mean()
print("average tenure of  directors:",average_tenure)

# data=[]
# for tr in tbody.find_elements(by=By.XPATH,value="//tr"):
#     row=[item.text for item in tr.find_elements(By.XPATH,".//td")]
#     data.append(row)


# df=pd.DataFrame(data)
# print(df)