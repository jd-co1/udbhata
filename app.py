import streamlit as st
from streamlit_option_menu import option_menu
from views.companies import load_companies
# from views.reports import load_reports
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)
name, authentication_status, username = authenticator.login()
if authentication_status:
    st.sidebar.info(f'Welcome *{name}* :sunglasses:')
    with st.sidebar:
            selected = option_menu(menu_title="Udbhata",options= ["Companies", 'Reports'], 
                icons=['search', 'upload'], menu_icon="cast", default_index=0)
    authenticator.logout('Logout', 'sidebar', key='unique_key')
    if selected=="Companies":
        load_companies()
    # if selected=="Reports":
    #     load_reports()
    if selected == "Logout":
        authentication_status=False
            
elif authentication_status is False:
    st.error('Username/password is incorrect')
elif authentication_status is None:
    st.warning('Please enter your username and password')


    

