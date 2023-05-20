import json
import couchdb
from couchdb_config import url
import pandas as pd

couch = couchdb.Server(url)
db = couch["sudo_sa4_industry"]

file_path = "data/sudo/sa4_industry/"
file_names = [file_path+"ind1.csv", file_path+"ind2.csv", file_path+"ind3.csv", file_path+"ind4.csv", file_path+"ind5.csv", 
              file_path+"ind6.csv", file_path+"ind7.csv", file_path+"ind8.csv", file_path+"ind9.csv", file_path+"ind10.csv",
              file_path+"ind11.csv", file_path+"ind12.csv", file_path+"ind13.csv", file_path+"ind14.csv", file_path+"ind15.csv",
              file_path+"ind16.csv", file_path+"ind17.csv", file_path+"ind18.csv", file_path+"ind19.csv"]

for file_name in file_names:
    
    df = pd.read_csv(file_name)
    
    for i in range(len(df)):
        
        data_dict = dict()
        
        data_dict["industry"] = str(df[" ind"][i])
        data_dict["sa4_code"] = str(df[" sa4_code_2016"][i])
        data_dict["sa4_name"] = str(df[" sa4_name_2016"][i])
        data_dict["sa4_state"] = str(df[" state_name_abbr"][i])
        
        data_dict["2016"] = int(df[" nov_16"][i]) if not pd.isna(df[" nov_16"][i]) else None
        data_dict["2020"] = int(df[" nov_20"][i]) if not pd.isna(df[" nov_20"][i]) else None
        data_dict["2021"] = int(df[" nov_21"][i]) if not pd.isna(df[" nov_21"][i]) else None
        
        db.save(data_dict)
        
