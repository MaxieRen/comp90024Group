import couchdb
import json
from flask import Flask, render_template
from flask_cors import CORS
from flask_restful import Api, Resource
import math
import numpy as np

# authentication
admin = 'admin'
password = 'admin'
url = f'http://{admin}:{password}@45.113.234.51:5984/'

# get couchdb instance
couch = couchdb.Server(url)

# indicate the db name


app = Flask(__name__)
api = Api(app)
CORS(app)


@app.route('/api_word_cloud/')
def api_word_cloud():
    # Mango Queries
    db = couch['word_cloud_mastodon']
    query = {
        
            "selector": {
            "_id": {
                "$gt": 1
            }
        }
        
    }
    # Execute the query
   
    query_result = db.find(query)
    res = []
    for row in query_result:
        for k,v in row.items():
            res.append({'name':k,'weight':v}) 
    return res[2:]

@app.route('/api_word_cloud_twitter/<address_code>')
def api_word_cloud_twitter(address_code):
    db = couch['word_cloud_twitter']
    # Mango Queries
    query = {
   "selector": {
      "sa4_code": {
         "$eq": str(address_code)
      }
   },
   "fields": ["world_cloud"]
}
    # Execute the query
   
    query_result = db.find(query)
    for row in query_result:
        res = [{'name':k,'weight':v} for k,v in row.get("world_cloud").items()]
         
    return res

@app.route('/api_overview/<rate>')
def api_overview(rate):
    db = couch['labour_au']
    skip = 0
    final_lst = []
    while True:

        query = {
    
            "selector": {
                rate: {
                    "$exists": True
                }
            },
            "fields": [
                rate
            ],
            "limit": 25,
            "skip": skip

            }
        # Execute the query
    
        query_result = db.find(query)
        res = [row.get(rate) for row in query_result]
        final_lst.extend(res)
        if len(res) == 25:
            skip = skip + 25
        else:
            break
    
    return final_lst

@app.route('/mastodon_activation_time/')
def mastodon_activation_time():
    mastodon_db_lst = ["mastodon", "mastodon_au"]
    result = []
    for db_name in mastodon_db_lst:
        db_mastodon2 = couch[db_name]
        query_result_mastodon2 = db_mastodon2.view("DesignDoc/actView", group_level=1)
        temp = [row.get("value") for row in query_result_mastodon2]
        result.append(temp)
    final_result = [sum(i) for i in zip(*result)]
    return final_result


@app.route('/age_population/<year>/<employed_status>')
def age_population(year, employed_status):
    db = couch['labour_monthly_age_sex']
    query_result = db.view("Docs/YASView", group_level=2)
    result = [row.get('value').get(employed_status)/10**7 for row in query_result if row.get('key')[0] == int(year)]
    
    return result

@app.route('/unemployment_age/<sa4_code>/<sex>')
def unemployment_age(sa4_code, sex):
    db = couch['labour_monthly_age_sex']
    query_result = db.view("Docs/unemployment_age", group_level=3)
    # result = [row for row in query_result]
    result = [row.get('value') for row in query_result if row.get('key')[0] == sa4_code and row.get('key')[2] == sex]
    result = list(map(lambda x: round(x / 4, 2), result))
    return result

@app.route('/insights/<sa4_code>/<attr_name>')
def insights(sa4_code,attr_name):
    db = couch['labour_2022']
    query = {
   "selector": {
      "_id": {
         "$gt": 1
      }
   }
}
    query_result = db.find(query)
    # result = [row for row in query_result]
    result = [row.get(attr_name) for row in query_result if row.get('sa4_code') == sa4_code]
    
    return result

@app.route('/count_mastodon/')
def count_mastodon():
    mastodon_db = ['mastodon', 'mastodon_au']
    total_size = 0
    for name in mastodon_db:
        db = couch[name]
        query_result = db.info()
        db_size = query_result.get('doc_count')
        total_size = total_size + db_size
    return str(f'{total_size:,}')

@app.route('/count_mastodon_twitter/')
def count_mastodon_twitter():
    mastodon_db = ['mastodon', 'mastodon_au','twitter']
    total_size = 0
    for name in mastodon_db:
        db = couch[name]
        query_result = db.info()
        db_size = query_result.get('doc_count')
        total_size = total_size + db_size
    return str(f'{total_size:,}')


