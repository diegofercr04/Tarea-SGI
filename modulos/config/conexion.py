import mysql.connector
from mysql.connector import Error

def get_connection():
    try:
        conn = mysql.connector.connect(
            host="bvldgyuqlhorc5b9e0bt-mysql.services.clever-cloud.com",
            port=3306,
            user="uwffu4vlmfh0rzy4",
            password="iGuMZsgMRdx9tqVeUyuD",
            database="bvldgyuqlhorc5b9e0bt"
        )
        return conn
    except Error as e:
        return None
