from flask import Flask
from flask import request
from flask import render_template
import json
import hashlib
from string import Template
from datetime import datetime
from pymongo import MongoClient

app = Flask(__name__)


@app.route('/get', methods=['GET'])
def get():
    uid = request.args.get('uid')
    date = request.args.get('date')
    if not uid or not date:
        return "No parameters were provided."
    try:
        datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Incorrect date format, should be YYYY-MM-DD")
    num = get_mongo(uid, date)
    if num < 0:
        return "Data is not found, database error?"
    else:
        return render_template("test.html", uid=uid, date=date, num=num)


@app.route('/post/', methods=['POST'])
def post():
    data = json.loads(request.data)
    s = Template('{"date": "$date", "uid": "$uid", "name": "$name"}')
    for i in data:
        h = hashlib.md5(s.substitute(name=i['name'], date=i['date'],
                                     uid=i['uid']).encode('utf-8'))
        if h.hexdigest() != i['md5checksum']:
            return "Provided checksum {0}, should be {1} for name {2}.".\
                format(i['md5checksum'], h.hexdigest(), i['name'])
        else:
            if not store_mongo(i):
                return "Checksum was correct but data was not saved."
            return "Correct checksum {0} for name {1}".format(h.hexdigest(),
                                                              i['name'])


def get_num(uid, date):
    """
    Given a uid and a date the endpoint should return the number of occurrences
    of a given UID (John Doe) for that day.
    :param uid:
    :param date:
    :return:
    """
    date_c = datetime.strptime(date, '%Y-%m-%d').date()
    count = 0
    with open('data.json', 'r') as f:
        data = json.load(f)
    for i in data:
        if date_c == datetime.strptime(i['date'], '%Y-%m-%dT%H:%M:%S.%f').date() \
                and uid == i['uid']:
            print("uid {0}, date {1}".format(uid, date))
            count += 1
    return count


def get_mongo(uid, date):
    """
    Given a uid and a date the endpoint should return the number of occurrences
    of a given UID (John Doe) for that day.
    :param uid:
    :param date:
    :return:
    """
    date_c = datetime.strptime(date, '%Y-%m-%d').date()
    count = 0
    db = get_mongo_db()
    if not db:
        return -1
    cursor = db.posts.find({"uid": uid})
    for i in cursor:
        if date_c == datetime.strptime(i['date'], '%Y-%m-%dT%H:%M:%S.%f').date():
            print("uid {0}, date {1}".format(uid, date))
            count += 1
    return count


def store_mongo(data):
    """
    Store object in Mongo
    :param data:
    :return:
        False in case of exception
    """
    db = get_mongo_db()
    if not db:
        return False
    db.posts.insert(data)
    return True


def get_mongo_db(host='localhost', port=27017):
    """
    Function to get Mongo db object.
    :param host: Host we need to connect to.
    :param port: Port number
    :return: db object or False
    """
    try:
        client = MongoClient(host, port)
        db = client.test
        return db
    except Exception as e:
        print(str(e))
        return False
