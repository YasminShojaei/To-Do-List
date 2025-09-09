import sqlite3

def create_database():
    connection = sqlite3.connect("to_do_list_db.sqlite")
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS TASKS (
        id_         INTEGER PRIMARY KEY AUTOINCREMENT,
        title       text NOT NULL,
        start_time  text NOT NULL,
        description text NOT NULL,
        priority    text NOT NULL
    )
    """)

    connection.commit()
    cursor.close()
    connection.close()