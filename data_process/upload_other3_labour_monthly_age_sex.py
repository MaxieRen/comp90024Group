import json
import couchdb
from couchdb_config import url
import pandas as pd

couch = couchdb.Server(url)
db = couch["labour_monthly_age_sex"]

df = pd.read_csv("data/other/labour_monthly_age_sex_2019_now.csv")

for i in range(len(df)):
    
    data_dict = dict()
    
    data_dict['time'] = df['Month'][i]
    data_dict['sex'] = df['Sex'][i]
    data_dict['age'] = df['Age'][i]
    data_dict['sa4_code'] = str(df['sa4_code'][i])
    
    data_dict['employed_fulltime'] = int(df["Employed full-time ('000)"][i]) * 1000
    data_dict['employed_parttime'] = int(df["Employed part-time ('000)"][i]) * 1000
    data_dict['unemployed'] = int(df["Unemployed total ('000)"][i]) * 1000
    data_dict['not_in_labour_force'] = int(df["Not in the labour force (NILF) ('000)"][i]) * 1000
    
    db.save(data_dict)
    
    
    
    
    
