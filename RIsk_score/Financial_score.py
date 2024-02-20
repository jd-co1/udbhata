from pymongo import MongoClient
import os,math,re
from dotenv import load_dotenv
import streamlit as st
load_dotenv()

client=MongoClient(st.secrets['mongodb'])
mydb=client.get_database('Udbhata')
information=mydb.companies_data

def ebit_netsales(option):
    k=information.find_one({"name":f"{option}"})
    if 'ebit/net_sales' in k:
        average_days=k['ebit/net_sales']
        if average_days=="NA":
            return 0
        else:
            if not isinstance(average_days, str):
                average_days=str(average_days)
            average_days=average_days.replace("%","")
            average_days=float(average_days)
            return round(average_days,2)
            # return round(average_days,2) #average_tenure
    else:
        return"average_tenure not found in any document"
def EBIT_Net_Sales(option):
        drreddy=ebit_netsales('drreddy')
        novartis=ebit_netsales('novartis')
        abbott=ebit_netsales('abbott')
        gsk=ebit_netsales('gsk')
        teva=ebit_netsales('teva')
        takeda=ebit_netsales('takeda')
        k={'drreddy': drreddy, 'novartis': novartis, 'abbott': abbott, 'gsk': gsk, 'teva': teva, 'takeda': takeda}
        print(k)
        list1=sorted(k.values())
        print(list1)
        op=k.get(option)
        print(op)
        gsk_position = len([x for x in list1 if x < op])
        print(gsk_position)
        percent=(gsk_position/len(list1))*100
        print(percent)
        if percent==0:
            gsk_percent1=0
        else:
            gsk_percent1=(100-percent)*0.075
        return gsk_percent1
        # print(gsk_percent1)

# print(EBIT_Net_Sales('teva'))
def debt(option):
    k=information.find_one({"name":f"{option}"})
    if 'debt_to_equity' in k:
        average_days=k['debt_to_equity']
        if average_days=="NA":
            return 0
        else:
            if not isinstance(average_days, str):
                average_days=str(average_days)
            average_days=average_days.replace("%","")
            average_days=float(average_days)
            return round(average_days,2)
            # return round(average_days,2) #average_tenure
    else:
        return"average_tenure not found in any document"
def Debt_to_Equity(option):
        drreddy=debt('drreddy')
        novartis=debt('novartis')
        abbott=debt('abbott')
        gsk=debt('gsk')
        teva=debt('teva')
        takeda=debt('takeda')
        k={'drreddy': drreddy, 'novartis': novartis, 'abbott': abbott, 'gsk': gsk, 'teva': teva, 'takeda': takeda}
        # print(k)
        list1=sorted(k.values())
        # print(list1)
        op=k.get(option)
        # print(op)
        gsk_position = len([x for x in list1 if x < op])
        # print(gsk_position)
        percent=(gsk_position/len(list1))*100
        # print(percent)
        if percent==0:
            gsk_percent1=0
        else:
            gsk_percent1=(100-percent)*0.075
        return gsk_percent1


# print(Debt_to_Equity('teva'))