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
db_name = 'mastodon2'

# if not exist, create one
if db_name not in couch:
    db = couch.create(db_name)
else:
    db = couch[db_name]

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
            "created_at": {
                "$gt": param
            }
        }
    }
    # Execute the query
    results = []
    for row in db.find(query):
        results.append(row)
    # Return the results as JSON
    return {'data': results}








# @app.route('/api_1', methods=['GET', 'POST', 'DELETE'])
# def api_1():
#     if request.method == 'POST':
#         # using an existing view
#         view = db.view('languages/judge', group_level=1)
#         # Retrieve the view results
#         results = {}
#         for row in view:
#             results[row.key] = row.value
#         # Return the results as JSON
#         return {'data': results}
#     else:
#         view = db.view('languages/langAvg', group_level=1)
#         # Retrieve the view results
#         results = {}
#         print(view)
#         for row in view:
#             results[row.key] = row.value
#         # Return the results as JSON
#         return {'data': results}


class api_2(Resource):

    def get(self, id=None):
        if not id:
            # do sth
            return [5, 40, 36, 40, 30, 20, 15]
        else:
            print(id)
            # do sth
            return res2

    def post(self):
        # do sth
        return res1

    def delete(self, id=None):
        if not id:
            # do sth
            return "no id"
        else:
            doc = db.get(id)
            if doc:
                db.delete(doc)
                return 'Document deleted successfully'
            else:
                return 'Document not found'


api.add_resource(api_2, '/api_2', '/api_2/<id>')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port='8081')
