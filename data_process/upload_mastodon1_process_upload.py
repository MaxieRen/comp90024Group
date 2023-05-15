import json
from nltk.sentiment import SentimentIntensityAnalyzer
from couchdb_config import url
import couchdb

couch = couchdb.Server(url)
db = couch["mastodon2"]

sid = SentimentIntensityAnalyzer()

def process_mastodone(string):
    string_dict = json.loads(string)
    mastodon_dict = dict()
    
    mastodon_dict["account"] = string_dict["doc"]["account"]["acct"]
    
    text = string_dict["doc"]["content"]
    mastodon_dict["text"] = text
    mastodon_dict["sentiment_neg"] = round(sid.polarity_scores(text)["neg"],4)
    mastodon_dict["sentiment_pos"] = round(sid.polarity_scores(text)["pos"],4)
    mastodon_dict["sentiment_neu"] = round(sid.polarity_scores(text)["neu"],4)
    mastodon_dict["sentiment_com"] = round(sid.polarity_scores(text)["compound"],4)
    
    mastodon_dict["language"] = string_dict["doc"]["language"]
    
    time = string_dict["doc"]["created_at"]
    
    mastodon_dict["year"] = time.split(" ")[0].split("-")[0]
    mastodon_dict["month"] = time.split(" ")[0].split("-")[1]
    mastodon_dict["day"] = time.split(" ")[0].split("-")[2]
    mastodon_dict["hour"] = time.split(" ")[1].split(":")[0]
    
    if mastodon_dict["hour"] in ["09","10","11","12","13","14"]:
        mastodon_dict["activation_time"] = "0"
    elif mastodon_dict["hour"] in ["15","16","17","18","19","20"]:
        mastodon_dict["activation_time"] = "1"
    elif mastodon_dict["hour"] in ["21","22","23","00","01","02"]:
        mastodon_dict["activation_time"] = "2"
    else:
        mastodon_dict["activation_time"] = "3"
    
    hashtag_list = []
    for i in string_dict["doc"]["tags"]:
        hashtag_list.append(i["name"])
    
    mastodon_dict["hashtag"] = hashtag_list
    
    return mastodon_dict

file_name = "data/mastodon/mastodon.json"

with open(file_name, "r", encoding="utf-8") as mastodon_file:
    
    new_line = mastodon_file.readline()
    while new_line:
        try:
            new_line = mastodon_file.readline().strip().strip(",")
            mastondon_dict = process_mastodone(new_line)
            db.save(mastondon_dict)
        except:
            pass


