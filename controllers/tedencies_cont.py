from flask import request
from models import tedencies

def get_tendencies_cont():
    if request.method == 'POST':
        username = request.json['username']
        result = tedencies.get_tedencies(username)
    return result