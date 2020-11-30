from utils import conn

"""Get Progress of each course for a user model"""

def get_course_progress(username):
    # Creating Db connection and cursor
    db_connection = conn.create_connection()
    db_cursor = db_connection.cursor()
    db_cursor.execute('SELECT COUNT(assesmentid), course.coursename FROM user_course_assesment INNER JOIN course ON user_course_assesment.courseid=course.courseid where userid = %s and assesment_state = %s GROUP BY user_course_assesment.userid,user_course_assesment.courseid',(username,'finished'))
    # Fetch all record and return result
    result = db_cursor.fetchall()
    # Close Db connection and cursor
    db_cursor.close()
    db_connection.close()

    return result