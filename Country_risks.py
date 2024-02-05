import pandas as pd
from country import stre,credit_ratings_algo
# from country_risk_web_scraping import credit_ratings_algo




my_list = stre('drreddy')

def convert_to_number(value):
    if isinstance(value, str):
        if value.isdigit():
            return int(value)
        elif value.isalpha() and value.upper() in 'ABCDEFG':
            # Replace letter with corresponding number from A to G
            return ord(value.upper()) - ord('A') + 1
        elif '/' in value:
            # Extract only the first part of the string before '/'
            return int(value.split('/')[0])
        else:
            try:
                return float(value)
            except ValueError:
                # If the string is not convertible to a number, return the original string
                return value
    else:
        return value

# Apply the conversion function to each element in the list
converted_list = [convert_to_number(value) for value in my_list]

# print(converted_list)

def cumulative_risk():
    Political_Risk_Short_term=round((5/100)*(converted_list[0]/7)*100,2)
    Political_Risk_Medium_long_Term=round((10/100)*(converted_list[1]/7)*100,2)
    Premium_Classification_OECD=round((5/100)*(converted_list[2]/7)*100,2)
    Business_Environment_Risk=round((10/100)*(converted_list[3]/7)*100,2)
    Political_Violence_Risk=round((5/100)*(converted_list[4]/7)*100,2)
    Expropriation_and_Government_Action_Risk=round((20/100)*((converted_list[5]/7)*100),2)
    Currency_Inconvertibility_and_Transfer_Restriction_Risk=round((10/100)*(converted_list[6]/7)*100,2)
    Corruption_Perceptions_Index=round((4/100)*converted_list[7],2)
    Ease_of_Doing_business=round((6/100)*converted_list[8],2)
    Economic_risk=(20/100)*converted_list[9]  # 43 is the sum of all the (Moody's+S&P+Fitch)/3 should find from algorithm(credit rating)
    Competitiveness_Index=round((3/100)*converted_list[10],2)
    Global_Terrorism_Impact=round((2/100)*converted_list[11],2)

    values=[Political_Risk_Short_term,Political_Risk_Medium_long_Term,Premium_Classification_OECD,Business_Environment_Risk,Political_Violence_Risk,Expropriation_and_Government_Action_Risk,
            Currency_Inconvertibility_and_Transfer_Restriction_Risk,Corruption_Perceptions_Index,Ease_of_Doing_business,Economic_risk,
            Competitiveness_Index,Global_Terrorism_Impact]
    
    sum=0
    for value in values:
        sum+=value

        # print(value)
        # print(sum)

    # print(sum)
    return sum


# print(cumulative_risk())







