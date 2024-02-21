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
            tsr,k1,list11,gsk_position1=TSR(option)
            st.write(f"{option}'s TSR:",tsr)
            if st.checkbox(label="Show calculations"):
                st.write(f"Companies TSR values:",k1)
                st.write(f"List of tsr values after sorting:",list11)
                percent1=round((gsk_position1/(len(list11)))*100,2)
                st.write(f"number companies below {option}=({gsk_position1}/{len(list11)})*100:",percent1)
                percent11=(100-percent1)
                st.write(f"100-{percent1}={percent11}")
                st.write(f"6% of {percent11}={percent11} * 0.06:",round((percent11*0.06),2))

            board,k2,list12,gsk_position2=board_industry_skills(option)#board_industry_skills(option)
            st.write(f"{option}'s Board Industry Experience:",board)
            if st.checkbox(label="Show calculations"):
                st.write(f"Companies Board Industry Experience values:",k2)
                st.write(f"List of Board Industry Experience values after sorting:",list12)
                percent2=round((gsk_position2/(len(list12)))*100,2)
                st.write(f"number companies below {option}=({gsk_position2}/{len(list12)})*100:",percent2)
                percent21=(100-percent2)
                st.write(f"100-{percent2}={percent21}")
                st.write(f"3% of {percent21}={percent21} * 0.03:",round((percent21*0.03),2))

            Hist,k3,list13,gsk_position3=HSR(option)
            st.write(f"{option}'s Historical Share Price:",Hist)
            if st.checkbox(label="Show calculations"):
                st.write(f"Companies average days values:",k3)
                st.write(f"List of average days values after sorting:",list13)
                percent3=round((gsk_position3/(len(list13)))*100,2)
                st.write(f"number companies below {option}=({gsk_position3}/{len(list13)})*100:",percent3)
                percent13=(100-percent3)
                st.write(f"100-{percent3}={percent13}")
                st.write(f"6% of {percent13}={percent13} * 0.06:",round((percent13*0.06),2))
            total1=tsr+board+Hist
            st.write(f"Total management score for {option}:",round((total1),2))



            st.subheader('Financial Score')
            ebit,k4,list14,gsk_position4=EBIT_Net_Sales(option)
            st.write(f"{option}'s EBIT/Net Sales:",ebit)
            if st.checkbox(label="Show calculations"):
                st.write(f"all Companies EBIT/Net Sales values:",k4)
                st.write(f"List of EBIT/Net Sales values after sorting:",list14)
                percent4=round((gsk_position4/(len(list14)))*100,2)
                st.write(f"number companies below {option}=({gsk_position4}/{len(list14)})*100:",percent4)
                percent14=(100-percent4)
                st.write(f"100-{percent4}={percent14}")
                st.write(f"7.5% of {percent14}={percent14} * 0.075:",round((percent14*0.075),2))

            debt,k5,list15,gsk_position5=Debt_to_Equity(option)
            st.write(f"{option}'s Debt to Equity ratio:",debt)
            if st.checkbox(label="Show calculations"):
                st.write(f"all Companies EBIT/Net Sales values:",k5)
                st.write(f"List of EBIT/Net Sales values after sorting:",list15)
                percent5=round((gsk_position5/(len(list15)))*100,2)
                st.write(f"number companies below {option}=({gsk_position5}/{len(list15)})*100:",percent5)
                percent15=(100-percent5)
                st.write(f"100-{percent5}={percent15}")
                st.write(f"7.5% of {percent15}={percent15} * 0.075:",round((percent15*0.075),2))
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





