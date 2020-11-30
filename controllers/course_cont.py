from flask import request
from models import course

"""Get all courses controller"""
def get_allcourse_cont():
    result = course.get_all_course()
    return result