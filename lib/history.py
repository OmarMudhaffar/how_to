import sqlite3
from datetime import datetime

DB_PATH = "history.db"


def connect(path=DB_PATH):
    """Open the database and make the table if it does not exist."""
    conn = sqlite3.connect(path)
    conn.execute(
        "CREATE TABLE IF NOT EXISTS history "
        "(id INTEGER PRIMARY KEY AUTOINCREMENT, question TEXT, time TEXT)"
    )
    return conn


def save_question(question, path=DB_PATH):
    """Save a question the user asked in the database."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    conn = connect(path)
    conn.execute("INSERT INTO history (question, time) VALUES (?, ?)", (question, now))
    conn.commit()
    conn.close()


def get_history(limit=10, path=DB_PATH):
    """Return the last questions as a list of tuples (question, time)."""
    conn = connect(path)
    rows = conn.execute(
        "SELECT question, time FROM history ORDER BY id DESC LIMIT ?", (limit,)
    ).fetchall()
    conn.close()
    return rows


def clear_history(path=DB_PATH):
    """Delete all saved questions."""
    conn = connect(path)
    conn.execute("DELETE FROM history")
    conn.commit()
    conn.close()
