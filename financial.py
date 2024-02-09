
import re
from concurrent.futures import ThreadPoolExecutor
import concurrent
# import streamlit as st
import pandas as pd
import pymongo
# client=pymongo.MongoClient('mongodb://localhost:27017/')

# mydb=client['drreddy']
# information=mydb.info
client=pymongo.MongoClient('mongodb+srv://test:test@cluster0.tw5ieeh.mongodb.net/?retryWrites=true&w=majority')

mydb=client.get_database('Udbhata')
information=mydb.companies_data

def Ebitda(option):
    k=information.find_one({"name":f"{option}"})
    if 'ebit/net_sales' in k:
            ebitda=k['ebit/net_sales']
            return ebitda

    else:
        # num_only=re.sub(r'\D', '',ebit)
        # information.insert_one({"ebitda":ebit})
        information.update_one({"name":f"{option}"},{"$set":{
                                                "ebitda":ebitda
                    }})
    return  ebitda
# print(Ebitda('drreddy'))


def debt_to_equity(option):
    k=information.find_one({"name":f"{option}"})

    if 'debt_to_equity' in k:
                    debt_to_equity=k['debt_to_equity']
                    return debt_to_equity
    else:
        # print(deb)
        # print(equi)
        # num_only=re.sub(r'[^\d.]', '', deb)
        deb=deb.replace(",","")
        equi=equi.replace(",","")
        # num_only=int(num_only)
        # return abs(num_only)
        result = float(int(deb) / int(equi))
        strin=str(result)[:5]
        debt_to_equity=float(strin)
        # print(result)
        # formatted_result = "{:.2f}".format(result)
        # information.insert_one({"debt_to_equity":float(strin)})
        information.update_one({"name":f"{option}"},{"$set":{
                                                "debt_to_equity":debt_to_equity
                    }})
    return  debt_to_equity

# print(Ebitda())
# print(debt_to_equity('drreddy'))
def ROCE_2023(option):
    
    k=information.find_one({"name":f"{option}"})
    if 'roce' in k:
                    roce=k['roce']
                    return roce
    else:
       
        # num_only=float(roce)
        # return abs(roce)
        # information.insert_one({"roce":roce})
        information.update_one({"name":f"{option}"},{"$set":{
                                                "roce":roce
                    }})
        return roce

# print(ROCE_2023('drreddy'))
def current_investment(option):
    k=information.find_one({"name":f"{option}"})
    if 'current_investment' in k:
                    current_investment=k['current_investment']
                    return current_investment
    else:
       
        
        # print(ms)
        # information.insert_one({"current_investment":cur_inv})
        information.update_one({"name":f"{option}"},{"$set":{
                                                "current_investment":current_investment
                    }})
        return current_investment


# print(current_investment("drreddy"))

def ESG(option):
    k=information.find_one({"name":f"{option}"})
    if 'ESG' in k:
        ESG=k['ESG']
        # source_docs=[]
        data_list = []
        for item in ESG:
            esg_data = item.get('Source','')
            esg_dict = {
                    'Question': item.get('Annual_Report', ''),
                    'Value': item.get('Value', ''),
                    'Source':esg_data
                }
            
            data_list.append(esg_dict)
        return data_list
    else:
        
        k="na"
        return k

# st.table(ESG())
# print(ESG("drreddy"))

# print(Awards())


def Board_industry_skills(option):
    # information.insert_one({"board_industry_skills":percentage})
    k=information.find_one({"name":f"{option}"})
    if 'board_industry_skills' in k:
                    board_industry_skills=k['board_industry_skills']
    else:
        board_industry_skills='na'
        information.update_one({"name":f"{option}"},{"$set":{
                                                "board_industry_skills":board_industry_skills
                    }})
        # return board_industry_skills
    return board_industry_skills
    # return bi,total
# print(Board_industry_skills('drreddy'))

