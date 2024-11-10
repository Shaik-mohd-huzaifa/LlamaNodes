from ..config import connection
import pymysql


def get_workflow(api_key, workflow_id):
    cursor = connection.cursor()

    try:
        query = """SELECT * FROM users WHERE api_key = %s"""
        cursor.execute(query, (api_key))
        api_key_exists = cursor.fetchone()
        connection.commit()

        if api_key_exists:
            query = """SELECT * FROM workflows WHERE workflow_id = %s"""
            cursor.execute(query, (workflow_id))
            workflow = cursor.fetchone()

            if workflow:
                return {"workflow": workflow}
            else:
                return False
        else:
            return {
                "status": "error",
                "message": "API Key does not exists or not match",
            }
    except pymysql.MySQLError as e:
        print(f"Error: {str(e)}")
        return {"status": "error", "message": f"Database error: {str(e)}"}

    finally:
        cursor.close()
