from flask import request
from models import points

"""Get points of a learner controller"""

def get_points_cont():
    if request.method == 'POST':
        username = request.json['username']
        result = points.get_points(username)
    return result