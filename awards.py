import streamlit as st
import pandas as pd
import pymongo
# import pandas as pd
client=pymongo.MongoClient(st.secrets['mongodb'])

mydb=client.get_database('Udbhata')
information=mydb.companies_data

def sustainability_award(option):
    k=information.find_one({"name":f"{option}"})
    if 'Sustainability' in k:
                    susustainability=k['Sustainability']
                    award = susustainability.get('awards', [])
                    sources = susustainability.get('sources', [])
                    award_list=[]
                    sources_list=[]
                    for i in sources:
                        sources_list.append(i)
                    for i in award:
                        award_list.append(i.split('\n'))
                    return award_list,sources_list
    else:
        return 0
        # df=pd.DataFrame(data)
    # print(data)
    # return df
# print(sustainability_award("drreddy"))


def finace_awards(option):
    k=information.find_one({"name":f"{option}"})
    if 'Finance' in k:
                    Finance=k['Finance']
                    award = Finance.get('awards', [])
                    sources = Finance.get('sources', [])
                    award_list=[]
                    sources_list=[]
                    for i in sources:
                        sources_list.append(i)
                    for i in award:
                        award_list.append(i)
                    return award_list,sources_list
    else:
        return 0
    # print(sources)
    # print(data)
# print(finace_awards("drreddy"))



def Risk_management_awards(option):
    k=information.find_one({"name":f"{option}"})
    if 'Risk_management' in k:
                    Risk_management=k['Risk_management']
                    award = Risk_management.get('awards', [])
                    sources = Risk_management.get('sources', [])
                    award_list=[]
                    sources_list=[]
                    for i in sources:
                        sources_list.append(i)
                    for i in award:
                        award_list.append(i)
                    return award_list,sources_list
    else:
        return 0
        # print(sources)
        # print(data)

# print(Risk_management_awards("drreddy"))

def Governance_awards(option):
    k=information.find_one({"name":f"{option}"})
    if 'Governance' in k:
                Governance=k['Governance']
                award = Governance.get('awards', [])
                sources = Governance.get('sources', [])
                award_list=[]
                sources_list=[]
                for i in sources:
                       sources_list.append(i)
                for i in award:
                    award_list.append(i)
                return award_list,sources_list
    else:
        return 0
        # print(award_list)

# print(Governance_awards("drreddy"))