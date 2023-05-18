import json
import nltk
from couchdb_config import url
import couchdb
from nltk.sentiment import SentimentIntensityAnalyzer

couch = couchdb.Server(url)
db = couch["mastodon_au"]

sid = SentimentIntensityAnalyzer()

def process_mastodone(string):
    string_dict = json.loads(string)
    mastodon_dict = dict()
    
    text = string_dict["doc"]["content"]
    mastodon_dict["content"] = text
    mastodon_dict["sentiment_neg"] = round(sid.polarity_scores(text)["neg"],4)
    mastodon_dict["sentiment_pos"] = round(sid.polarity_scores(text)["pos"],4)
    mastodon_dict["sentiment_neu"] = round(sid.polarity_scores(text)["neu"],4)
    mastodon_dict["sentiment_com"] = round(sid.polarity_scores(text)["compound"],4)
    
    mastodon_dict["language"] = string_dict["doc"]["language"]
    
    time = string_dict["doc"]["created_at"]
    
    mastodon_dict["year"] = int(time.split(" ")[0].split("-")[0])
    mastodon_dict["month"] = int(time.split(" ")[0].split("-")[1])
    mastodon_dict["day"] = int(time.split(" ")[0].split("-")[2])
    mastodon_dict["hour"] = int(time.split(" ")[1].split(":")[0])
    
    hashtag_list = []
    for i in string_dict["doc"]["tags"]:
        hashtag_list.append(i["name"])
    
    mastodon_dict["tags"] = hashtag_list
    
    return mastodon_dict

file_name = "data/mastodon/mastodon_au.json"

with open(file_name, "r", encoding="utf-8") as mastodon_file:
    new_line = mastodon_file.readline()
    count = 0
    while new_line:
        try:
            new_line = mastodon_file.readline().strip().strip(",")
            mastondon_dict = process_mastodone(new_line)
            db.save(mastondon_dict)
        except:
            pass

