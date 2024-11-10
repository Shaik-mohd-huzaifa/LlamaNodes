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

    cursor.execute(query, (workflow_id, username, json.dumps(schema)))
    connection.commit()

    cursor.execute("SELECT * FROM workflows WHERE workflow_id = %s", (workflow_id))
    res = cursor.fetchone()
    schema = json.loads(res["workflow_schema"])
    cursor.close()

    return {"workflow_id": workflow_id, "username": username, "workflow_schema": schema}
