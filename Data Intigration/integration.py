import pandas as pd
#County + state as the key 
#

county_info_df = pd.read_csv('acs2017_census_tract_data.csv',usecols=['State','County','TotalPop','Poverty','IncomePerCap'])
# county_info_df = county_data_df.groupby(['State','County']).sum()

#county_info_df['County2'] = county_info_df['County'] + county_info_df['State']

#county_info_df = county_info_df.longstrings.map(hash)
result = county_info_df[county_info_df["County"] == "Loudoun County"].groupby(['State','County']).sum()
print(result)