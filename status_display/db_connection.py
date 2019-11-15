import sqlite3
from sqlite3 import Error
 
 
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn        
 
def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def mark_processed(conn, task):
    sql = ''' UPDATE events
              SET processed = ? ,
              WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()

def select_server_by_id(conn, priority):
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE id=?", (priority,))
 
    rows = cur.fetchall()
 
    return rows[0]

def create_tables(connection):
    sql_create_servers_table = """ CREATE TABLE IF NOT EXISTS servers (
                                        id text PRIMARY KEY,
                                        voice_users integer,
                                    ); """
                                    
    sql_create_events_table = """ CREATE TABLE IF NOT EXISTS events (
                                    id integer PRIMARY KEY,
                                    type text NOT NULL,
                                    timestamp text NOT NULL,
                                    quantity integer,
                                    FOREIGN KEY (server_id) REFERENCES servers (id),
                                    processed boolean,
                                ); """

    create_table(connection, sql_create_servers_table)
    create_table(connection, sql_create_events_table)