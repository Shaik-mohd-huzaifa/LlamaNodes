import os
import pymysql.cursors
from dotenv import load_dotenv

# from .icu_information import icu_schema

load_dotenv()

ENDPOINT = os.getenv("AWS_RDS_ENDPOINT")
USER = os.getenv("AWS_RDS_USER")
PASSWORD = os.getenv("AWS_RDS_PASSWORD")
DATABASE = os.getenv("AWS_RDS_DATABASE")
PORT = 3306

connection = pymysql.connect(
    host=ENDPOINT,
    user=USER,
    password=PASSWORD,
    database=DATABASE,
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor,
)

try:
    connection = pymysql.connect(
        host=ENDPOINT,
        user=USER,
        password=PASSWORD,
        database=DATABASE,
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
    )

    print("Connection Established")

    cursor = connection.cursor()

    # Define the SQL statement for creating a table

    # Execute the query
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS users(
        user_id INT AUTO_INCREMENT PRIMARY KEY,
        email VARCHAR(100) NOT NULL,
        api_key VARCHAR(150) NOT NULL
    );
"""
    )
    # data = cursor.fetchmany()

    # print(data)

    # Commit the transaction
    connection.commit()

except pymysql.MySQLError as e:
    print(e)
# finally:

#     if connection:
#         connection.close()
#         print("Connection Closed")
