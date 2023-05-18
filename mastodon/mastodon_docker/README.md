`sudo docker build -t mastodon_image_v1 .`
- Edit env.list
`sudo docker run --env-file env.list --name mastodon_client mastodon_image_v1 `
