from flask import request


from models import register

def register_form():
    if request.method == 'POST' and 'userid' in request.form and 'password' in request.form:
        userid = request.form['userid']
        password = request.form['password']
        name = request.form['name']
        email = request.form['email']
        address = request.form['address']
        tribe_id = request.form['tribe_id']
        mentor_id = request.form['mentor_id']
        response = register.register(userid,password,name,email,address,tribe_id,mentor_id)
    else:
        response = "pass all required parameters"
    return response

