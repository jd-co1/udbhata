import pandas as pd
import numpy as np
import pymongo
  

# client=pymongo.MongoClient('mongodb://localhost:27017/')
# mydb=client['drreddy']
# information=mydb.info
client=pymongo.MongoClient('mongodb+srv://test:test@cluster0.tw5ieeh.mongodb.net/?retryWrites=true&w=majority')

mydb=client.get_database('Udbhata')
information=mydb.companies_data
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
    j=information.find_one({"name":f"{option}"})
    if "company_Impact" in j:
        tsr=j["company_Impact"]
        return round(tsr,2)
    else:
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
        information.update_one({"name":f"{option}"},{"$set":{
                                                "company_Impact":sum,
                                                "company_count":count
        }})
        # print(df['Impact Value'])
        return sum,count



# print(country_specific(option))