from utils import conn

def get_points(username):
    db_connection = conn.create_connection()
    db_cursor = db_connection.cursor()
    db_cursor.execute('SELECT * FROM points WHERE userid = %s',(username,))
    # Fetch one record and return result
    result = db_cursor.fetchone()
    db_cursor.close()
    db_connection.close()

    if (result):
        result_json= {"wisdompoints":result[1],"connectionpoints":result[2]}
    else:
        result_json = "User don't have points"

    return result_json