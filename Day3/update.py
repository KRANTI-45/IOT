# import mysql connector
import mysql.connector

# function to create a connection
def get_connection():
    return mysql.connector.connect(
        host = "localhost",
        port = 3306,
        user = "sunbeam",
        password = "sunbeam",
        database = "iotdb"
    )

def update_employee(uid, date_of_joining):
    # get connection
    conn = get_connection()

    # form a query
    query = f"update employee SET date_of_joining = %s where uid = %s;"
    val = (date_of_joining, uid)

    # create a cursor
    cursor = conn.cursor()

    # execute the query
    cursor.execute(query, val)

    # commit the changes
    conn.commit()

    # close cursor as well as connection
    cursor.close()
    conn.close()



update_employee (24, "23-4-2024")













