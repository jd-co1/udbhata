import streamlit as st
import os
import pandas as pd
from RIsk_score.management_hsr import board_industry_skills,TSR,HSR
# from pymongo import MongoClient


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
        st.write(f"Total management score for {option}={tsr}+{board}+{Hist}:",tsr+board+Hist)





