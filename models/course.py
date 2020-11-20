from flask import jsonify

from utils import conn

def get_all_course():
    db_connection = conn.create_connection()
    db_cursor = db_connection.cursor()
    db_cursor.execute('SELECT * FROM course')
    # Fetch one record and return result
    rv = db_cursor.fetchall()
    db_cursor.close()
    db_connection.close()

    if (rv):
        payload = []
        content = {}
        for result in rv:
            content = {'courseid': result[0], 'coursename': result[1]}
            payload.append(content)
            content = {}
        result_json =  jsonify(payload)
    else:
        result_json = "don't have any course"

    return result_json