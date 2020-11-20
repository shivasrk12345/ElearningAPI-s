
from utils import conn

def get_course_progress(username):
    db_connection = conn.create_connection()
    db_cursor = db_connection.cursor()
    db_cursor.execute('SELECT COUNT(assesmentid), course.coursename FROM user_course_assesment INNER JOIN course ON user_course_assesment.courseid=course.courseid where userid = %s and assesment_state = %s GROUP BY user_course_assesment.userid,user_course_assesment.courseid',(username,'finished'))
    # Fetch one record and return result
    result = db_cursor.fetchall()
    db_cursor.close()
    db_connection.close()

    return result