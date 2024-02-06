import pandas as pd
import numpy as np
import re,os,glob
import pymongo
  

# client=pymongo.MongoClient('mongodb://localhost:27017/')
# mydb=client['drreddy']
# information=mydb.info
client=pymongo.MongoClient('mongodb+srv://test:test@cluster0.tw5ieeh.mongodb.net/?retryWrites=true&w=majority')

mydb=client.get_database('Udbhata')
information=mydb.companies_data
def tsr(option):
    k=information.find_one({"name":f"{option}"})

    if 'tsr_value' in k:
                    tsr_value=k['tsr_value']
    else:
        from views.reports import run_question

        information.update_one({"name":f"{option}"},{"$set":{
                                                "dividend":dividend
                    }})
        # print(dividend)
    # data=pd.read_csv(f"C:\\Users\\sheik jaheer\\OneDrive\\Desktop\\TYNYBAY\\udbhata\\udbhata-poc-main\\share_price_data\\drreddy.csv")
        data=pd.read_csv(f"C:\\Users\\sheik jaheer\\OneDrive\\Desktop\\TYNYBAY\\udbhata\\udbhata-poc-main\\share_price_data\\{option.lower()}.csv")
        df=pd.DataFrame(data)
        # print(len(df))
        val2023=df.iloc[0,4]
        # print(val2023)

        val2022=df.iloc[len(df)-1,4]
        # print(val2022)   

        # number_only = re.sub(r'\D', '',dividend)
        # print(number_only)

        tsr_value=(float(val2023)-float(val2022))+float(dividend)/float(val2022)
        # print(tsr_value)
        information.update_one({"name":f"{option}"},{"$set":{
                                                    "tsr_value":tsr_value
                        }})
    return tsr_value

print(tsr('drreddy'))

def history(option):
    k=information.find_one({"name":f"{option}"})
    if 'average_days' in k:
                    average_days=k['average_days']
                    # print(f"Average Days to Reach Opening: {average_days}")
    else:
        data=pd.read_csv(f"C:\\Users\\sheik jaheer\\OneDrive\\Desktop\\TYNYBAY\\udbhata\\udbhata-poc-main\\share_price_data\\{option.lower()}.csv")

        dat=pd.DataFrame(data,columns=['Date','Open Price','Close Price','Spread Close-Open'])
        # df=pd.DataFrame(data,columns=['Date','Open Price','Close Price','Spread Close-Open'])
        df=dat[::-1]
        # print(df)
        df['Date'] = pd.to_datetime(df['Date'], infer_datetime_format=True)
        df['Date'] = pd.to_datetime(df['Date'], format='%d-%b-%y')
        # Filter rows where opening_close_diff is less than -10
        filtered_df = df.loc[df['Spread Close-Open'] <= -10]
        # print(filtered_df)
        # variables to accumulate days and count of matching rows
        total_days = 0
        count = 0

        # Iterate through each row in the filtered dataframe
        for index, row in filtered_df.iterrows():
            opening_price = row['Open Price']
            # closing_price = row['Close Price']
            target_date = row['Date']
            
            # Find rows with a closing price within a range and date greater than target_date
            matching_row = df[(df['Close Price'] >= opening_price) & (df['Date'] > target_date)]
            if not matching_row.empty:
            # Get the date from the matching row
                matching_date = matching_row.iloc[0]['Date']

                # Calculate the number of days it took to reach the opening price
                days_to_reach_opening = (pd.to_datetime(matching_date) - pd.to_datetime(target_date)).days

                # Accumulate the days and increment the count
                total_days += days_to_reach_opening
                count += 1
                # print(f"Days to reach opening: {days_to_reach_opening} for {row['Spread Close-Open']}")    
        # Calculate the average number of days
        # print(total_days)
        # print(count)
        if count > 0:
            average_days = total_days / count
            print(f"Average Days to Reach Opening: {average_days}")
        else:
            print("No rows found in 'open-close' column less than -10.")
        average_days=int(average_days)
        information.update_one({"name":f"{option}"},{"$set":{
                                                "average_days":average_days
                    }})
        # doc=information.find_one({"average_days": {"$exists": True}})
        # if doc:
        #     average_days = doc["average_days"]

    return average_days
print(history("drreddy"))