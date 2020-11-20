from utils import conn

def register(userid,password,name,email,address,tribe_id,mentor_id):
    print("into models db")
    db_connection = conn.create_connection()
    db_cursor = db_connection.cursor()
    sql = 'INSERT INTO users (userid,password,name,email,address,tribe_id,mentor_id) VALUES(%s,%s,%s,%s,%s,%s,%s)'
    val = (userid,password,name,email,address,tribe_id,mentor_id)
    db_cursor.execute(sql, val)
    db_connection.commit()

    return "Registration Successful"

