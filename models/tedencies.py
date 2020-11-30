from utils import conn

"""Get Learner tendencies model"""

def get_tedencies(username):
    # Creating Db connection and cursor
    db_connection = conn.create_connection()
    db_cursor = db_connection.cursor()
    db_cursor.execute('SELECT * FROM tendencies WHERE userid = %s',(username,))
    # Fetch one record and return result
    result = db_cursor.fetchone()
    # Close Db connection and cursor
    db_cursor.close()
    db_connection.close()
    if(result):
        result_json = {"tendencie1":result[1],"tendencie2":result[2],"tendencie3":result[3]}
    else:
        result_json = "User don't have tendencies"

    return result_json