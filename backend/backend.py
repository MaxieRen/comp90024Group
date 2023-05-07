from flask import Flask, render_template, request
from flask_restful import Api, Resource
from flask_cors import CORS
import couchdb

# authentication
admin = 'admin'
password = 'password'
url = f'http://{admin}:{password}@172.26.135.248:5984/'

# get couchdb instance
couch = couchdb.Server(url)

# indicate the db name
db_name = ['twitter_db','mastodon_db','labor_market_db']

# if not exist, create one
# for name in db_name:
#     if name not in couch:
#         db = couch.create(name)

db_tt = couch['twitter_db']
db_md = couch['mastodon_db']
db_lm = couch['labor_market_db']

app = Flask(__name__)
api = Api(app)
CORS(app)
#CORS(app, origins=['http://127.0.0.1:8080'])

res1 = {'code': 200, 'msg': 'OK', 'data': {}}
res2 = {'code': 200, 'msg': 'OK', 'data': {'array': ['data1', 'data2', 'data3'], 'str': 'string'}}


#homepage
@app.route('/')
def root():
    return render_template('Index.html')


# default GET
@app.route('/api_0/<param>')
def api_0(param):
    # Mango Queries
    query = {
        "selector": {
            "language": {
                "$eq": param
            }
        }
    }
    # Execute the query
    results = []
    for row in db_tt.find(query):
        results.append(row)
    # Return the results as JSON
    return {'data': results}



@app.route('/api_1', methods=['GET', 'POST', 'DELETE'])
def api_1():
    if request.method == 'POST':
        # using an existing view
        view = db_tt.view('languages/judge', group_level = 1)
        # Retrieve the view results
        results = {}
        for row in view:
            results[row.key] = row.value
        # Return the results as JSON
        return {'data': results}
    else:
        view = db_tt.view('languages/langAvg', group_level = 1)
        # Retrieve the view results
        results = {}
        print(view)
        for row in view:
            results[row.key] = row.value
        # Return the results as JSON
        return {'data': results}


if __name__ == '__main__':
    app.run(debug=True, host='45.113.235.46', port='8081')