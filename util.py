from datetime import datetime
from flask import session
import connection
from psycopg2 import sql

import password_handler


@connection.connection_handler
def check_username(cursor, username):
    query = '''
    SELECT username
    FROM users
    WHERE username = %s
    '''
    cursor.execute(query, (username, ))
    if(cursor.rowcount == 0):
        return True
    else:
        return False


@connection.connection_handler
def user_registration(cursor, username, fist_name, last_name, hashed_password):
    query = '''
    INSERT INTO users(username, is_admin, first_name, last_name, password)
    VALUES(%s , FALSE , %s, %s, %s)'''
    cursor.execute(query, (username, fist_name, last_name, hashed_password))


@connection.connection_handler
def user_login(cursor, username):
    query = '''
    SELECT password
    FROM users 
    WHERE username = %s'''
    cursor.execute(query, (username, ))
    return cursor.fetchall()[0]['password']

