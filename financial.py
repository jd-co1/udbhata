
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
    if 'ebitda' in k:
            ebitda=k['ebitda']
            return ebitda
    else:
        from views.reports import run_question
        ebitda,source_docs=run_question("EBITDA margin for the year 2023")
        # num_only=re.sub(r'\D', '',ebit)
        # information.insert_one({"ebitda":ebit})
        information.update_one({"name":f"{option}"},{"$set":{
                                                "ebitda":ebitda
                    }})
    return ebitda
# print(Ebitda('drreddy'))


def debt_to_equity(option):
    k=information.find_one({"name":f"{option}"})

    if 'debt_to_equity' in k:
                    debt_to_equity=k['debt_to_equity']
                    return debt_to_equity
    else:
        from views.reports import run_question
        deb,source=run_question("what is the total debt of the company, just give value dont give description ")
        # print(deb)
        equi,source_docs=run_question("what is the total shareholders equity of the company for the year 2023, just give value dont give description ")
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
        from views.reports import run_question
        roce,source=run_question(f"what is the value of Earnings before interest and taxes divided by Capital Employed for 2023 year ")
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
        from views.reports import run_question
        current_investment,source=run_question("from the report search current investments, just give value dont give description ")
        
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
        from views.reports import run_question
        questions=[
        "Does the company has a independance statement for the board of directors in place?",
        "Does the company have a formal board diversity policy that clearly requires diversity factors such as gender, race, ethnicity, country of origin, nationality or cultural background in the board nomination process?",
        "Has the company conducted a materiality analysis to identify the most important material issues (economic, environmental, or social) for the company's performance?",
        "Does the company publicly disclose details of the materiality analysis, including information on how they conduct the materiality analysis process and progress towards targets or metrics?",
        "Does the company have Risk Management Committee.",
        "Does the company identify emerging risks, and give the mitigation plans for the risks",
        "Does the company have business continuity or contigency plans and incident reponse in place for cybersecurity or data security?",
        "Does the company have a Supplier Code of Conduct and is it publicly available?"
        

        ]
        print("Running",len(questions))
        results=[]

        with ThreadPoolExecutor(max_workers=3) as executor:
                # Submit tasks to the executor
                t1=executor.submit(run_question, questions[0])
                t2=executor.submit(run_question, questions[1])
                t3=executor.submit(run_question, questions[2])
                t4=executor.submit(run_question, questions[3])
                t5=executor.submit(run_question, questions[4])
                t6=executor.submit(run_question, questions[5])
                t7=executor.submit(run_question, questions[6])
                t8=executor.submit(run_question, questions[7])
                concurrent.futures.wait([t1,t2,t3,t4,t5,t6,t7,t8])
                if t1.done() & t2.done() & t3.done() & t4.done() & t5.done() & t6.done() & t7.done() & t8.done():
                    results.append({"Annual_Report":questions[0],"Value":t1.result()[0],"Source":str(t1.result()[1])})
                    results.append({"Annual_Report":questions[1],"Value":t2.result()[0],"Source":str(t2.result()[1])})
                    results.append({"Annual_Report":questions[2],"Value":t3.result()[0],"Source":str(t3.result()[1])})
                    results.append({"Annual_Report":questions[3],"Value":t4.result()[0],"Source":str(t4.result()[1])})
                    results.append({"Annual_Report":questions[4],"Value":t5.result()[0],"Source":str(t5.result()[1])})
                    results.append({"Annual_Report":questions[5],"Value":t6.result()[0],"Source":str(t6.result()[1])})
                    results.append({"Annual_Report":questions[6],"Value":t7.result()[0],"Source":str(t7.result()[1])})
                    results.append({"Annual_Report":questions[7],"Value":t8.result()[0],"Source":str(t8.result()[1])})
                    print("Done")

        df=pd.DataFrame(results)
        data_dict = df.to_dict(orient='records')
        information.update_one({"name":f"{option}"},{"$set":{
                                                    "ESG":data_dict
                        }})
        return df

# st.table(ESG())
# print(ESG("drreddy"))


def Awards():
    from views.reports import run_question
    aw=run_question("""
                    
                    What are the key awards and recognitions of the company in the areas of Finance, Risk management, Sustainability and Governance?
                    Just give the count of awards and recognitions.
                    
                    """) 
    num_only=re.sub(r'\D', '',aw)
    # information.insert_one({"awards":num_only})
    return num_only
# print(Awards())


def Board_industry_skills(option):
    # information.insert_one({"board_industry_skills":percentage})
    k=information.find_one({"name":f"{option}"})
    if 'board_industry_skills' in k:
                    board_industry_skills=k['board_industry_skills']
    else:
        from views.reports import run_question
        total,source=run_question("How many board members are there in the company?")
        print(total)
        bi,source_doc=run_question("How many indipendent board members have experience in the pharmaceutical industry?")
        print(bi)
        num_only=re.sub(r'\D', '',total)
        print(num_only)
        num=re.sub(r'\D', '',bi)
        print(num)
        percentage1=(int(num)/int(num_only))*100
        percentage=round(percentage1,2)
        board_industry_skills=round(percentage,2)
        print(board_industry_skills)
        information.update_one({"name":f"{option}"},{"$set":{
                                                "board_industry_skills":board_industry_skills
                    }})
        # return board_industry_skills
    return board_industry_skills
    # return bi,total
# print(Board_industry_skills('drreddy'))

