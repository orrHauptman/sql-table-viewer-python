import mysql.connector
from mysql.connector import MySQLConnection , InterfaceError , Error , ProgrammingError

def connect_to_sql() -> MySQLConnection:
    while True:

        try:

            connect_host : str = input("Enter the hostname of the database server: ")
            connect_user : str = input("Enter the username of the database server: ")
            connect_password : str = input("Enter the password of the database server: ")
            connect_database : str = input("Enter the name of the database to connect to in the server: ")
            


            conn : MySQLConnection = mysql.connector.connect(
                host = connect_host,
                user = connect_user,
                password = connect_password,
                database = connect_database
            ) # type: ignore

            return conn

        except InterfaceError as e:
            print(f"Host wasn't correct : {e} \n Try again")

        except ProgrammingError as e:
            print(f"User/password/database wasn't correct: {e} \n Try again")

        except Error as e:
            print(f"Other MySQL error: {e} \nTry again")


def show_table() -> None:

    conn = connect_to_sql()
    curser = conn.cursor()

    while True:
        try:
            connect_table: str = input("Enter the table to connect to: ")

            if connect_table.lower() == "stop":
                print("Stopping program")
                break

            curser.execute(f"SELECT * FROM {connect_table}")

            result = curser.fetchall() 

            for i , line in enumerate(result, 1):
                print(f"Line number {i} : {line}")

        except ProgrammingError as e:
            print(f"Table not found or SQL error: {e}\nTry again")

        except Error as e:
            print(f"Other MySQL error: {e}\nTry again")

if __name__ == "__main__":
    show_table()