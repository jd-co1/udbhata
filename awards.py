import streamlit as st
import pandas as pd
import pymongo
# import pandas as pd
client=pymongo.MongoClient('mongodb+srv://test:test@cluster0.tw5ieeh.mongodb.net/?retryWrites=true&w=majority')

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
                        award_list.append(i)
                    return award_list,sources_list
    else:
        from views.reports import run_question
        susustainability,source=run_question("""What are the awards and recognitions for the company in the area of sustainability?.\n,
                                             only give awards and recognitions which come under Sustainability category,dont give awards which come under other categories.\n,
                                             give award names with 5 words description and seperated by comma""")
        # print(finace,source)
        # fin=run_question(f"from {finace},give count")
        # return fin
        award_list=susustainability.split(",")
        sources=[]
        for i in source:
            content=(i.page_content+"\n "+str(float(i.metadata['page']+1))+"\n "+i.metadata['source'])
            sources.append(content)
        # award_list.extend(sources)
        data={
            "Award":award_list#* len(sources),
            # "Source":sources
            }
        information.update_one({"name":f"{option}"},{"$set":{
                                                    "Sustainability":{
                                                        "awards":award_list,
                                                        "sources":sources
                                                    }
                        }})
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
        from views.reports import run_question
        finace,source=run_question("""What are the awards and recognitions  of the company which comes under Finance ?\n,
                                   only give awards and recognitions which come under Financial category,dont give awards which come under other categories.\n
                                if there is more than one award then just give award names with 5 words description and seperated by comma""")
        award_list=finace.split(",")
        sources=[]
        for i in source:
            content=(i.page_content+"\n "+str(i.metadata))
            sources.append(content)

        data={
            "Award":award_list,
        }
        information.update_one({"name":f"{option}"},{"$set":{
            "Finance":{
                "awards":award_list,
                "sources":sources
            }
        }})
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
        from views.reports import run_question
        Risk_management,source=run_question("""What are the awards and recognitions  of the company for Risk management?\n,
                                if there is more than one award then just give award names with 5 words description and seperated by comma""")
        award_list=Risk_management.split(",")
        sources=[]
        for i in source:
            content=(i.page_content+"\n "+str(i.metadata))
            sources.append(content)

        data={
            "Award":award_list,
        }
        information.update_one({"name":f"{option}"},{"$set":{
            "Risk_management":{
                "awards":award_list,
                "sources":sources
            }
        }})
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
        from views.reports import run_question
        Governance,source=run_question("""What are the awards and recognitions  of the company in the area of Governance?\n,
                                if there is more than one award then just give award names with 5 words description and seperated by comma""")
        award_list=Governance.split(",")
        sources=[]
        for i in source:
            content=(i.page_content+"\n "+str(i.metadata))
            sources.append(content)

        data={
            "Award":award_list,
        }
        information.update_one({"name":f"{option}"},{"$set":{
            "Governance":{
                "awards":award_list,
                "sources":sources
            }
        }})
        # print(award_list)

# print(Governance_awards("drreddy"))