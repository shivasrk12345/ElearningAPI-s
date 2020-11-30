from flask import request, jsonify
from models import course_assignment

"""Get course assignment controller"""

def get_course_assignment():
    if request.method == 'POST':
        coursename = request.json['coursename']
        result = course_assignment.get_course_assignment(coursename)
        if (result):
            payload = []
            content = {}
            for data in result:
                content = {'assignment id': data[0], 'assignment name':data[1], 'assignment score':data[2]}
                payload.append(content)
                content = {}
            result_json = jsonify(payload)
        else:
            result_json = "user don't have assignment"

        print(result_json)


    return result_json