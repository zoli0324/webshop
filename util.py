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
    if cursor.rowcount == 0:
        return True
    else:
        return False


@connection.connection_handler
def is_admin(cursor, username):
    query = '''
    SELECT is_admin 
    FROM users 
    WHERE username = %s
    '''
    cursor.execute(query, (username,))
    return cursor.fetchone()["is_admin"]


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


@connection.connection_handler
def change_password(cursor, username, new_password):
    query = '''
    UPDATE users
    SET password = %s
    WHERE username = %s
    '''
    cursor.execute(query, (new_password, username))


@connection.connection_handler
def add_product(cursor, category, product_name, description, price, in_stock):
    query = '''
    INSERT INTO products(CATEGORY, PRODUCT_NAME, DESCRIPTION, PRICE, IN_STOCK)
    VALUES(%s, %s, %s, %s, %s)
    '''
    cursor.execute(query, (category, product_name, description, price, in_stock))
