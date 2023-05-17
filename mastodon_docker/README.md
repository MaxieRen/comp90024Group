`sudo docker build -t mastodon_image_v1 .`
`sudo docker run --name mastodon_client mastodon_image_v1 --user <db_user_name> --password <db_password> --dbName <db_name> --ip <db_ip> --server <server_name> --token <token>`
