from pymongo import MongoClient
import os,math,re
from dotenv import load_dotenv
import streamlit as st
load_dotenv()

client=MongoClient(st.secrets['mongodb'])
mydb=client.get_database('Udbhata')
information=mydb.companies_data

def impact(option):
    k=information.find_one({"name":f"{option}"})
    if 'company_Impact' in k:
        average_days=k['company_Impact']
        if average_days=="NA":
            return 0
        else:
            return round(average_days,2)
            # return round(average_days,2) #average_tenure
    else:
        return"company_Impact not found in any document"
def Company_Impact(option):
        drreddy=impact('drreddy')
        novartis=impact('novartis')
        abbott=impact('abbott')
        gsk=impact('gsk')
        teva=impact('teva')
        takeda=impact('takeda')
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
        return gsk_percent1,k,list1,gsk_position

def count(option):
    k=information.find_one({"name":f"{option}"})
    if 'company_count' in k:
        average_days=k['company_count']
        if average_days=="NA":
            return 0
        else:
            return round(average_days,2)
            # return round(average_days,2) #average_tenure
    else:
        return"company_count not found in any document"
    

def company_Count(option):
        drreddy=count('drreddy')
        novartis=count('novartis')
        abbott=count('abbott')
        gsk=count('gsk')
        teva=count('teva')
        takeda=count('takeda')
        k={'drreddy': drreddy, 'novartis': novartis, 'abbott': abbott, 'gsk': gsk, 'teva': teva, 'takeda': takeda}
        print(k)
        list1=sorted(k.values())
        print(list1)
        op=k.get(option)
        # print(op)
        gsk_position = len([x for x in list1 if x < op])
        print(gsk_position)
        percent=(gsk_position/len(list1))*100
        print(percent)
        if percent==0:
            gsk_percent1=0
        else:
            gsk_percent1=(100-percent)*0.075
        return gsk_percent1,k,list1,gsk_position


# print(company_Count('abbott'))