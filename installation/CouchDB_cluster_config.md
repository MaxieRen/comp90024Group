# master node docker
sudo docker volume create --name masternode_data
sudo docker run\
  --detach \
	-p 4369:4369 \
  -p 5984:5984 \
  -p 9100:9100 \
  --name couchdb45.113.234.51\
  -v masternode_data:/opt/couchdb/data \
  --env COUCHDB_USER='admin'\
  --env COUCHDB_PASSWORD='admin'\
  --env COUCHDB_SECRET='a192aeb9904e6590849337933b000c99'\
  --env ERL_FLAGS="-setcookie \"'a192aeb9904e6590849337933b000c99'\" -name \"couchdb@45.113.234.51\""\
  ibmcom/couchdb3:'3.2.1'

# worker 1 docker
sudo docker volume create --name worker1_data
mkdir -p /home/ubuntu/couchdb/data
sudo docker run\
  --detach \
	-p 4369:4369 \
  -p 5984:5984 \
  -p 9100:9100 \
  -v worker1_data:/opt/couchdb/data \
  --name couchdb45.113.235.190\
  --env COUCHDB_USER='admin'\
  --env COUCHDB_PASSWORD='admin'\
  --env COUCHDB_SECRET='a192aeb9904e6590849337933b000c99'\
  --env ERL_FLAGS="-setcookie \"'a192aeb9904e6590849337933b000c99'\" -name \"couchdb@45.113.235.190\""\
  ibmcom/couchdb3:'3.2.1'
  
# worker 2 docker
sudo docker volume create --name worker2_data
sudo docker run\
  --detach \
	-p 4369:4369 \
  -p 5984:5984 \
  -p 9100:9100 \
  -v worker2_data:/opt/couchdb/data \
  --name couchdb45.113.234.130\
  --env COUCHDB_USER='admin'\
  --env COUCHDB_PASSWORD='admin'\
  --env COUCHDB_SECRET='a192aeb9904e6590849337933b000c99'\
  --env ERL_FLAGS="-setcookie \"'a192aeb9904e6590849337933b000c99'\" -name \"couchdb@45.113.234.130\""\
  ibmcom/couchdb3:'3.2.1'


# create culster

# worker 1

curl -X POST -H "Content-Type: application/json" http://admin:admin@45.113.234.51:5984/_cluster_setup -d '{"action": "enable_cluster", "bind_address":"0.0.0.0", "username": "admin", "password":"admin", "port": 5984, "remote_node": "45.113.235.190", "remote_current_user": "admin", "remote_current_password": "admin" }'

curl -X POST -H "Content-Type: application/json" http://admin:admin@45.113.234.51:5984/_cluster_setup -d '{"action": "add_node", "host":"45.113.235.190", "port": "5984", "username": "admin", "password":"admin"}'

# worker 2

curl -X POST -H "Content-Type: application/json" http://admin:admin@45.113.234.51:5984/_cluster_setup -d '{"action": "enable_cluster", "bind_address":"0.0.0.0", "username": "admin", "password":"admin", "port": 5984, "remote_node": "45.113.234.130", "remote_current_user": "admin", "remote_current_password": "admin" }'

curl -X POST -H "Content-Type: application/json" http://admin:admin@45.113.234.51:5984/_cluster_setup -d '{"action": "add_node", "host":"45.113.234.130", "port": "5984", "username": "admin", "password":"admin"}'


# finish cluster setup
curl -X POST -H "Content-Type: application/json" http://admin:admin@45.113.234.51:5984/_cluster_setup -d '{"action": "finish_cluster"}'

# check cluster 
curl -X GET http://admin:admin@45.113.234.51:5984/_membership

# setup photon
couch="-H Content-Type:application/json -X PUT http://admin:admin@45.113.234.51:5984"; \
curl $couch/photon; curl https://raw.githubusercontent.com/ermouth/couch-photon/master/photon.json | \
curl $couch/photon/_design/photon -d @- ; curl $couch/photon/_security -d '{}' ; \
curl $couch/_node/_local/_config/csp/attachments_enable -d '"false"' ; \
curl $couch/_node/_local/_config/chttpd_auth/same_site -d '"lax"' ; 
# check photon
http://45.113.234.51:5984/photon/_design/photon/index.html
