from flask import request
from datetime import datetime
from models import post

def add_post():
    if request.method == 'POST' and 'userid' in request.json and 'text' in request.json:
        userid = request.json['userid']
        text = request.json['text']
        timestamp = datetime.now()
        response = post.add_post(userid,text,timestamp)
    else:
        response = "pass all required parameters"
    return response

def get_post():
    if request.method == 'POST' and 'userid' in request.json:
        userid = request.json['userid']
        response = post.get_post(userid)
    else:
        response = "pass all required parameters"
    return response

def get_comments():
    if request.method == 'POST' and 'postid' in request.json:
        postid = request.json['postid']
        response = post.get_commnets(postid)
    else:
        response = "pass all required parameters"
    return response


def add_comment():
    if request.method == 'POST' and 'postid' in request.json and 'commenttext' in request.json:
        postid = request.json['postid']
        commenttext = request.json['commenttext']
        timestamp = datetime.now()
        response = post.add_comment(postid,commenttext,timestamp)
    else:
        response = "pass all required parameters"
    return response

def add_like():
    if request.method == 'POST' and 'postid' in request.json and 'userid' in request.json:
        postid = request.json['postid']
        userid = request.json['userid']
        timestamp = datetime.now()
        response = post.add_like(postid,userid,timestamp)
    else:
        response = "pass all required parameters"
    return response

def get_alllikes():
    if request.method == 'POST' and 'postid' in request.json:
        postid = request.json['postid']
        response = post.get_alllikes(postid)
    else:
        response = "pass all required parameters"
    return response