import json
import couchdb
from couchdb_config import url
import pandas as pd

df = pd.read_csv("data/other/labour_2022.csv")

couch = couchdb.Server(url)
db = couch["labour_2022"]


for i in range(len(df)):
    data_dict = dict()
    
    data_dict["sa4_code"] = str(df["SA4_CODE21"][i])
    data_dict["sa4_name"] = str(df["SA4_NAME21"][i])
    
    data_dict["2022_working_age_population"] = int(df["Working Age Population (15-64)"][i])
    data_dict["2022_employed_15_plus"] = int(df["Employed (15+)"][i])
    data_dict["2022_employment_rate_15_64"] = round(df["Employment Rate (15-64)"][i],2)
    data_dict["2022_participation_rate_15_plus"] = round(df["Participation Rate (15+)"][i],2)
    data_dict["2022_unemployment_rate_15_plus"] = round(df["Unemployment Rate (15+)"][i],2)
    data_dict["2022_youth_unemployment_rate_15_24"] = round(df["Youth Unemployment Rate (15-24)"][i],2)
    
    db.save(data_dict)
    




