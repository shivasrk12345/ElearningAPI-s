
from utils import conn

"""Get course assignment model"""

def get_course_assignment(coursename):
    # Creating Db connection and cursor
    db_connection = conn.create_connection()
    db_cursor = db_connection.cursor()
    db_cursor.execute('select assesment.assesmentid, assesment.assesment_name, assesment.assesment_score, course.coursename from assesment inner join course on course.courseid = assesment.course_id where course.coursename=%s',(coursename,))
    # Fetch all record and return result
    result = db_cursor.fetchall()
    # Close Db connection and cursor
    db_cursor.close()
    db_connection.close()

    return result