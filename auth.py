import sqlite3

DB = "database.db"


def get_conn():
    return sqlite3.connect(DB)


def signup_user(username, password):

    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users(
            username TEXT PRIMARY KEY,
            password TEXT
        )
    """)

    try:
        cur.execute(
            "INSERT INTO users(username,password) VALUES(?,?)",
            (username, password)
        )
        conn.commit()
        return {"success": True}
    except:
        return {"success": False, "message": "User already exists"}


def login_user(username, password):

    conn = get_conn()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )

    user = cur.fetchone()

    if user:
        return {"success": True}
    else:
        return {"success": False, "message": "Invalid credentials"}
