workflow_builder_schema = """
    CREATE TABLE IF NOT EXISTS workflows (
        workflow_id VARCHAR(100) PRIMARY KEY,
        username VARCHAR(100) NOT NULL,
        workflow_schema JSON
    );
"""
