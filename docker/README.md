1. To install and start Docker look at https://docs.docker.com/installation/ for instructions.
2. Clone repo, for example: git clone https://github.com/jskyworker/drobot, into separate folder.
3. Change dir to docker folder
4. Run next command to build an image: docker build -t mongo/test1 .
5. Run container from built image: docker run --name mongoX -p 8080:8080  -d -t mongo/test1
6. Use browser or cURL to see data: curl "http://127.0.0.1:8080/get?date=2015-05-12&uid=10"
7. Use cURL to POST data: curl -H "Content-Type: application/json" -X POST -d '[{"uid": "11", "name": "22xyz", "date": "2015-05-12T14:36:00.451765", "md5checksum": "91d79228a2570e66122de519291589df"}]' http://localhost:8080/post/
