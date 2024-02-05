import streamlit as st
import pandas as pd

# Load existing data from file
try:
    df = pd.read_csv("data.csv", index_col=0)
except FileNotFoundError:
    df = pd.DataFrame(columns=["Key"])

def manager():
    with st.expander("Example"):
        user_input = st.text_input("Enter a key")
        add_button = st.button("Add", key='add_button')
        while True:
            if add_button:
                if len(user_input) > 0:
                    df = pd.DataFrame({"Key": [user_input]})
                    df.to_csv("data.csv")
                    st.success("Key added successfully!")
                else:
                    st.warning("Enter text")

if __name__ == '__main__':
    manager()
