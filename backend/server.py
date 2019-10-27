import json
import sqlite3
from flask import Flask, Response
from flask import g
from datetime import datetime, timedelta
app = Flask(__name__)


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = sqlite3.connect('database.db',
                             detect_types=sqlite3.PARSE_DECLTYPES)
        db.row_factory = sqlite3.Row
        init_db(db)
        setattr(g, '_database', db)
    return db


def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))


def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


def update_db(query, args=()):
    db = get_db()
    try:
        db.execute(query, args)
        db.commit()
    except Exception as e:
        print("ERROR:", e)


def init_db(db):
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route("/api/uid/", methods=["GET"])
def seat_get_all():
    query = query_db('SELECT * FROM uid')
    result = []
    for row in query:
        re = {}
        re['uid'] = row['uid']
        result.append(re)
    return Response(json.dumps(result), mimetype="application/json")


@app.route("/api/uid/<int:uid_id>", methods=["GET"])
def uid_get(uid_id):
    query = query_db('SELECT * FROM uid WHERE id = ?', (uid_id,), True)
    result = {}
    if query is None:
        result['id'] = uid_id
        result['uid'] = ''
    else:
        result['uid'] = query['uid']
        result['time'] = query['time'].isoformat()
    return Response(json.dumps(result), mimetype="application/json")


@app.route("/api/uid/<int:uid_id>/<uid>")
def uid_update(uid_id, uid):
    """
    This function updates the status of the seat
    """
    result = query_db('SELECT * FROM uid WHERE id = ?', (uid_id,), True)
    if result is None:
        update_db('INSERT INTO uid(id, uid, time) VALUES (?, ?, ?)',
                  (uid_id, uid, datetime.now()))
    else:
        update_db('UPDATE uid SET uid = ?, time = ? WHERE id = ?',
                  (uid, datetime.now(), uid_id))
    return ""


def get_data(data):
    """
    This function deserializes an JSON object.

    :param data: JSON data
    :type data: str
    """
    json_data = json.loads(data)
    print("Deserialized data: {}".format(data))
    return json_data


def return_result(result):
    """
    This function simply returns an operation's status in JSON.

    :param result: boolean whether successful
    :type result: bool
    """
    ret = {}
    if result:
        ret["code"] = 0
        ret["message"] = "SUCCESS"
    else:
        ret["code"] = 1
        ret["message"] = "FAILURE"
    return json.dumps(ret)


if __name__ == "__main__":
    # enable if you also like to live dangerously
    # APP.run(debug=False, host="0.0.0.0")
    app.run(debug=True)
