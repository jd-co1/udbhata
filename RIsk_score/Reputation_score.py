from pymongo import MongoClient
import os,math,re
from dotenv import load_dotenv
import streamlit as st
load_dotenv()

client=MongoClient(st.secrets['mongodb'])
mydb=client.get_database('Udbhata')
information=mydb.companies_data


def sustainability_db(option):
    k=information.find_one({"name":f"{option}"})
    if 'Sustainability' in k:
        fin=k['Finance']
        ESG=k['Sustainability']
        Governance=k['Governance']
        Risk=k['Risk_management']
        if 'awards' in ESG:
            awards=ESG['awards']
            data_list=[]
            for i in awards:
                k=data_list.append(i.split('\n'))
            # print(data_list)
            if data_list[0][0]=='NA':
                sus= 0
            # print(data_list)
            else:
                sus= len([item for sublist in data_list for item in sublist])
        if 'awards' in fin:
            awards=fin['awards']
            data_list=[]
            for i in awards:
                k=data_list.append(i.split('\n'))
            # print(data_list)
            if data_list[0][0]=='NA':
                Fina= 0
            # print(data_list)
            else:
                Fina= len([item for sublist in data_list for item in sublist])
        if 'awards' in Governance:
            awards=Governance['awards']
            data_list=[]
            for i in awards:
                k=data_list.append(i.split('\n'))
            # print(data_list)
            if data_list[0][0]=='NA':
                Gov= 0
            # print(data_list)
            else:
                Gov= len([item for sublist in data_list for item in sublist])
        if 'awards' in Risk:
            awards=Risk['awards']
            data_list=[]
            for i in awards:
                k=data_list.append(i.split('\n'))
            # print(data_list)
            if data_list[0][0]=='NA':
                Rik= 0
            else:
                Rik= len([item for sublist in data_list for item in sublist])
            # print(data_list)
        return Fina+sus+Gov+Rik
        
        

# print(sustainability_db("drreddy"))
def Sustainability(option):
    drreddy=sustainability_db('drreddy')
    novartis=sustainability_db('novartis')
    abbott=sustainability_db('abbott')
    gsk=sustainability_db('gsk')
    teva=sustainability_db('teva')
    takeda=sustainability_db('takeda')
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
        gsk_percent1=(100-percent)*0.10
    return gsk_percent1,k,list1,gsk_position

# print(Sustainability('teva'))