from pymongo import MongoClient
import os,math,re
from dotenv import load_dotenv

load_dotenv()

client=MongoClient('mongodb+srv://test:test@cluster0.tw5ieeh.mongodb.net/?retryWrites=true&w=majority')
mydb=client.get_database('Udbhata')
information=mydb.companies_data

def current_investment(option):
    k=information.find_one({"name":f"{option}"})
    if 'current_investment' in k:
        average_days=k['current_investment']
        if average_days=="NA":
            return 0
        else:
            if not isinstance(average_days, str):
                average_days=str(average_days)
            average_days=re.sub(r'[^0-9]', '', average_days)
            average_days=float(average_days)
            return round(average_days,2)
            # return round(average_days,2) #average_tenure
    else:
        return"average_tenure not found in any document"
# print(current_investment('drreddy'))
def Investment(option):
        drreddy=current_investment('drreddy')
        novartis=current_investment('novartis')
        abbott=current_investment('abbott')
        gsk=current_investment('gsk')
        teva=current_investment('teva')
        takeda=current_investment('takeda')
        k={'drreddy': ((drreddy*120498.90)/1000000), 'novartis': novartis, 'abbott': abbott, 'gsk': ((gsk*1078748.00)/1000000), 'teva': teva, 'takeda': ((takeda*6668.45)/1000000)}
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
            gsk_percent1=(100-percent)*0.025
        return gsk_percent1

# print(EBIT_Net_Sales('drreddy'))

def roce_db(option):
    k=information.find_one({"name":f"{option}"})
    if 'roce' in k:
        average_days=k['roce']
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
    
def ROCE(option):
    drreddy=roce_db('drreddy')
    novartis=roce_db('novartis')
    abbott=roce_db('abbott')
    gsk=roce_db('gsk')
    teva=roce_db('teva')
    takeda=roce_db('takeda')
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
        gsk_percent1=(100-percent)*0.025
    return gsk_percent1
# print(ROCE('drreddy'))

def esg_db(option):
    k=information.find_one({"name":f"{option}"})
    if 'ESG' in k:
        ESG=k['ESG']
        data_list=[]
        for i in ESG:
            j=i.get('Value')
            j=j.replace('.','')
            data_list.append(j)
        l=data_list.count('Yes')
        return l
    else:
        return "ESG not found in any document"
    
def ESG(option):
    drreddy=esg_db('drreddy')
    novartis=esg_db('novartis')
    abbott=esg_db('abbott')
    gsk=esg_db('gsk')
    teva=esg_db('teva')
    takeda=esg_db('takeda')
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
        gsk_percent1=(100-percent)*0.05
    return gsk_percent1