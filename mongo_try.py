import pymongo
import pandas as pd
client=pymongo.MongoClient('mongodb://localhost:27017/')

mydb=client['drreddy']
information=mydb.info
def board_industry_skills(option):
    k=information.find_one({"name":f"{option}"})
    if 'board_industry_skills' in k:
                    board_industry_skills=k['board_industry_skills']
    return board_industry_skills

def Awards():
    doc=information.find_one({"awards": {"$exists": True}})

    if doc:
        awards = doc["awards"]
    else:
        print("awards not found in any document")
    return awards

def Ebitda(option):
    k=information.find_one({"name":f"{option}"})
    if 'ebitda' in k:
                    ebitda=k['ebitda']
    return ebitda

def debt_to_equity(option):
    k=information.find_one({"name":f"{option}"})
    if 'debt_to_equity' in k:
                    debt_to_equity=k['debt_to_equity']
    return debt_to_equity

def roce(option):
    k=information.find_one({"name":f"{option}"})
    if 'roce' in k:
                    roce=k['roce']
    return roce


def current_investment(option):
    k=information.find_one({"name":f"{option}"})
    if 'current_investment' in k:
                    current_investment=k['current_investment']
    return current_investment


def ESG():
    # doc=information.find_one({"ESG_count": {"$exists": True}})
    data_dict=information.find_one({"ESG": {"$exists": True}})
    # Extract values from data_dict
    esg_data = data_dict.get('ESG', [])

# Create a list of dictionaries to represent the data
    data_list = []
    for esg_item in esg_data:
        esg_dict = {
            'Question': esg_item.get('Annual_Report', ''),
            'Value': esg_item.get('Value', '')
        }
        data_list.append(esg_dict)

    # Convert the list of dictionaries to a DataFrame
    # df = pd.DataFrame(data_list)
    # if doc:
    #     ESG = doc["ESG_count"]
    # else:
    #     print("ESG not found in any document")
    return data_list
# print(ESG())

def average_tenure(option):
    k=information.find_one({"name":f"{option}"})
    if 'average_tenure' in k:
                    average_tenure =k['average_tenure']
    else:
        print("average_tenure not found in any document")
    return average_tenure
















