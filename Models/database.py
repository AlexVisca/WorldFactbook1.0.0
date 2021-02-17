import mysql.connector
from mysql.connector import errorcode

class Database:

    @staticmethod
    def get_db_connection(**kwargs):
        """ Establishes connection with the database

        Returns:
            object: MySQL connection
        """
        try:
            connection = mysql.connector.connect(**kwargs)
            print("Connection established")
            # print version
            cursor = connection.cursor()
            cursor.execute("SHOW VARIABLES like 'version'")
            result = cursor.fetchall()
            for row in result:
                print(row)
            
            return connection

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("User and/or password is incorrect")
                exit("Connection terminated")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            connection.close()

