import json
import couchdb
import os
import re
import pandas as pd
import random
from couchdb_config import url
from mpi4py import MPI
import nltk
from collections import Counter

file_name = "data/twitter/twitter-huge.json"

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

totl_size = os.path.getsize(file_name)
part_size = totl_size // size
read_srt = part_size * rank
read_end = part_size * (rank + 1)

couch = couchdb.Server(url)
db = couch["word_cloud_twitter"]

sid = nltk.sentiment.SentimentIntensityAnalyzer()

def get_time(string):
    
    string_list = string.split("T")
    date_list = string_list[0].split("-")
    time_list = string_list[1].split(":")
    
    year = date_list[0]
    month = date_list[1]
    day = date_list[2]
    hour = time_list[0]
    
    return year, month, day, hour

place_db = pd.read_csv("data/other/position.csv")
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

counter_dict = dict()
sa4_df = pd.read_csv("data/other/sa4_list.csv")
for i in range(len(sa4_df)):
    counter_dict[str(sa4_df["SA4_CODE_2016"][i])] = dict()

def count(sa4_code, text):
    word_list = []
    for token in nltk.word_tokenize(text):
        token = re.sub("[^a-zA-Z]", "", token.lower())
        if token != "":
            word_list.append(token)
    
    global counter_dict
    for word in word_list:
        if word in counter_dict[sa4_code]:
            counter_dict[sa4_code][word] += 1
        else:
            counter_dict[sa4_code][word] = 1

with open(file_name, "r", encoding="utf-8") as twitter_file:
    twitter_file.seek(read_srt)
    new_line = twitter_file.readline()
    while new_line:
        new_line = twitter_file.readline()
        if '"places"' in new_line:
            try:
                twitter_dict = process_newline(new_line)
                count(twitter_dict["sa4_code"], twitter_dict["text"])
            except:
                pass
            if twitter_file.tell() > read_end:
                break

counter_dict_gather = comm.gather(counter_dict, root = 0)

if root == 0:
    
    languages = nltk.corpus.stopwords.fileids()
    stopwords = ["https", "nt", "p"]
    for lang in languages:
        stopwords += nltk.corpus.stopwords.words(lang)
    
    sa4_code_list = list(pd.read_csv("data/other/sa4_position.csv")["sa4_code"])
    
    wordcloud_dict0 = counter_dict_gather[0]
    wordcloud_dict1 = counter_dict_gather[1]
    wordcloud_dict2 = counter_dict_gather[2]
    wordcloud_dict3 = counter_dict_gather[3]
    wordcloud_dict4 = counter_dict_gather[4]
    wordcloud_dict5 = counter_dict_gather[5]
    wordcloud_dict6 = counter_dict_gather[6]
    wordcloud_dict7 = counter_dict_gather[7]
    
    for sa4_code in sa4_code_list:
        sa4_code = str(sa4_code)
        counter0 = Counter(wordcloud_dict0[sa4_code])
        counter1 = Counter(wordcloud_dict1[sa4_code])
        counter2 = Counter(wordcloud_dict2[sa4_code])
        counter3 = Counter(wordcloud_dict3[sa4_code])
        counter4 = Counter(wordcloud_dict4[sa4_code])
        counter5 = Counter(wordcloud_dict5[sa4_code])
        counter6 = Counter(wordcloud_dict6[sa4_code])
        counter7 = Counter(wordcloud_dict7[sa4_code])
        counter = counter0 + counter1 + counter2 + counter3 + counter4 + counter5 + counter6 + counter7
        
        temp_dict = dict()
        for key, value in counter.items():
            if key not in stopwords:
                temp_dict[key] = value
        temp_dict = Counter(temp_dict)
        top20 = temp_dict.most_common(20)
        
        counter_final = dict()
        for key, value in top20:
            counter_final[key] = value
        
        final_dict = dict()
        final_dict["sa4_code"] = sa4_code
        final_dict["world_cloud"] = counter_final
        
        db.save(final_dict)
        
# mpiexec -n 8 --oversubscribe python3 upload_twitter2_wordcloud.py