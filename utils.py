import pymysql

def connect(username, password, database):
    connection = pymysql.connect(
        host='localhost',
        user=username, 
        password = password,
        db=database,
        )
      
    cursor = connection.cursor()
    return cursor

def query(cursor):      
    cursor.execute("SELECT * FROM world_population")
    output = cursor.fetchall()
    return output