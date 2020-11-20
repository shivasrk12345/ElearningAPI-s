from configparser import ConfigParser
from flask import Flask, request
from werkzeug import serving
from controllers import register,auth,points_cont,tedencies_cont,course_cont,post_cont,course_progress_cont,course_assignment_cont
from configparser import ConfigParser
from flask import Flask, render_template, Response, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'elearning!@#$321'

config = ConfigParser()
config.read("config.ini")
port = config.get('app', 'port')

@app.route('/login',methods=['GET','POST'])
def login():
    response = auth.login_api()
    return response

@app.route('/logout',methods=['GET'])
def logout():
    response = auth.logout_api()
    return response

@app.route('/register',methods=['GET','POST'])
def adduser():
        response = register.register_form()
        return response

@app.route('/points',methods=['GET','POST'])
def points():
        response = points_cont.get_points_cont()
        return response

@app.route('/tedencies',methods=['GET','POST'])
def tedencies():
        response = tedencies_cont.get_tendencies_cont()
        return response

@app.route('/courses',methods=['GET'])
def courses():
        response = course_cont.get_allcourse_cont()
        return response

@app.route('/courseprogress',methods=['GET','POST'])
def courseprogress():
        response = course_progress_cont.get_course_progress()
        return response

@app.route('/courseassignment',methods=['GET','POST'])
def courseassignment():
        response = course_assignment_cont.get_course_assignment()
        return response

@app.route('/addpost',methods=['GET','POST'])
def addpost():
        response = post_cont.add_post()
        return response

@app.route('/addcomment',methods=['GET','POST'])
def addcomment():
        response = post_cont.add_comment()
        return response

@app.route('/getpost',methods=['GET','POST'])
def getpost():
        response = post_cont.get_post()
        return response

@app.route('/getcomments',methods=['GET','POST'])
def getcomments():
        response = post_cont.get_comments()
        return response

@app.route('/addlikes',methods=['GET','POST'])
def addlikes():
        response = post_cont.add_like()
        return response

@app.route('/getlikes',methods=['GET','POST'])
def getlikes():
        response = post_cont.get_alllikes()
        return response


if __name__ == '__main__':
    app.run(host="127.0.0.1",port=port,debug=True,use_reloader=False)
