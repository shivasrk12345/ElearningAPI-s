from flask import request, session
from models import auth

def login_api():
    if request.method == 'POST' and 'userid' in request.form and 'password' in request.form:
        # Create variables for easy access
     username = request.form['userid']
     password = request.form['password']
     response = auth.login(username, password)
    else:
     response= "All details Required"
    return response

def logout_api():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)

    return "Log out successfull"
