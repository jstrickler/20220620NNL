#!/usr/bin/env python
from threading import Thread
import sqlite3

def do_query(connection, query):
    cursor = connection.cursor()  # <2>

    # select first name, last name from all presidents
    cursor.execute('''
        select firstname, lastname
        from presidents
    ''')  # <3>

    return cursor

def timer(timeout=30):
    pass

query_thread = Thread(target=do_query, args=(conn, "select * from presidents"))
