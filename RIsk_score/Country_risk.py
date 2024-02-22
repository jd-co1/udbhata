
from pymongo import MongoClient
import os,math,re
# from dotenv import load_dotenv
# from Country_risks import cumulative_risk




client=MongoClient('mongodb+srv://test:test@cluster0.tw5ieeh.mongodb.net/?retryWrites=true&w=majority')

mydb=client.get_database('Udbhata')
information=mydb.countries_data
def db(option):
    k=information.find_one({"name":f'{option}'})
    if 'cumulative_risk' in k:
        return k['cumulative_risk']
    else:
        return f'Cumulative risk not found for {option}'

def COUNTRY(option):
    if option=='drreddy':
        option='India'
    elif option=='takeda':
        option='Japan'
    elif option=='teva':
        option='Israel'
    elif option=='gsk':
        option='United Kingdom'
    elif option=='abbott':
        option='United States'
    else:
        option='Switzerland'
    India=db('India')
    USA=db('United States')
    UK=db('United Kingdom')
    Japan=db('Japan')
    Israel=db('Israel')
    Switzerland=db('Switzerland')
    k={'India': India, 'United States': USA, 'United Kingdom': UK, 'Japan': Japan, 'Israel': Israel, 'Switzerland': Switzerland}
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
        gsk_percent1=(100-percent)*0.15
    return gsk_percent1,k,list1,gsk_position

# print(COUNTRY('United Kingdom'))



