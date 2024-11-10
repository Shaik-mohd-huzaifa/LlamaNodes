from ..config import connection
import secrets
import pymysql


def generate_api_key():
    api_key = "worx-ai-" + secrets.token_hex(16)
    return api_key


def create_or_update_user(email):
    api_key = generate_api_key()

    try:
        with connection.cursor() as cursor:
            # Check if user with the given email already exists
            check_query = "SELECT * FROM users WHERE email = %s"
            cursor.execute(check_query, (email))
            user = cursor.fetchone()

            if user:
                connection.commit()
                return {
                    "email": user["email"],
                    "api_key": user["api_key"],
                }
            else:
                # If user does not exist, create a new record
                insert_query = "INSERT INTO users (email, api_key) VALUES (%s, %s)"
                cursor.execute(insert_query, (email, api_key))
                connection.commit()
                return {
                    "status": "created",
                    "message": "User created successfully",
                    "email": email,
                    "api_key": api_key,
                }

    except pymysql.MySQLError as e:
        print(f"Error: {str(e)}")
        return {"status": "error", "message": f"Database error: {str(e)}"}

    finally:
        cursor.close()
