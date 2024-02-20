import streamlit as st
import os
import pandas as pd
from RIsk_score.management_hsr import board_industry_skills,TSR,HSR
# from pymongo import MongoClient
from RIsk_score.Financial_score import Debt_to_Equity,EBIT_Net_Sales
from RIsk_score.company_specific import company_Count,Company_Impact
from RIsk_score.Non_financial_score import Investment,ROCE,ESG
from RIsk_score.Reputation_score import Sustainability
from pymongo import MongoClient
client=MongoClient(st.secrets['mongodb'])

mydb=client.get_database('Udbhata')
information=mydb.companies_data


def load_reports():
    st.header("Reports Generator")
    companies_df = pd.DataFrame({'Company': ['drreddy','gsk','takeda','teva','abbott','novartis']})
    
    st.header('Companies')
    option = st.selectbox(
        'Select a company',
        companies_df['Company'],
        index=None,
        placeholder="companies")
    if option == 'drreddy' or option == 'gsk' or option == 'takeda' or option == 'teva' or option == 'abbott' or option == 'novartis':
        
            st.write('You selected:', option)
            st.subheader('Managemeant Score')
            tsr=TSR(option)
            st.write(f"{option}'s TSR:",tsr)
            board=board_industry_skills(option)#board_industry_skills(option)
            st.write(f"{option}'s Board Industry Experience:",board)
            Hist=HSR(option)
            st.write(f"{option}'s Historical Share Price:",Hist)
            total1=tsr+board+Hist
            st.write(f"Total management score for {option}:",round((total1),2))



            st.subheader('Financial Score')
            ebit=EBIT_Net_Sales(option)
            st.write(f"{option}'s EBIT/Net Sales:",ebit)
            debt=Debt_to_Equity(option)
            st.write(f"{option}'s Debt to Equity ratio:",debt)
            total2=ebit+debt
            st.write(f"Total financial score for {option}:",round((total2),2))

            st.subheader('Industry Risk Score')
            st.write("NA")

            st.subheader('Company Specific Risk Score')
            impact=Company_Impact(option)
            st.write(f"{option}'s Risk Impact:",impact)
            count=company_Count(option)
            st.write(f"{option}'s Risk Count:",count)
            total3=impact+count
            st.write(f"Total company specific score for {option}:",round((total3),2))

            st.subheader("Country Specific Risk Score")
            st.write("NA")

            st.subheader("Non-financial Risk Score")
            inves=Investment(option)
            st.write(f"{option}'s current Investment:",inves)
            roce=ROCE(option)
            st.write(f"{option}'s ROCE:",roce)
            esg=ESG(option)
            st.write(f"{option}'s count of YES for ESG questions:",esg)
            total4=inves+roce+esg
            st.write(f"Total non-financial score for {option}:",round((total4),2))


            st.subheader("Reputation Score")
            award=Sustainability(option)
            st.write(f"{option}'s 10% score of awards:",award)
            total5=award
            st.write(f"Total reputation score for {option}:",round((total5),2))


            st.subheader("Overall Score")
            total=total1+total2+total3+total4+total5
            information.update_one({"name":f"{option}"},{"$set":{
                                                    "total_risk_score":total
                        }})
            st.write(f"Total Overall score for {option}:",round((total),2))





