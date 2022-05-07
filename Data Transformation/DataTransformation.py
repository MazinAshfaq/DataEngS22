import pandas as pd
import re

# dataFrame =  pd.read_csv('books.csv', usecols =['Identifier','Place of Publication','Date of Publication','Publisher','Title','Author','Contributors','Flickr URL'])
dataFrame =  pd.read_csv('books.csv')

dataFrame.drop(columns=['Edition Statement', 'Corporate Author', 'Corporate Contributors', 'Former owner', 'Engraver', 'Issuance type', 'Shelfmarks'])

dataFrame['Date of Publication'].str.replace(r'\[.*\]','')
print(dataFrame['Date of Publication'].str.replace(r'\[.*\]',''))

