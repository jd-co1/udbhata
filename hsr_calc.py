import pandas as pd
import app


def history(option):
    data=pd.read_csv(f"C:\\Users\\sheik jaheer\\OneDrive\\Desktop\\TYNYBAY\\udbhata\\udbhata-poc-main\\share_price_data\\{option.lower()}.csv")


    df=pd.DataFrame(data,columns=['Date','Open Price','Close Price','Spread Close-Open'])
    # print(df)

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

    # Calculate the average number of days
    if count > 0:
        average_days = total_days / count
        print(f"Average Days to Reach Opening: {average_days}")
    else:
        print("No rows found in 'open-close' column less than -10.")
    return average_days