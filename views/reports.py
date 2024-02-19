import streamlit as st
import os
import pandas as pd
from RIsk_score.management_hsr import board_industry_skills,TSR,HSR
# from pymongo import MongoClient
from RIsk_score.Financial_score import Debt_to_Equity,EBIT_Net_Sales
from RIsk_score.company_specific import company_Count,Company_Impact
from RIsk_score.Non_financial_score import Investment,ROCE

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
        st.write(f"Total management score for {option}={tsr}+{board}+{Hist}:",round((tsr+board+Hist),2))

        st.subheader('Financial Score')
        ebit=EBIT_Net_Sales(option)
        st.write(f"{option}'s EBIT/Net Sales:",ebit)
        debt=Debt_to_Equity(option)
        st.write(f"{option}'s Debt to Equity ratio:",debt)
        st.write(f"Total financial score for {option}:",round((ebit+debt),2))


        st.subheader('Industry Risk Score')
        st.write("NA")

        st.subheader('Company Specific Risk Score')
        impact=Company_Impact(option)
        st.write(f"{option}'s Risk Impact:",impact)
        count=company_Count(option)
        st.write(f"{option}'s Risk Count:",count)
        st.write(f"Total company specific score for {option}:",round((impact+count),2))

        st.subheader("Country Specific Risk Score")
        st.write("NA")

        st.subheader("Non-financial Risk Score")
        inves=Investment(option)
        st.write(f"{option}'s current Investment:",inves)
        roce=ROCE(option)
        st.write(f"{option}'s ROCE:",roce)
        st.write(f"Total non-financial score for {option}:",round((inves+roce),2))





