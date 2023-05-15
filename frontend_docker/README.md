## Build the image and start the container
- `docker build -t vuejs-cookbook/dockerize-vuejs-app .`
- `sudo docker run -it -p 8080:80 --rm --name dockerize-vuejs-app-1 vuejs-cookbook/dockerize-vuejs-app`
