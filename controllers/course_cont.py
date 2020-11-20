from flask import request
from models import course

def get_allcourse_cont():
    result = course.get_all_course()
    return result