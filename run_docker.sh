docker rm -f mycontainer
docker build -t myimage .
docker run -d --name mycontainer -p 80:80 -e TIMEOUT="300" myimage