#!/bin/bash

/usr/bin/mongod --smallfiles && python2 /flask/start.py &
