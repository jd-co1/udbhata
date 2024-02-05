import pandas as pd
import streamlit as st
# from country_risk_web_scraping import ease_of_doing_business,Competitiveness_Index,trading_economics,Corruption_Perceptions_Index

import pymongo
# client=pymongo.MongoClient('mongodb://localhost:27017/')
# mydb=client['drreddy']
# information=mydb.info
client=pymongo.MongoClient('mongodb+srv://test:test@cluster0.tw5ieeh.mongodb.net/?retryWrites=true&w=majority')

mydb=client.get_database('Udbhata')
information=mydb.companies_data


def country_risk():
    data=pd.read_excel("Country_Risk_Summary_Table_1.xlsx",header=None)
    # data=pd.read_csv("Country_risk.csv",header=None)

    df=pd.DataFrame(data)
    # df = df.drop(df.index[:5]).reset_index(drop=True)
    matched=df[df.loc[:,0]=='IND']


    for index,row in matched.iterrows():
        w=row.iloc[2:]
        # w=pd.DataFrame(w)
    
    return w
# print(country_risk())

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
# chrome_options = Options()
# chrome_options.add_argument("--headless=new")
# driver = webdriver.Chrome(options=chrome_options)
driver = webdriver.Chrome()
def Corruption_Perceptions_Index():
    url = "https://www.transparency.org/en/countries/india"

    driver.get(url)
    driver.maximize_window()

    def wait_for_element(selector,delay=10):
            return WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, selector)))
    rank=wait_for_element("/html/body/main/div[4]/section[1]/div/section[1]/div[1]/div[1]/p[2]").text
    return rank
    # print(rank)

def Competitiveness_Index():
      url=f"https://worldcompetitiveness.imd.org/Copyright?returnUrl=%2Fcountryprofile%2FIN%2Fwcy"
      driver.get(url)
      driver.maximize_window()
      driver.implicitly_wait(20)
      def wait_for_element(selector,delay=70):
            return WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, selector)))
      accept=wait_for_element("/html/body/div[6]/div/div/div/a[2]/span")
      accept.click()
      index=wait_for_element("/html/body/div[3]/div/section[1]/div[1]/div[2]/p").text
      numeric_part = index.split(" ")[0]  # Get the first part of the string
      numeric_value = ''.join(filter(str.isdigit, numeric_part))  # Remove non-numeric characters
      # print(numeric_value)
      return numeric_value

# print(Competitiveness_Index())


def ease_of_doing_business():
      url="https://archive.doingbusiness.org/en/data/exploreeconomies/india"

      driver.get(url)
      driver.maximize_window()
      # driver.implicitly_wait(10)
      def wait_for_element(selector,delay=20):
            return WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, selector)))

      db_rank=wait_for_element("/html/body/div[5]/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div/div/div[1]/div[2]/table/tbody/tr[1]/td[2]").text
      
      # print(db_rank)
      return db_rank

# print(ease_of_doing_business())
      

def trading_economics():
      driver=webdriver.Chrome()
      url="https://tradingeconomics.com/country-list/rating"
      driver.get(url)
      # driver.maximize_window()
      driver.minimize_window()
    #   actions = ActionChains(driver)
      # driver.implicitly_wait(10)
      def wait_for_element(selector,delay=20):
            return WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, selector)))
      # driver.execute_script('document.getElementsByTagName("html")[0].style.scrollBehavior = "auto"')
      row=wait_for_element("/html/body/form/div[5]/div/div[1]/div[1]/div/table/tbody/tr[63]")
      columns = row.find_elements(By.TAG_NAME, 'td')
      # column=[]
      # Iterate through columns and print the text
      # for column in columns:
      #       print(column.text)
      
      # rating=wait_for_element("/html/body/form/div[5]/div/div[1]/div[1]/div/table/tbody/tr[63]/td[5]/span/text")
      # rating=wait_for_element('//*[@id="ctl00_ContentPlaceHolder1_ctl01_GridView1"]/tbody/tr[63]/td[5]/span')
      # actions.move_to_element(rating).perform()
      # wait_for_element("//text")
      # rating=rating.text
      return columns

# print(trading_economics()[2].text.upper())

def credit_ratings_algo():
      data=pd.read_csv("credit_ratings.csv")
      df=pd.DataFrame(data)
      # print(df)
      cr=trading_economics()
      if len(cr) >= 4:
        cr_sp = cr[1].text.upper()
        cr_moodys = cr[2].text
        cr_fitch = cr[3].text.split()[0].upper()

        filtered_df1= df.loc[df['S&P'].isin([cr_sp])].iloc[0]['Grade'] if not df.loc[df['S&P'].isin([cr_sp])].empty else None
        filtered_df2 = df.loc[df["Moody's"].isin([cr_moodys])].iloc[0]['Grade'] if not df.loc[df["Moody's"].isin([cr_moodys])].empty else None
        filtered_df3 = df.loc[df["Fitch"].isin([cr_fitch])].iloc[0]['Grade'] if not df.loc[df["Fitch"].isin([cr_fitch])].empty else None
      # print(filtered_df1,filtered_df2,filtered_df3)
        avg=(filtered_df1+filtered_df2+filtered_df3)/3
      return round(avg)
# print(credit_ratings_algo())

# print(trading_economics())

def Terror():
    data=pd.read_csv("terror_impact.csv")
    df=pd.DataFrame(data)

    matched = df[df['COUNTRY'].str.strip().str.lower() == 'India'.strip().lower()].iat[0, 1]
    return matched

def stre(option):
    k=information.find_one({"name":f"{option}"})
    if 'country_risk' in k:
                    data_dict=k['country_risk']
    # Extract values from data_dict
                    esg_data = data_dict

                        # Create a list of dictionaries to represent the data
                    data_list = []
                    for esg_item in esg_data:
                              esg_dict = {
                                    'Question': esg_item.get('Metric', ''),
                                    'Value': esg_item.get('Value', '')
                              }
                              data_list.append(esg_dict)
                              df=pd.DataFrame(data_list)
                              matched=df['Value'].to_list()
    else:

            data = {
                      'Metric': ['Political Risk Short Term', 
                                 'Political Risk Medium/Long Term',
                                   f' Premium classification OECD', 
                                  #  'Commercial Risk',
                                     'Business environment risk','Political Violence Risk',
                                     'Expropriation and Government Action Risk',
                                     'Currency Inconvertibility and Transfer Restriction Risk',
                                     'Corruption Perception Index',
                                     'Ease of Doing Business Rank',
                                     'Economic Risk (credit rating)',
                                     'Competitiveness Index',
                                     'Golbal Terrorism Impact'],
                      'Value': [
                          country_risk()[2],
                          country_risk()[3],
                          country_risk()[4],
                          # country_risk()[5],
                          country_risk()[6],
                          country_risk()[7],
                          country_risk()[8],
                          country_risk()[9],
                          Corruption_Perceptions_Index(),
                          ease_of_doing_business(),
                        #   trading_economics(),
                          credit_ratings_algo(),
                          Competitiveness_Index(),
                          Terror()
                      ]
                  }
            df=pd.DataFrame(data)
            data_dict = df.to_dict(orient='records')
            print(df)
            matched=df['Value'].to_list()
            print(matched)

            information.update_one({"name":f"{option}"},{"$set":{
                                                "country_risk":data_dict
                    }})
#     information.insert_one({"country_risk":matched})
    
#   print(matched)
    return matched
# print(stre('drreddy'))



