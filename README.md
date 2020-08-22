# Python API: Using Flask and MySQL (Create, read, update and delete)

## Introduction ##

Python REST API using Flask and MySQL. You can find how to create a web application CRUD example using Python, Flak and MySQL in this repository.

What is REST or RESTful?

A RESTful API is an application program interface (API) that uses HTTP requests to GET, PUT, POST and DELETE data. An API for a website is code that allows two software programs to communicate with each other.

    The base URL for the Web service such as http://<host>/<appcontext/contextpath>/<url pattern>/<resources>.
    The set of operations supported by the service. (for example, POST, GET, PUT or DELETE).

REST or RESTful Methods

HTTP methods are mapped to CRUD (create, read, update and delete) actions for a resource. Although you can make slight modifications such as making the PUT method to be create or update, the basic patterns are listed as follows.

>    GET: Get/List/Retrieve an individual resource or a collection of resources.

>    POST: Create a new resource or resources.

>    PUT: Update an existing resource or collection of resources.

>    DELETE: Delete a resource or collection of resources.

## Prerequisites ##

    Docker and Docker Compose installed machine
    Here have used python 3.8.5-buster docker image
    Curl or any tool for send CRUD requqests (like Postman)

## Preparing your workspace ##

Preparing your workspace is one of the first things that you can do to make sure that you start off well. The first step is to check your working directory.

Docker-compose.yml file contains 2 services: db and flask. 

> db service: There will be a docker container for mysql version 5.7 that contains mysql database named 'students' and mysql user apiuser1. The database name, users and password is configurable. Please find details in docker-compose.yml file

> flask service: There will be another docker container which is based on python:3.8.5-buster image. This container will run the API which deployed using flask. You can find details in flask folder. 

For this Python REST API CRUD Example using Flask and MySQL, we need modules, such as, flask and mysql. The module flask works as a web framework and mysql module is required to establish connection with MySQL database and query the database using Python programming language.

## Example and Source Code ##

You can simply clone the repository from github and start to deploy containers. Since the repository comes with MIT license permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files.

Step 1: Deploy docker containers via docker compose.

```

$:~/API/python-flask-api# ls
LICENSE  README.md  docker-compose.yml  flask  students.sql

$:~/API/python-flask-api# docker-compose build

db uses an image, skipping
Building flask
Step 1/6 : FROM python:3.8.5-buster
Step 2/6 : WORKDIR /app
Step 3/6 : ADD . /app
Step 4/6 : RUN pip install -r requirements.txt
Step 5/6 : ENTRYPOINT ["python3"]
Step 6/6 : CMD ["main.py"]
Successfully built 2cad588ade2f
Successfully tagged python-flask-api_flask:latest

```

Step 2: run ``` docker-compose up -d``` to build, (re)create, start, and attach to containers for a service.


``` 
$:~/API/python-flask-api# docker-compose up -d
Creating volume "python-flask-api_my-db" with default driver
Pulling db (mysql:5.7)...
5.7: Pulling from library/mysql
bf5952930446: Pull complete
8254623a9871: Pull complete
938e3e06dac4: Pull complete
ea28ebf28884: Pull complete
f3cef38785c2: Pull complete
894f9792565a: Pull complete
1d8a57523420: Pull complete
5f09bf1d31c1: Pull complete
1b6ff254abe7: Pull complete
74310a0bf42d: Pull complete
d398726627fd: Pull complete
Digest: sha256:da58f943b94721d46e87d5de208dc07302a8b13e638cd1d24285d222376d6d84
Status: Downloaded newer image for mysql:5.7
Creating python-flask-api_db_1 ... done
Creating flask-api             ... done

```

Step 3: run ```docker ps``` command to check currently running container:

```
$:~/API/python-flask-api# docker ps
CONTAINER ID        IMAGE                    COMMAND                  CREATED              STATUS              PORTS               NAMES
ba7f9a1f9cf3        mysql:5.7                "docker-entrypoint.s…"   About a minute ago   Up About a minute                       python-flask-api_db_1
a67f132a8928        python-flask-api_flask   "python3 main.py"        About a minute ago   Up About a minute                       flask-api
```

Step 4: run students.sql in order to create students table:

```
$:~/API/python-flask-api# docker exec -i python-flask-api_db_1 mysql -uapiuser1 -ppassword < students.sql
```

Step 5: You can use curl command, Postman, REST Client etc. to test your REST or RESTful APIs. Here I used ```curl``` command.  

Display all users:

```
$~/API/python-flask-api# curl http://localhost:5000/users
[]
```

Step 6: Let's add a new user and try to display all users again

```
$:~# curl -i -X POST -H "Content-Type: application/json" -d  '{"name":"Fagani Hajizada", "email":"fagani@example.com", "university":"University001"}'  http://localhost:5000/add

HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 27
Access-Control-Allow-Origin: *
Server: Werkzeug/1.0.1 Python/3.8.5
Date: Sat, 22 Aug 2020 17:24:27 GMT

"User added successfully!"
```
Display all users:

```
$:~# curl http://localhost:5000/users

[{"email":"fagani@example.com","id":1,"name":"Fagani Hajizada","university":"University001"}]
```

Step 7: Let's update the existing user with PUT request

```
$~# curl -i -X PUT -H "Content-Type: application/json" -d  '{"id":"1","name":"Fagani Hajizada", "email":"fagani@example.com", "university":"University002"}'  http://localhost:5000/update

HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 29
Access-Control-Allow-Origin: *
Server: Werkzeug/1.0.1 Python/3.8.5
Date: Sat, 22 Aug 2020 17:31:26 GMT

"User updated successfully!"
```
Let's check the user's university:

```
$:~# curl http://localhost:5000/users

[{"email":"fagani@example.com","id":1,"name":"Fagani Hajizada","university":"University002"}]
```

Step 8: Add a new user via POST method and try to display single user with GET method

```
$:~# curl -i -X POST -H "Content-Type: application/json" -d  '{"name":"John Doe", "email":"john.doe@example.com", "university":"University003"}'  http://localhost:5000/add
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 27
Access-Control-Allow-Origin: *
Server: Werkzeug/1.0.1 Python/3.8.5
Date: Sat, 22 Aug 2020 17:36:23 GMT

"User added successfully!"

```

```
$:~# curl http://localhost:5000/users

[{"email":"fagani@example.com","id":1,"name":"Fagani Hajizada","university":"University002"},
{"email":"john.doe@example.com","id":2,"name":"John Doe","university":"University003"}]
```

It's also possible to display single user within ID

```
$:~# curl http://localhost:5000/user/1

{"email":"fagani@example.com","id":1,"name":"Fagani Hajizada","university":"University002"}

```

Step 9: delete a user with DELETE method:

```
$:~# curl -i -X DELETE http://localhost:5000/delete/2
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 29
Access-Control-Allow-Origin: *
Server: Werkzeug/1.0.1 Python/3.8.5
Date: Sat, 22 Aug 2020 17:44:08 GMT

"User deleted successfully!"
```

User with id:2 deleted successfully:

```
$:~# curl http://localhost:5000/users

[{"email":"fagani@example.com","id":1,"name":"Fagani Hajizada","university":"University002"}]
```
