from ..config import connection
import pymysql


def get_user_workflows(email):
    cursor = connection.cursor()

    try:
        query = """SELECT * FROM workflows WHERE username = %s"""
        cursor.execute(query, (email))
        workflows = cursor.fetchall()

        return {"username": email, "workflows": workflows}
    except pymysql.MySQLError as e:
        print(f"Error: {str(e)}")
        return {"status": "error", "message": f"Database error: {str(e)}"}

    finally:
        cursor.close()
