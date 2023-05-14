import couchdb
from mastodon import Mastodon, StreamListener
import json
import html2text
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import datetime
import argparse
import os

nltk.download('vader_lexicon')

# authentication
class ConnectCouchDB:
    def __init__(self, admin, password, ipAddress):
        self.admin = admin
        self.password = password
        self.address = ipAddress
        self.url = f'http://{self.admin}:{self.password}@{self.address}:5984/'
    
    def connect(self):
        couch = couchdb.Server(self.url)
        return couch

    def createDB(self, couch, dbName):
        if dbName not in couch:
            db = couch.create(dbName)
        else:
            db = couch[dbName]
        return db


# optional, better not hardcode here
def connectMastodon(server, token):
    try:
        m = Mastodon(
            # your server here
            api_base_url=f'https://{server}/',
            access_token=token
        )
    except:
        print("Error: Mastodon connection failed")
    return m

def get_time(date_string):

    year = date_string.year
    month = date_string.month
    day = date_string.day
    hour = date_string.hour
    return year, month, day, hour

def get_sentiment(text):
    sid = SentimentIntensityAnalyzer()
    ss = sid.polarity_scores(text)
    # round the score to 4 decimal places
    ss = {key: round(value, 4) for key, value in ss.items()}
    return ss['neg'], ss['pos'], ss['neu'], ss['compound']

def preProcess(status):
    result = {'content': '', 'language': '', 'tags': [], "sentiment_neg": 0,
  "sentiment_pos": 0, "sentiment_neu": 0, "sentiment_com": 0,"year": "", "month": "", "day": "","hour": ""}
    if status.get('content'):
        result['content'] = html2text.html2text(status.get('content'))
        result['sentiment_neg'], result['sentiment_pos'], result["sentiment_neu"], result['sentiment_com'] = get_sentiment(status.get('content'))
    if status.get('created_at'):
        result['year'], result['month'], result['day'], result['hour'] = get_time(status.get('created_at'))
    if status.get('language'):
        result['language'] = status.get('language')
    if status.get('tags'):
        result['tags'] = list(map(lambda x: x.get('name'), status.get('tags')))
    return result

# listen on the timeline
class Listener(StreamListener):
    # called when receiving new post or status update
    def __init__(self,db):
        super().__init__()
        self.db = db
    def on_update(self, status):
        
        result = preProcess(status)
        json_str = json.dumps(result, indent=2, sort_keys=True, default=str)
        doc_id, doc_rev = self.db.save(json.loads(json_str))

parser = argparse.ArgumentParser()
parser.add_argument('--user', type=str, default='admin', help='couchdb admin')
parser.add_argument('--password', type=str, default='password', help='couchdb password')
parser.add_argument('--dbName', type=str, default="mastodon_data", help='couchdb database name')
parser.add_argument('--ip', type=str, default="127.0.0.1", help='couchdb ip address')
parser.add_argument('--server', type=str, default='aus.social', help='mastodon server url')
parser.add_argument('--token', type=str, default='AvLtf57hHjGtSP5Qq_t-UyAfVABievlLY9Toba3RkZ8', help='mastodon token')
args = parser.parse_args()

# DB_USERNAME = os.getenv('DB_USERNAME', 'admin')
# DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')
# DB_NAME = os.getenv('DB_NAME', 'mastodon_social_cleandata')
# DB_IP = os.getenv('DB_IP', '172.26.135.248')
# MASTODON_SERVER = os.getenv('MASTODON_SERVER', 'aus.social')
# MASTODON_TOKEN = os.getenv('MASTODON_TOKEN', 'AvLtf57hHjGtSP5Qq_t-UyAfVABievlLY9Toba3RkZ8')

# db = ConnectCouchDB(DB_USERNAME, DB_PASSWORD, DB_IP)
# db_handle = db.createDB(db.connect(), DB_NAME)
# mastodon = connectMastodon(MASTODON_SERVER, MASTODON_TOKEN)
# mastodon.stream_public(Listener(db_handle))

db = ConnectCouchDB(args.user, args.password, args.ip)
db_handle = db.createDB(db.connect(), args.dbName)
mastodon = connectMastodon(args.server, args.token)
mastodon.stream_public(Listener(db_handle))

# nohup python3 Mastodon_client.py --user admin --password password --dbName mastodon_social_cleandata --ip 127.0.0.1 --server aus.social --token AvLtf57hHjGtSP5Qq_t-UyAfVABievlLY9Toba3RkZ8 2>&1 & 

