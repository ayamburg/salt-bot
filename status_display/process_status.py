from db_connection import *

def setup():
    connection = create_connection(r"bot_status.db")
    create_tables(connection)
    
def main():
    setup()
