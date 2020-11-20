from flask import session

from utils import conn


def login(username, password):
    db_connection = conn.create_connection()
    db_cursor = db_connection.cursor()
    #db_cursor.execute('SELECT * FROM users WHERE userid = %s AND password = %s', (username, password))
    db_cursor.execute('SELECT users.userid, users.name, users.email,users.contact,users.address, tribe.tribename, mentor.mentorname FROM users INNER JOIN tribe ON users.tribe_id=tribe.tribeid INNER JOIN mentor ON users.mentor_id = mentor.mentorid where users.userid = %s and users.password = %s', (username, password))
    #db_cursor.execute('SELECT users.userid, users.name, users.email,users.contact,users.address, tribe.tribename, mentor.mentorname FROM users INNER JOIN tribe ON users.tribe_id=tribe.tribeid INNER JOIN mentor ON users.mentor_id = mentor.mentorid where users.userid='shiva123' and users.password='1234')
    # Fetch one record and return result
    account = db_cursor.fetchone()
    # If account exists in accounts table in out database
    if account:
        # Create session data, we can access this data in other routes
        session['loggedin'] = True
        session['userid'] = account[0]
        session['name'] = account[1]
        # Redirect to home page
        db_cursor.close()
        db_connection.close()
        print(account)
        response = {"userid":account[0],"name":account[1],"email":account[2],"contact":account[3],"address":account[4],"tribename":account[5],"mentorname":account[6]}
    else:
        # Account doesnt exist or username/password incorrect
        response = 'Incorrect username/password!'

    return response

