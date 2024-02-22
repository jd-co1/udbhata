import pandas as pd
import streamlit as st
# from country_risk_web_scraping import ease_of_doing_business,Competitiveness_Index,trading_economics,Corruption_Perceptions_Index

import pymongo
# client=pymongo.MongoClient('mongodb://localhost:27017/')
# mydb=client['drreddy']
# information=mydb.info
client=pymongo.MongoClient('mongodb+srv://test:test@cluster0.tw5ieeh.mongodb.net/?retryWrites=true&w=majority')

mydb=client.get_database('Udbhata')
information=mydb.countries_data


def country_risk(option):
    data=pd.read_excel("Country_Risk_Summary_Table_1.xlsx",header=None)
    # data=pd.read_csv("Country_risk.csv",header=None)

    df=pd.DataFrame(data)
    # df = df.drop(df.index[:5]).reset_index(drop=True)
    matched=df[df.loc[:,1]==f'{option}']


    for index,row in matched.iterrows():
        w=row.iloc[2:]
        # w=pd.DataFrame(w)
    
    return w
# print(country_risk("United Kingdom"))

#Country risk from external sources
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
import string
import requests
chrome_options = Options()
chrome_options.add_argument("--headless=new")
# driver = webdriver.Chrome(options=chrome_options)
driver = webdriver.Chrome()
def Corruption_Perceptions_Index(option):
    if ' ' in option:
          words=option.split()
          option="-".join(word.lower() for word in words)
    else:
        option=option.lower()
    url = f"https://www.transparency.org/en/countries/{option}"

    driver.get(url)
    driver.maximize_window()

    def wait_for_element(selector,delay=10):
            return WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, selector)))
    allow=wait_for_element('//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]')
    allow.click()
    
    rank=wait_for_element('//*[@id="cpi"]/div[1]/div[1]/p[2]').text
    return rank
    # print(rank)
# print(Corruption_Perceptions_Index("israel"))
def Competitiveness_Index(option):
      data=pd.read_excel("Competitiveness_2023.xlsx",header=None)
      df=pd.DataFrame(data)
      df.set_index(0,inplace=True)
      if option=='United States':
            option='USA'
      matched=df.loc[option][1]
      return matched

# print(Competitiveness_Index())


def ease_of_doing_business(option):
      url="https://archive.doingbusiness.org/en/data"

      driver.get(url)
      driver.maximize_window()
      # driver.implicitly_wait(10)
      def wait_for_element(selector,delay=20):
            return WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, selector)))
      click=wait_for_element("/html/body/div[3]/div/div/div/div/div/div[3]/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div[2]/div/span/span/span[1]")
      click.click()
      input=wait_for_element('//*[@id="economylist-list"]/span/input')
      time.sleep(2)
      input.send_keys(f"{option}")
      time.sleep(2)
      input.send_keys(Keys.ENTER)
      db_rank=wait_for_element("/html/body/div[5]/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div/div/div[1]/div[2]/table/tbody/tr[1]/td[2]").text
      time.sleep(5)
      # print(db_rank)
      return db_rank

# print(ease_of_doing_business())
      

# 
def trading_economics(option):
    if ' ' in option:
          words=option.split()
          option="-".join(word.lower() for word in words)
    else:
        option=option.lower()
    url=f"https://www.fxempire.com/macro/credit-ratings/{option}"
    driver = webdriver.Chrome()
    driver.get(url)
    # html = driver.page_source
    driver.maximize_window()

    def wait_for_element(selector,delay=20):
                return WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, selector)))

    tr=wait_for_element('//*[@id="content"]/div[2]/div[7]/div/div[3]/div/div/table/tbody/tr')
    td=tr.find_elements(By.XPATH, ".//td")
    td_vals=[td.text for td in td]
    return td_vals
# print(trading_economics("United Kingdom"))

def credit_ratings_algo(option):
      data=pd.read_csv("credit_ratings.csv")
      df=pd.DataFrame(data)
      # print(df)
      cr=trading_economics(option)
      print(cr)
      if len(cr) >= 3:
        cr_moodys = cr[0]
        cr_sp = cr[2].upper()
        cr_fitch = cr[4].split()[0].upper()

        filtered_df1= df.loc[df['S&P'].isin([cr_sp])].iloc[0]['Grade'] if not df.loc[df['S&P'].isin([cr_sp])].empty else None
        filtered_df2 = df.loc[df["Moody's"].isin([cr_moodys])].iloc[0]['Grade'] if not df.loc[df["Moody's"].isin([cr_moodys])].empty else None
        filtered_df3 = df.loc[df["Fitch"].isin([cr_fitch])].iloc[0]['Grade'] if not df.loc[df["Fitch"].isin([cr_fitch])].empty else None
      # print(filtered_df1,filtered_df2,filtered_df3)
        avg=(filtered_df1+filtered_df2+filtered_df3)/3
      return round(avg)
# print(credit_ratings_algo('United Kingdom'))      

# print(trading_economics())

def Terror(option):
    data=pd.read_csv("terror_impact.csv")
    df=pd.DataFrame(data)
    # if option=='United States':

    matched = df[df['COUNTRY'].str.strip().str.lower().str.contains(option.strip().lower())].iat[0, 1]
    return matched
# print(Terror("UNITED states"))
def stre(option):
    k=information.find_one({"name":f"{option}"})
    if k:
      matched=[]
      exclude_indices = [0, 1]  # Define indices to exclude
      for index, (key, value) in enumerate(k.items()):
            if index not in exclude_indices:
                matched.append(value)
                # print(f'{key}: {value}')
      return matched
    
    else:
            data = {
                      'name':f'{option}',
                      'Political Risk Short Term':country_risk(option)[2],
                      'Political Risk Medium/Long Term':country_risk(option)[3],
                      'Premium classification OECD':country_risk(option)[4],
                      'Business environment risk':country_risk(option)[6],
                      'Political Violence Risk':country_risk(option)[7],
                      'Expropriation and Government Action Risk':country_risk(option)[8],
                      'Currency Inconvertibility and Transfer Restriction Risk':country_risk(option)[9],
                      'Corruption Perception Index':Corruption_Perceptions_Index(option),
                      'Ease of Doing Business Rank':ease_of_doing_business(option),
                      'Economic Risk (credit rating)':credit_ratings_algo(option),
                      'Competitiveness Index':Competitiveness_Index(option),
                      'Golbal Terrorism Impact':Terror(option)
                      
                  }         
            df = pd.DataFrame.from_dict(data, orient='index', columns=['Value'])

            # Reset the index to have metrics as a separate column
            df.reset_index(inplace=True)
            df.rename(columns={'index': 'Metric'}, inplace=True)
            print(df)
            matched=df['Value'].to_list()
            print(matched)
            information.insert_one(data)
            
#     information.insert_one({"country_risk":matched})
    
#   print(matched)
    return matched
# print(stre('Israel'))



