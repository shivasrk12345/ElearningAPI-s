from flask import request, jsonify
from models import course_progress

def get_course_progress():
    if request.method == 'POST':
        username = request.json['username']
        result = course_progress.get_course_progress(username)
        if (result):
            payload = []
            content = {}
            for data in result:
                progress = (data[0]/10)*100
                content = {'course name': data[1], 'progress': progress}
                payload.append(content)
                content = {}
            result_json = jsonify(payload)
        else:
            result_json = "user progress is 0%"

        print(result_json)


    return result_json