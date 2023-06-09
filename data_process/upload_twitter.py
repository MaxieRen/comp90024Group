# Packages
import json
import couchdb
import os
import pandas as pd
import random
from couchdb_config import url
from mpi4py import MPI
from nltk.sentiment import SentimentIntensityAnalyzer

# File path
file_name = "data/twitter/twitter-huge.json"

# MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

totl_size = os.path.getsize(file_name)
part_size = totl_size // size
read_srt = part_size * rank
read_end = part_size * (rank + 1)

# CouchDB
couch = couchdb.Server(url)
db = couch["twitter_db2"]

# Sentiment Analysis
sid = SentimentIntensityAnalyzer()

# Get Time
def get_time(string):
    
    string_list = string.split("T")
    date_list = string_list[0].split("-")
    time_list = string_list[1].split(":")
    
    year = date_list[0]
    month = date_list[1]
    day = date_list[2]
    hour = time_list[0]
    
    return year, month, day, hour

# Get Place
place_db = pd.read_csv("data/geom/position.csv")
def place(w,s,e,n):
    c_lon = (w + e) / 2
    c_lat = (s + n) / 2
    candidate_loc = []
    for i in range(len(place_db)):
        sa4_code = place_db["sa4_code"][i]
        sa4_name = place_db["sa4_name"][i]
        w1 = place_db["w"][i]
        s1 = place_db["s"][i]
        e1 = place_db["e"][i]
        n1 = place_db["n"][i]
        if w1 < c_lon < e1 and s1 < c_lat < n1:
            candidate_loc.append((sa4_code, sa4_name))
    if len(candidate_loc) >= 1:
        location = random.choice(candidate_loc)
    else:
        location = ("NAN", "NAN")
    
    return location


# Process Twitter String
def process_newline(string):
    string = string.strip().strip(",")
    string_dict = json.loads(string)
    
    twitter_dict = dict()
    
    if '"text"' in string:
        text = string_dict["doc"]["data"]["text"]
        twitter_dict["text"] = text
        twitter_dict["sentiment_neg"] = round(sid.polarity_scores(text)["neg"],4)
        twitter_dict["sentiment_pos"] = round(sid.polarity_scores(text)["pos"],4)
        twitter_dict["sentiment_neu"] = round(sid.polarity_scores(text)["neu"],4)
        twitter_dict["sentiment_com"] = round(sid.polarity_scores(text)["compound"],4)
    else:
        twitter_dict["text"] = None
        twitter_dict["sentiment_neg"] = None
        twitter_dict["sentiment_pos"] = None
        twitter_dict["sentiment_neu"] = None
        twitter_dict["sentiment_com"] = None
    
    if '"tokens"' in string:
        twitter_dict["token"] = string_dict["value"]["tokens"]
    else:
        twitter_dict["token"] = None
    
    if '"sentiment"' in string:
        twitter_dict["sentiment"] = string_dict["doc"]["data"]["sentiment"]
    else:
        twitter_dict["sentiment"] = None
    
    if '"lang"' in string:
        twitter_dict["language"] = string_dict["doc"]["data"]["lang"]
    else:
        twitter_dict["language"] = None
    
    if '"created_at"' in string:
        year, month, day, hour = get_time(string_dict["doc"]["data"]["created_at"])
        twitter_dict["year"] = str(year)
        twitter_dict["month"] = str(month)
        twitter_dict["day"] = str(day)
        twitter_dict["hour"] = str(hour)
    else:
        twitter_dict["year"] = None
        twitter_dict["month"] = None
        twitter_dict["day"] = None
        twitter_dict["hour"] = None
    
    if '"places"' in string:
        location_range = string_dict["doc"]["includes"]["places"][0]["geo"]["bbox"]
        w = location_range[0]
        s = location_range[1]
        e = location_range[2]
        n = location_range[3]
        location = place(w, s, e, n)
        twitter_dict["sa4_code"] = str(location[0])
        twitter_dict["sa4_name"] = str(location[1])
    else:
        twitter_dict["sa4_code"] = "NAN"
        twitter_dict["sa4_name"] = "NAN"
    
    if '"hashtags"' in string:
        twitter_dict["hashtags"] = string_dict["doc"]["data"]["entities"]["hashtags"][0]["tag"]
    else:
        twitter_dict["hashtags"] = None
    
    return twitter_dict

# Read & Process
with open(file_name, "r", encoding="utf-8") as twitter_file:
    twitter_file.seek(read_srt)
    new_line = twitter_file.readline()
    while new_line:
        new_line = twitter_file.readline()
        if '"places"' in new_line:
            try:
                twitter_dict = process_newline(new_line)
                if twitter_dict["sa4_code"] != "NAN":
                    doc_id, doc_rev = db.save(twitter_dict)
            except:
                pass
            if twitter_file.tell() > read_end:
                break

# mpiexec -n 8 --oversubscribe python3 upload_twitter.py