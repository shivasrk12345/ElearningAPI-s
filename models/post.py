from flask import jsonify

from utils import conn

def add_post(userid,text,timestamp):
    db_connection = conn.create_connection()
    db_cursor = db_connection.cursor()
    sql = 'INSERT INTO post (userid,text,imageurl,timestamp) VALUES(%s,%s,%s,%s)'
    val = (userid,text,'',timestamp)
    db_cursor.execute(sql, val)
    db_connection.commit()

    return "Post Added"

def get_post(userid):
    db_connection = conn.create_connection()
    db_cursor = db_connection.cursor()
    #sql = 'select * from post where userid=%s', (userid,);
    db_cursor.execute('select * from post where userid = %s', (userid,));
    rv = db_cursor.fetchall()
    db_cursor.close()
    db_connection.close()

    if (rv):
        payload = []
        content = {}
        for result in rv:
            content = {'postid': result[0], 'posttext': result[2],'imageurl':result[3],'timestamp':result[4]}
            payload.append(content)
            content = {}
        result_json =  jsonify(payload)
    else:
        result_json = "don't have post yet"

    return result_json


def get_post_tribe(userid):
    db_connection = conn.create_connection()
    db_cursor = db_connection.cursor()
    #sql = 'select * from post where userid=%s', (userid,);
    db_cursor.execute('select * from post where userid in (select userid from users where tribe_id in (select tribe_id from users where userid= %s))', (userid,));
    rv = db_cursor.fetchall()
    db_cursor.close()
    db_connection.close()

    if (rv):
        payload = []
        content = {}
        for result in rv:
            content = {'postid': result[0], 'posttext': result[2],'imageurl':result[3],'timestamp':result[4]}
            payload.append(content)
            content = {}
        result_json =  jsonify(payload)
    else:
        result_json = "don't have post yet"

    return result_json


def add_comment(postid,commenttext,timestamp):
    db_connection = conn.create_connection()
    db_cursor = db_connection.cursor()
    sql = 'INSERT INTO comment (commenttext, timestamp, postid) VALUES(%s,%s,%s)'
    val = (commenttext,timestamp, postid)
    db_cursor.execute(sql, val)
    db_connection.commit()

    return "Comment Added"

def add_like(postid,userid,timestamp):
    db_connection = conn.create_connection()
    db_cursor = db_connection.cursor()
    db_cursor.execute('select * from likes where userid = %s and postid= %s',(userid,postid));
    result = db_cursor.fetchone()
    print(result)
    # status 0 means likes, 1 means disliked
    if(result):
        if(result[3]==0):
            db_cursor.execute('update likes set active_likes = %s where userid = %s and postid= %s', (1,userid, postid));
            db_connection.commit()
        else:
            db_cursor.execute('update likes set active_likes = %s where userid = %s and postid= %s',(0, userid, postid));
            db_connection.commit()
        msg = 'like updated'
    else:
        sql = 'INSERT INTO likes (postid, userid,active_likes) VALUES(%s,%s,%s)'
        val = (postid, userid,0)
        db_cursor.execute(sql, val)
        db_connection.commit()
        msg = 'like added'

    return msg

def get_commnets(postid):
    db_connection = conn.create_connection()
    db_cursor = db_connection.cursor()
    #sql = 'select * from post where userid=%s', (userid,);
    db_cursor.execute('select * from comment where postid = %s',(postid,));
    rv = db_cursor.fetchall()
    db_cursor.close()
    db_connection.close()
    if (rv):
        payload = []
        content = {}
        for result in rv:
            content = {'commentid': result[0], 'commenttext': result[1],'timestamp':result[2]}
            payload.append(content)
            content = {}
        result_json =  jsonify(payload)
    else:
        result_json = "no comment on this post"

    return result_json

def get_alllikes(postid):
    db_connection = conn.create_connection()
    db_cursor = db_connection.cursor()
    #sql = 'select * from post where userid=%s', (userid,);
    db_cursor.execute('select count(likeid) from likes where postid=%s and active_likes=%s group by(postid);', (postid,0));
    result = db_cursor.fetchone()
    if(result):
        all_likes = {'alllikes': result[0]}
    else:
        all_likes='post have 0 likes'
    db_cursor.close()
    db_connection.close()
    print(all_likes)

    return all_likes