@app.route('/total_word_collect', methods=['GET', 'POST'])
def api_4():
    n_db_name = 'word_cloud_twitter'
    db_name = couch[n_db_name]

    total_word_dict = {}
    for row_id in db_name:
        query = {
            'selector':{
                '_id':row_id
            }
        }
        for right_row in db_name.find(query):
            region_word_dict = right_row['world_cloud']
            for key, items in region_word_dict.items():
                if key in total_word_dict.keys():
                    total_word_dict[key] += items
                else:
                    total_word_dict[key] = items
    dict_list = []
    key_l = []
    items_l = []
    for key, items in total_word_dict.items():
        key_l.append(key)
        items_l.append(items)

    index = np.argsort(-np.array(items_l))
    for i in index[:30]:
        sort_dict = {}
        sort_dict['name'] = key_l[i]
        sort_dict['weight'] = items_l[i]
        dict_list.append(sort_dict)

    return dict_list

@app.route('/area_active_time/<sa4>/<time_slot>', methods=['GET', 'POST']) # active_time
def api_6(sa4,time_slot):
    db_name = 'example'
    db = couch[db_name]
    view_result = db.view('active-time-ex/active-time', group_level=1)
    key_list = ['1st', '2nd', '3rd', '4th']
    out_list = []
    for row in view_result:
        if row.get('key') == sa4:
            result_dict = row.get('value')
            for val in key_list:
                if val in result_dict.keys():
                    out_list.append(result_dict[val])
                else:
                    out_list.append(0)
    if int(time_slot) < len(out_list) - 1:
        content = str(f'{out_list[int(time_slot)]:,}')
    else:
        return str(0)
    return content

@app.route('/labour_2022/<sa4>/<param>', methods=['GET', 'POST']) # unemployment
def api_7(sa4, param):
    db_name = 'labour_2022'
    db = couch[db_name]
    query = {
        'selector':{
            'sa4_code':sa4
        }
    }
    out_list = []
    for row in db.find(query):
        out_list.append(row[param])
    if out_list:
        if param != '2022_working_age_population':
            content = str(f'{out_list[0]}%')
        else:
            content = str(f'{out_list[0]:,}')
    else:
        content = str(0)
    return content

@app.route('/twitter_user_number/<sa4>', methods=['GET', 'POST']) # twitter user number
def api_8(sa4):
    db_name = 'example'
    db = couch[db_name]
    db_view = db.view('user-num-ex/user-num', group_level=1)
    out_list = []
    for row in db_view:
        if row.get('key')[0] == sa4:
            out_list.append(row.get('value'))
    if out_list == []:
        out_list.append(0)
    content = str(f'{out_list[0]:,}')
    return content

@app.route('/satisfaction/<sa4>', methods=['GET', 'POST']) # sentiment percentage [pos, neu, neg]
def api_9(sa4):
    db_name = 'example'
    db = couch[db_name]
    db_view = db.view('sentiment-ex/sentiment', group_level=1)
    result_dict = None
    key_list = ['pos', 'neu', 'neg']
    out_list = []
    for row in db_view:
        if row:
            if row.get('key') == sa4:
                result_dict = row.get('value')

    for key in key_list:
        if result_dict:
            if key in result_dict.keys():
                out_list.append(result_dict[key])
            else:
                out_list.append(0)

    if out_list == []:
        return str(f'{0:.2f}%')
    else:
        output = [(num / sum(out_list)) for num in out_list]
    content = str(f'{output[0] * 100:.2f}%')
    return content

@app.route('/active_time_all_twitter/', methods=['GET', 'POST']) # active time total
def api_10():
    db_name = 'example'
    db = couch[db_name]
    view_result = db.view('active-time-ex/active-time', group_level=1)
    out_dict = {'1st':0, '2nd':0, '3rd':0, '4th':0}
    for row in view_result:
        result_dict = row.get('value')
        for key in out_dict.keys():
            if key in result_dict.keys():
                out_dict[key] += result_dict[key]
    out_list = []
    for key, items in out_dict.items():
        out_list.append(items)

    return out_list

@app.route('/sentiment_number/<param>', methods=['GET', 'POST']) # sentiment number [pos, neu, neg]
def api_11(param):
    db_name_list = ['mastodon', 'mastodon_au']
    out_dict = {'pos':0, 'neu':0, 'neg':0}
    for db_name in db_name_list:
        db = couch[db_name]
        db_view = db.view('DesignDoc/sentimentView', group_level=1)
        for row in db_view:
            if row.key in out_dict.keys():
                out_dict[row.get('key')] += row.get('value')

    out_list = [out_dict['pos'], out_dict['neu'], out_dict['neg']]
    if out_list == []:
        return str(f'{0:,}')
    elif param == 'pos':
        return str(f'{out_list[0]:,}')
    elif param == 'neu':
        return str(f'{out_list[1]:,}')
    else:
        return str(f'{out_list[2]:,}')
    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8081')
    # app.run(debug=True, host='127.0.0.1', port='8081')
