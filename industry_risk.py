import pandas as pd
import numpy as np
  
data=pd.read_csv("Peer Analyser Data March 2022 to Mar 2023 Pharma Industry.csv")
def industry_specific():    
    # Sample Data
    data=pd.read_csv("Peer Analyser Data March 2022 to Mar 2023 Pharma Industry.csv")

    df = pd.DataFrame(data)
    df_len=len(df)
    # Remove 'N/A' rows
    df = df[df['Impact Value'] != 'N/A']

    # Convert USD to INR and standardize to Cr/Bn
    df['Impact Value'] = df['Impact Value'].apply(lambda x: np.nan if pd.isna(x) else (
        float(x.split()[1]) * 83.13 if 'USD' in x else (
            float(x.split()[1]) * 90.43 if 'EUR' in x else (
                float(x.split()[1]) * 100 if 'Bn' in x and ('USD' in x or 'INR' in x) else (
                float(x.split()[1]) / 10 if 'Mn' in x else (
                    float(x.split()[1]) if 'Cr' in x else np.nan
                )
            )
        )
    )))
    count=df_len
    sum=df['Impact Value'].sum()
    return count,sum

# print(industry_specific())
# df['Impact Value'].to_csv('industry_risk.csv', index=False)
# option='drreddy'
def country_specific(option):    

    df = pd.DataFrame(data)

    # Remove 'N/A' rows
    df = df[df['Source'].str.contains(option, case=False, na=False)]
    # print(df['Impact Value'])
    df_len=len(df)
    # df=df[df['Impact Value'] != 'N/A']
    df = df.dropna(how='any')
    # Convert USD to INR and standardize to Cr/Bn
    df['Impact Value'] = df['Impact Value'].apply(lambda x: np.nan if pd.isna(x) else (
        float(x.split()[1]) * 83.13 if 'USD' in x else (
            float(x.split()[1]) * 90.43 if 'EUR' in x else (
                float(x.split()[1]) * 100 if 'Bn' in x and ('USD' in x or 'INR' in x) else (
                float(x.split()[1]) / 10 if 'Mn' in x else (
                    float(x.split()[1]) if 'Cr' in x else np.nan
                )
            )
        )
    )))
    sum=df['Impact Value'].sum()
    count=df_len
    # print(df['Impact Value'])
    return sum,count


# print(country_specific(option))