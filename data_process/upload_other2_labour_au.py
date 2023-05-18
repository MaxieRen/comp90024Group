import json
import couchdb
from couchdb_config import url
import pandas as pd

couch = couchdb.Server(url)
db = couch["labour_au"]

df = pd.read_csv("data/other/labour_aus_20_years_rate.csv")

for i in range(len(df)):
    data_dict = dict()
    
    data_dict['time'] = df['Date'][i]
    data_dict['unemployment_rate'] = df['Unemployment rate (%)'][i]
    data_dict['male_unemployment_rate'] = df['Males Unemployment Rate(%)'][i]
    data_dict['female_unemployment_rate'] = df['Females Unemployment Rate(%)'][i]
    data_dict['persons_unemployment_rate'] = df['Persons Unemployment Rate(%)'][i]
    data_dict['youth_unemployment_rate'] = df['Youth (15-24 years) Unemployment Rate(%)'][i]
    data_dict['male_participation_rate'] = df['Male participation rate'][i]
    data_dict['female_participation_rate'] = df['Female participation rate'][i]
    data_dict['persons_participation_rate'] = df['Persons participation rate'][i]
    
    db.save(data_dict)
    
    
    
    
    
