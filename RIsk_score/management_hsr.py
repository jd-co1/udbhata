from pymongo import MongoClient
import os,math,re
from dotenv import load_dotenv
import streamlit as st
load_dotenv()
client=MongoClient(st.secrets['mongodb'])
mydb=client.get_database('Udbhata')
information=mydb.companies_data

def avg_days(option):
    k=information.find_one({"name":f"{option}"})
    if 'average_days' in k:
        average_days=k['average_days']
        if average_days=="NA":
            return 0
        else:
            return round(average_days,2) #average_tenure
    else:
        return"average_tenure not found in any document"
def HSR(option):
        drreddy=avg_days('drreddy')
        novartis=avg_days('novartis')
        abbott=avg_days('abbott')
        gsk=avg_days('gsk')
        teva=avg_days('teva')
        takeda=avg_days('takeda')
        k={'drreddy': drreddy, 'novartis': novartis, 'abbott': abbott, 'gsk': gsk, 'teva': teva, 'takeda': takeda}
        # print(k)
        list1=sorted(k.values())
        op=k.get(option)
        gsk_position = len([x for x in list1 if x < op])
        print(gsk_position)
        percent=(gsk_position/len(list1))*100
        print(percent)
        if percent==0:
            gsk_percent1=0
        else:
            gsk_percent1=(100-percent)*0.06
        return gsk_percent1,k,list1,gsk_position
        # print(gsk_percent1)

# print(percent('teva'))

def tsr_value(option):
    k=information.find_one({"name":f"{option}"})
    if 'tsr_value' in k:
        tsr=k['tsr_value']
        return tsr
    else:
        return"tsr not found in any document"

def TSR(option):
        drreddy=tsr_value('drreddy')
        novartis=tsr_value('novartis')
        abbott=tsr_value('abbott')
        gsk=tsr_value('gsk')
        teva=tsr_value('teva')
        takeda=tsr_value('takeda')
        k={'drreddy': (drreddy/83), 'novartis': novartis, 'abbott': abbott, 'gsk': gsk, 'teva': teva, 'takeda': takeda}
        # print(k)
        list1=sorted(k.values())
        op=k.get(option)
        gsk_position = len([x for x in list1 if x < op])
        print(gsk_position)
        percent=(gsk_position/len(list1))*100
        print(percent)
        if percent==0:
            gsk_percent1=0
        else:
            gsk_percent1=(100-percent)*0.06
        return gsk_percent1,k,list1,gsk_position  

# print(TSR('gsk'))

def board_skill(option):
    k=information.find_one({"name":f"{option}"})
    if 'board_industry_skills' in k:
        board_industry_skills=k['board_industry_skills']
        if board_industry_skills=="NA":
            return 0
        else:
            return round(board_industry_skills,2) #average_tenure
    else:
        return"average_tenure not found in any document"

def board_industry_skills(option):
        drreddy=board_skill('drreddy')
        novartis=board_skill('novartis')
        abbott=board_skill('abbott')
        gsk=board_skill('gsk')
        teva=board_skill('teva')
        takeda=board_skill('takeda')
        k={'drreddy': drreddy, 'novartis': novartis, 'abbott': abbott, 'gsk': gsk, 'teva': teva, 'takeda': takeda}
        print(k)
        list1=sorted(k.values())
        print(list1)
        op=k.get(option)
        gsk_position = len([x for x in list1 if x < op])
        print(gsk_position)
        percent=(gsk_position/len(list1))*100
        print(percent)
        if percent==0:
            gsk_percent1=0
        else:
            gsk_percent1=(100-percent)*0.03
        return gsk_percent1,k,list1,gsk_position
# print(board_industry_skills('drreddy'))