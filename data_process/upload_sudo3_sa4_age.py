import json
import couchdb
from couchdb_config import url
import pandas as pd

couch = couchdb.Server(url)
db = couch["sudo_sa4_age"]

file_path = "data/sudo/sa4_age/"
file_names = [file_path+"age1.csv", file_path+"age2.csv", file_path+"age3.csv", file_path+"age4.csv", file_path+"age5.csv", file_path+"age6.csv"]

for file_name in file_names:
    
    df = pd.read_csv(file_name)
    
    for i in range(len(df)):
        
        data_dict = dict()
        
        data_dict["age_group"] = str(df[" age_group"][i])
        data_dict["sa4_code"] = str(df[" sa4_code_2016"][i])
        data_dict["sa4_name"] = str(df[" sa4_name_2016"][i])
        data_dict["sa4_state"] = str(df[" state_name_abbr"][i])
        
        data_dict["2016"] = int(df[" dec_16"][i]) if not pd.isna(df[" dec_16"][i]) else None
        data_dict["2020"] = int(df[" dec_20"][i]) if not pd.isna(df[" dec_20"][i]) else None
        data_dict["2021"] = int(df[" dec_21"][i]) if not pd.isna(df[" dec_21"][i]) else None
        
        db.save(data_dict)
        