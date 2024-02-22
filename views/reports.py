import streamlit as st
import os
import pandas as pd
from RIsk_score.management_hsr import board_industry_skills,TSR,HSR
# from pymongo import MongoClient
from RIsk_score.Financial_score import Debt_to_Equity,EBIT_Net_Sales
from RIsk_score.company_specific import company_Count,Company_Impact
from RIsk_score.Non_financial_score import Investment,ROCE,ESG
from RIsk_score.Reputation_score import Sustainability
from RIsk_score.Country_risk import COUNTRY
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
            if st.checkbox(label="Show calculations",key=1):
                st.write(f"Companies TSR values:",k1)
                st.write(f"List of tsr values after sorting:",list11)
                percent1=round((gsk_position1/(len(list11)))*100,2)
                st.write(f"number companies below {option}=({gsk_position1}/{len(list11)})*100:",percent1)
                if percent1==0:
                    percent11=0
                else:
                    percent11=(100-percent1)
                    st.write(f"100-{percent1}={percent11}")
                st.write(f"6% of {percent11}={percent11} * 0.06:",round((percent11*0.06),2))

            board,k2,list12,gsk_position2=board_industry_skills(option)#board_industry_skills(option)
            st.write(f"{option}'s Board Industry Experience:",board)
            if st.checkbox(label="Show calculations",key=2):
                st.write(f"Companies Board Industry Experience values:",k2)
                st.write(f"List of Board Industry Experience values after sorting:",list12)
                percent2=round((gsk_position2/(len(list12)))*100,2)
                st.write(f"number companies below {option}=({gsk_position2}/{len(list12)})*100:",percent2)
                if percent2==0:
                    percent21=0
                else:
                    percent21=(100-percent2)
                    st.write(f"100-{percent2}={percent21}")
                st.write(f"3% of {percent21}={percent21} * 0.03:",round((percent21*0.03),2))

            Hist,k3,list13,gsk_position3=HSR(option)
            st.write(f"{option}'s Historical Share Price:",Hist)
            if st.checkbox(label="Show calculations",key=3):
                st.write(f"Companies average days values:",k3)
                st.write(f"List of average days values after sorting:",list13)
                percent3=round((gsk_position3/(len(list13)))*100,2)
                st.write(f"number companies below {option}=({gsk_position3}/{len(list13)})*100:",percent3)
                if percent3==0:
                    percent13=0
                else:
                    percent13=(100-percent3)
                    st.write(f"100-{percent3}={percent13}")
                st.write(f"6% of {percent13}={percent13} * 0.06:",round((percent13*0.06),2))
            total1=tsr+board+Hist
            st.write(f"Total management score for {option}:",round((total1),2))



            st.subheader('Financial Score')
            ebit,k4,list14,gsk_position4=EBIT_Net_Sales(option)
            st.write(f"{option}'s EBIT/Net Sales:",ebit)
            if st.checkbox(label="Show calculations",key=4):
                st.write(f"all Companies EBIT/Net Sales values:",k4)
                st.write(f"List of EBIT/Net Sales values after sorting:",list14)
                percent4=round((gsk_position4/(len(list14)))*100,2)
                st.write(f"number companies below {option}=({gsk_position4}/{len(list14)})*100:",percent4)
                if percent4==0:
                    percent14=0
                else:
                    percent14=(100-percent4)
                    st.write(f"100-{percent4}={percent14}")
                st.write(f"7.5% of {percent14}={percent14} * 0.075:",round((percent14*0.075),2))

            debt,k5,list15,gsk_position5=Debt_to_Equity(option)
            st.write(f"{option}'s Debt to Equity ratio:",debt)
            if st.checkbox(label="Show calculations",key=5):
                st.write(f"all Companies debt to equity values:",k5)
                st.write(f"List of debt to equity values after sorting:",list15)
                percent5=round((gsk_position5/(len(list15)))*100,2)
                st.write(f"number companies below {option}=({gsk_position5}/{len(list15)})*100:",percent5)
                if percent5==0:
                    percent15=0
                else:
                    percent15=(100-percent5)
                    st.write(f"100-{percent5}={percent15}")
                st.write(f"7.5% of {percent15}={percent15} * 0.075:",round((percent15*0.075),2))
            total2=ebit+debt
            st.write(f"Total financial score for {option}:",round((total2),2))

            st.subheader('Industry Risk Score')
            st.write("NA")

            st.subheader('Company Specific Risk Score')
            impact,k6,list16,gsk_position6=Company_Impact(option)
            st.write(f"{option}'s Risk Impact:",impact)
            if st.checkbox(label="Show calculations",key=6):
                st.write(f"Companies Risk Impact values:",k6)
                st.write(f"List of Risk Impact values after sorting:",list16)
                percent6=round((gsk_position6/(len(list16)))*100,2)
                st.write(f"number companies below {option}=({gsk_position6}/{len(list16)})*100:",percent6)
                if percent6==0:
                    percent16=0
                else:
                    percent16=(100-percent6)
                    st.write(f"100-{percent6}={percent16}")
                st.write(f"7.5% of {percent16}={percent16} * 0.075:",round((percent16*0.075),2))

            count,k7,list17,gsk_position7=company_Count(option)
            st.write(f"{option}'s Risk Count:",count)
            if st.checkbox(label="Show calculations",key=7):
                st.write(f"Companies Risk Count values:",k7)
                st.write(f"List of Risk Count values after sorting:",list17)
                percent7=round((gsk_position7/(len(list17)))*100,2)
                st.write(f"number companies below {option}=({gsk_position7}/{len(list17)})*100:",percent7)
                if percent7==0:
                    percent17=0
                else:
                    percent17=(100-percent7)
                    st.write(f"100-{percent7}={percent17}")
                st.write(f"7.5% of {percent17}={percent17} * 0.075:",round((percent17*0.075),2))

            total3=impact+count
            st.write(f"Total company specific score for {option}:",round((total3),2))
            

            st.subheader("Country Specific Risk Score")
            country,k12,list22,gsk_position12=COUNTRY(option)
            st.write(f"{option}'s Country Risk:",round(country,2))#,country)
            if st.checkbox(label="Show calculations",key=12):
                st.write(f"Companies Country Risk values:",k12)
                st.write(f"List of Country Risk values after sorting:",list22)
                percent12=round((gsk_position12/(len(list22)))*100,2)
                st.write(f"number companies below {option}=({gsk_position12}/{len(list22)})*100:",percent12)
                if percent12==0:
                    percent22=0
                else:
                    percent22=(100-percent12)
                    st.write(f"100-{percent12}={percent22}")
                st.write(f"15% of {percent22}={percent22} * 0.15:",round((percent22*0.15),2))
            total6=country
            st.write(f"Total country Risk score",round((total6),2))


            st.subheader("Non-financial Risk Score")
            inves,k8,list18,gsk_position8=Investment(option)
            st.write(f"{option}'s current Investment:",inves)
            if st.checkbox(label="Show calculations",key=8):
                st.write(f"Companies current investment values:",k8)
                st.write(f"List of current investment values after sorting:",list17)
                percent8=round((gsk_position8/(len(list18)))*100,2)
                st.write(f"number companies below {option}=({gsk_position8}/{len(list18)})*100:",percent7)
                if percent8==0:
                    percent18=0
                else:
                    percent18=(100-percent8)
                    st.write(f"100-{percent8}={percent18}")
                st.write(f"2.5% of {percent18}={percent18} * 0.025:",round((percent18*0.025),2))

            roce,k9,list19,gsk_position9=ROCE(option)
            st.write(f"{option}'s ROCE:",roce)
            if st.checkbox(label="Show calculations",key=9):
                st.write(f"Companies ROCE values:",k9)
                st.write(f"List of ROCE values after sorting:",list19)
                percent9=round((gsk_position9/(len(list19)))*100,2)
                st.write(f"number companies below {option}=({gsk_position9}/{len(list19)})*100:",percent9)
                if percent9==0:
                    percent19=0
                else:
                    percent19=(100-percent9)
                    st.write(f"100-{percent9}={percent19}")
                st.write(f"2.5% of {percent19}={percent19} * 0.025:",round((percent19*0.025),2))
            esg,k10,list20,gsk_position10=ESG(option)
            st.write(f"{option}'s count of YES for ESG questions:",esg)
            if st.checkbox(label="Show calculations",key=10):
                st.write(f"Companies count of YES for ESG questions:",k10)
                st.write(f"List of count of YES for ESG questions after sorting:",list19)
                percent10=round((gsk_position10/(len(list20)))*100,2)
                st.write(f"number companies below {option}=({gsk_position10}/{len(list20)})*100:",percent10)
                if percent10==0:
                    percent20=0
                else:
                    percent20=(100-percent10)
                    st.write(f"100-{percent10}={percent20}")
                st.write(f"5% of {percent20}={percent20} * 0.05:",round((percent20*0.05),2))

            total4=inves+roce+esg
            st.write(f"Total non-financial score for {option}:",round((total4),2))


            st.subheader("Reputation Score")
            award,k11,list21,gsk_position11=Sustainability(option)
            st.write(f"{option}'s 10% score of awards:",award)
            if st.checkbox(label="Show calculations",key=11):
                st.write(f"Companies 10% score of awards:",k11)
                st.write(f"List of 10% score of awards after sorting:",list21)
                percent11=round((gsk_position11/(len(list21)))*100,2)
                st.write(f"number companies below {option}=({gsk_position11}/{len(list21)})*100:",percent11)
                if percent11==0:
                    percent21=0
                else:
                    percent21=(100-percent11)
                    st.write(f"100-{percent11}={percent21}")
                st.write(f"10% of {percent21}={percent21} * 0.1:",round((percent21*0.1),2))

            total5=award
            st.write(f"Total reputation score for {option}:",round((total5),2))


            st.subheader("Overall Score")
            total=total1+total2+total3+total4+total5+total6
            # information.update_one({"name":f"{option}"},{"$set":{
            #                                         "total_risk_score":total
            #             }})
            st.write(f"Total Overall score for {option}:",round((total),2))





