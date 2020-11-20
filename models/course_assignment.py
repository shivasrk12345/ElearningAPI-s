
from utils import conn

def get_course_assignment(coursename):
    db_connection = conn.create_connection()
    db_cursor = db_connection.cursor()
    db_cursor.execute('select assesment.assesmentid, assesment.assesment_name, assesment.assesment_score, course.coursename from assesment inner join course on course.courseid = assesment.course_id where course.coursename=%s',(coursename,))
    # Fetch one record and return result
    result = db_cursor.fetchall()
    db_cursor.close()
    db_connection.close()

    return result