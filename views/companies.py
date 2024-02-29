import streamlit as st
import pandas as pd
from TSR_calc import tsr,history

from average_tenure import average_tenure_of_a_company
from financial import Ebitda,debt_to_equity,current_investment,ROCE_2023,ESG,Board_industry_skills
# from country import stre
from industry_risk import industry_specific, country_specific
from Country_risks import cumulative_risk
from awards import finace_awards,sustainability_award,Governance_awards,Risk_management_awards
# from hsr_calc import history

def load_companies():
    # Initialize companies DataFrame
    companies_df = pd.DataFrame({'Company': ['drreddy','gsk','takeda','teva','abbott','novartis']})
    
    st.header('Companies')
    option = st.selectbox(
        'Select a company',
        companies_df['Company'],
        index=None,
        placeholder="companies",
        
        )
    if option == "drreddy" or option == "abbott" or option == "gsk" or option == "novartis" or option == "takeda" or option == "teva":
        st.write('You selected:', option)
        if option == f'{option}':
            if option == "drreddy":
                st.write('The values are INR')
            elif option == "takeda":
                st.write('The values are YEN,tsr is USD')
                
            # st.session_state.company_selected = option
            # t=historical_share_csv_web_scraping(option)
            # t
            # st.write(f'Average tenure of {option} company directors: {average_tenure_of_a_company("drreddy")} months')
            # # t=historical_share_csv_web_scraping("drreddy")
            # # t
            # st.write(f'TSR of {option}:',tsr("drreddy"))
            # st.write(f'Average number of days taken to recover from 10% drop in share price: {history("drreddy")}')
            # st.write(f'Ebitda/Net sales of {option}:{Ebitda()} percent')
            # st.write(f'Debt to equity ratio of {option}:',debt_to_equity())
            data = {
                'Metric': ['Average Tenure (months)','Board Industry Experience (%)', 'TSR', f' Average Days to Recover from 5% drop'],
                'Value': [
                    average_tenure_of_a_company(option),
                    Board_industry_skills(option),
                    tsr(option),
                    history(option)
                ]
            }
            table_df = pd.DataFrame(data)
            st.header("Management:")
            st.table(table_df)

            data1 = {
                'Metric': ['Ebitda/Net Sales (%)', 'Debt to Equity Ratio'],
                'Value': [
                    Ebitda(option),
                    debt_to_equity(option)
                ]
            }
            df=pd.DataFrame(data1)
            
            st.header("Financial:")
            st.table(df)
            risk_count,risk_sum=industry_specific()
            data5={
                'Metric': ['Risk Impact in crores', 'Risk events count'],
                'Value': [
                    risk_sum,
                    risk_count
                ]
            }
            df5=pd.DataFrame(data5)
            st.header("Industry Risk:")
            st.table(df5)
            company_risk_sum,company_risk_count=country_specific(option)
            data6={
                'Metric': ['Total Ipact (in crores)','Risk events count'],
                'Value': [
                    company_risk_sum,
                    company_risk_count
                ]
            }
            df6=pd.DataFrame(data6)
            st.header("Company Specific Risk:")
            st.table(df6)
            st.header("Country Risk:")
            total,values_list,names_list,converted=cumulative_risk(option)
            # names_list1=names_list
            st.write("Total caluculated score from the algorithmm:",total)
            if st.checkbox(label="Show calculations",key=2):
                # result_dict = dict(zip(names_list, values_list))
                dictt=dict(zip(names_list, converted))
                # col1, col2 = st.columns(2)
                # with col1:
                #     st.dataframe(result_dict)
                # with col2:
                st.dataframe(dictt)
                # round((5/100)*(converted_list[0]/7)*100,2)
                st.write(f"5% weightage  for Political Risk Short term so 5% of {converted[0]}/7 is",round((5/100)*(converted[0]/7)*100,2))
                st.write(f"10% weightage  for Political Risk Medium/long Term so 10% of {converted[1]}/7 is",round((10/100)*(converted[1]/7)*100,2))
                st.write(f'5% weightage for Premium Classification OECD so 5% of {converted[2]}/7 is',round((5/100)*(converted[2]/7)*100,2) )
                st.write(f"10% weightage  for Business Environment Risk so 10% of {converted[3]}/7 is",round((10/100)*(converted[3]/7)*100,2))
                st.write(f"5% weightage  for Political Violence Risk so 5% of {converted[4]}/7 is",round((5/100)*(converted[4]/7)*100,2))
                st.write(f"20% weightage of Expropriation & Government Action Risk so 20% of {converted[5]}/7 is",round((20/100)*(converted[5]/7)*100,2))
                st.write(f"10% weightage of Currency Inconvertibility and Transfer Restriction Risk so 10% of {converted[6]}/7 is",round((10/100)*(converted[6]/7)*100,2))
                st.write(f"4% weightage of Corruption Perceptions Index so 4% of {converted[7]} is",round((4/100)*converted[7],2))
                st.write(f"6% weightage of Ease of Doing business so 6% of {converted[8]} is",round((6/100)*(converted[8])*100,2))
                st.write(f"20% weightage of Economic Risk so 20% of {converted[9]} is",round((20/100)*(converted[9])*100,2))
                st.write(f"3% weightage of Competitiveness Index so 3% of {converted[10]} is",round((3/100)*(converted[10])*100,2))
                st.write(f"2% weightage of Global Terrorism Impact so 2% of {converted[11]} is",round((2/100)*(converted[10])*100,2))
            st.header("Non-Financial:")
            data3={
                'Metric': ['Current Investment', 'ROCE'],
                'Value': [
                    current_investment(option),
                    ROCE_2023(option)
                ]
            }
            df1=pd.DataFrame(data3)
            st.subheader("Investments:")
            st.table(df1)
            st.subheader("ESG:")
            data_list=ESG(option)
            df3=pd.DataFrame(data_list)
            def check(data_list):
                for index, row in enumerate(data_list):
                    source_button = st.checkbox(f"Show Source ({index+1})")
                    if source_button:
                        k=st.write(row["Source"])
                        return k
            count=df3['Value'].value_counts().get('Yes', 0)
            question_and_value=[(item['Question'], item['Value']) for item in data_list]
            df_st=pd.DataFrame(question_and_value,columns=["Question", "Value"]) 
            st.table(
                df_st,
                # columns=["Question", "Value", "Sources"],
                # width=1000,  # Adjust table width as needed
            )
            source_button1 = st.checkbox(f"Show SourceS")
            if source_button1:
                check(data_list)
            
            st.write(f'Total number of Yes: {count}')

            st.header("Reputation:")
            st.subheader("Sustainability:")
            sus_data,sus_sources=sustainability_award(option)
            sus_data1={
                'Awards': sus_data,
            }
            sus_df=pd.DataFrame(sus_data1)
            st.table(sus_df)
            st.write(f"Total number of awards: {len(sus_data)}")
            show_sus_sources = st.checkbox("Show sources", value=False)
            if show_sus_sources:
                for i in sus_sources:
                    st.write(i)
            st.subheader("Finance:")
            fin_data,fin_sources=finace_awards(option)
            fin_data1={
                'Awards': fin_data,
            }
            fin_df=pd.DataFrame(fin_data1)
            st.table(fin_df)
            st.write(f"Total number of awards: {len(fin_data)}")
            show_fin_sources = st.checkbox("show sources", value=False)
            if show_fin_sources:
                for i in fin_sources:
                    st.write(i)
            st.subheader("Risk Management:")
            risk_data,risk_sources=Risk_management_awards(option)
            risk_data1={
                'Awards': risk_data,
            }
            risk_df=pd.DataFrame(risk_data1)
            st.table(risk_df)
            st.write(f"Total number of awards: {len(risk_data)}")
            show_risk_sources = st.checkbox("Show SOurces", value=False)
            if show_risk_sources:
                for i in risk_sources:
                    st.write(i)
            st.subheader("Governance:")
            Governance_data,Governance_sources=Governance_awards(option)
            Governance_data1={
                'Awards': Governance_data,
            }
            Governance_df=pd.DataFrame(Governance_data1)
            st.table(Governance_df)
            # st.write(f"Total number of awards: {len(Governance_data)}")
            show_Governance_sources = st.checkbox("Show Sources", value=False)
            if show_Governance_sources:
                for i in Governance_sources:
                    st.write(i)
        

        else:
            st.write(f"{option} company data is not available")
            
        
            






