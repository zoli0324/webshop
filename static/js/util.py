
from datetime import datetime
from flask import session
import connection
from psycopg2 import sql

# UNIVERSAL FUNCTIONS #
import password_handler


@connection.connection_handler
def get_id_for_username(cursor, username):
    quer y= '''
    SELECT user_id 
    FROM user_admin 
    WHERE username = %s
    '''
    cursor.execute(query, (username, ))
    return cursor.fetchone()['user_id']