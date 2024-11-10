from ..config import connection
from uuid import uuid4
import json


def create_workflow(username, schema):
    cursor = connection.cursor()
    uid = str(uuid4())
    workflow_id = "workflow-" + uid

    query = """
        INSERT INTO workflows (workflow_id, username, workflow_schema) VALUES (%s, %s, %s) 
    """

    try:
        # Execute the insertion query
        cursor.execute(query, (workflow_id, username, json.dumps(schema)))
        connection.commit()

        # Retrieve the inserted record to confirm
        cursor.execute("SELECT * FROM workflows WHERE workflow_id = %s", (workflow_id,))
        res = cursor.fetchone()

        # Parse the schema back into JSON if necessary
        schema = json.loads(res["workflow_schema"])
    except Exception as e:
        connection.rollback()
        print(f"Database error: {e}")
        return {"error": "Database error occurred"}
    finally:
        cursor.close()

    return {"workflow_id": workflow_id, "username": username, "workflow_schema": schema}
