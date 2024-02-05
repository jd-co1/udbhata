from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import os, glob
import pymongo
client=pymongo.MongoClient('mongodb+srv://test:test@cluster0.tw5ieeh.mongodb.net/?retryWrites=true&w=majority')

mydb=client.get_database('Udbhata')
information=mydb.companies_data


def average_tenure_of_a_company(option):
        k=information.find_one({"name":f"{option}"})
        if 'average_tenure' in k:
                    average_tenure=k['average_tenure']
                    return average_tenure
        else:
                    chrome_options = Options()
                    chrome_options.add_argument("--headless=new")
                    # driver = webdriver.Chrome(options=chrome_options)
                    driver = webdriver.Chrome()
                    url = "https://www.bseindia.com/"

                    driver.get(url)
                    driver.maximize_window()
                    # driver.minimize_window()

                    def wait_for_element(selector,delay=20):
                        return WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, selector)))


                    # Search for the company
                    search = wait_for_element("/html/body/div[1]/div[5]/div/div/div[3]/div/section/form/div[1]/input")
                    search.send_keys(option)
                    time.sleep(2)
                    search.send_keys(Keys.ENTER)
                    # Scroll down the page
                    driver.execute_script('document.getElementsByTagName("html")[0].style.scrollBehavior = "auto"')

                    time.sleep(2)
                    company_link = wait_for_element("/html/body/div[1]/div[4]/div[5]/div[7]/aside/div/div[3]/div[5]/div/div/h1/a")
                    # Click on the link for the company
                    company_link.click()


                    # Wait for the table to be present
                    # table = wait_for_element("/html/body/div[1]/div[4]/div[5]/div[7]/div/div/ng-view/div/div[3]/div[1]/div[2]/div[1]/div[3]/table/tbody/tr/td/table/tbody/tr")

                    rows = wait_for_element("/html/body/div[1]/div[4]/div[5]/div[7]/div/div/ng-view/div/div[3]/div[1]/div[2]/div[1]/div[3]/table/tbody/tr/td/table/tbody").find_elements(By.XPATH, ".//tr")

                    column_values = [row.find_elements(By.XPATH, ".//td")[15].text if len(row.find_elements(By.XPATH, ".//td")) > 15 else None for row in rows]


                    # Create a DataFrame with the column name 'Tenure'
                    df = pd.DataFrame({'Tenure': column_values})

                    # Convert 'Tenure' to numeric, replace '-' with NaN
                    df['Tenure'] = pd.to_numeric(df['Tenure'], errors='coerce')


                    # Calculate and print the average tenure
                    average_tenure = df['Tenure'].mean()
                    print(average_tenure)
                    information.update_one({"name":f"{option}"},{"$set":{
                                                "average_tenure":average_tenure
                    }})
                    
                    return average_tenure
        


# print(average_tenure_of_a_company("drreddy"))



