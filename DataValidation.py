import pandas as pd


dataFrame =  pd.read_csv('OregonHwy26CrashDatafor2019-CrashesonHwy26during2019.csv')

# Assertions
# Existence
# Every Crash Needs atleast one Car


# Limit
# All crashes must be within January to December
assert dataFrame['Crash Month'].dropna() < 12, "Data is not within valid months"
assert dataFrame['Crash Month'].dropna() > 1, "Data is not within valid months"

# All speed involved flags must be US or OR
if (dataFrame['Speed Involved Flag'].dropna() == 'US' or dataFrame['Speed Involved Flag'].dropna() == 'US'):
    print("Valid Speed Involved Flags")
else:
    print("NOT Valid Speed Involved Flags")

if (dataFrame['Latitude'].dropna() == '44' or dataFrame['Longitude'].dropna() == '-122'):
    print("Valid Latitude and Longitude")
else:
    print("NOT Valid Latitude and Longitude")

# Existence
# Every crash must be on earth (check to see the coodrinates)
assert dataFrame['']
