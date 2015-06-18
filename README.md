Create a repository on GitHub or Bitbucket with the following:
 
* A Vagrantfile for managing a virtual machine with a Linux-based operating system of your choice. 
Please, use a publicly available box, for example one of the boxes hosted here: https://atlas.hashicorp.com/boxes/search.
* A small Flask application (details explained down below)
* An Ansible playbook (with any associated roles or files), that can install the above flask application and mongodb on the above virtual machine.

Details about the Flask application:

* Write a small Flask web application that will listen on port 8080.
* The Flask application should have only 2 endpoints.
* The first endpoint should accept only POST requests which will have a json payload.

The JSON payload will be:

   [{'uid': '1'
   'name': 'John Doe',
   'date': '2015-05-12T14:36:00.451765',
   'md5checksum': 'e8c83e232b64ce94fdd0e4539ad0d44f'},
   
   {'uid': '2'
   'name': 'Jane Doe',
   'date': '2015-05-13T14:36:00.451765',
   'md5checksum': 'b419795d50db2a35e94c8364978d898f'},
   ...]

The endpoint should store the data in a mongo data store.
Before storing the data we need to make sure that the checksum for each
JSON object (just fields: uid, name and date) is correct and matches the original checksum in
the JSON payload.

The second Endpoint should only accept GET requests with an uid parameter
and a date parameter. Given a uid and a date the endpoint should return the
number of occurrences of a given UID (John Doe) for that day.
 
Write tests for the application.

There will be a simple README file in docker and vagrant folders that will help to run the above. 