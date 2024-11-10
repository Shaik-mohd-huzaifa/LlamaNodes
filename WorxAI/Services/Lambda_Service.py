import boto3
import json
from botocore.exceptions import BotoCoreError, ClientError
from dotenv import load_dotenv

load_dotenv()


def call_lambda(access_key, secret_key, region, function_name, input_data):
    AWS_ACCESS_KEY_ID = access_key
    AWS_SECRET_ACCESS_KEY = secret_key
    try:
        # Create a Lambda client using the provided credentials and region
        lambda_client = boto3.client(
            "lambda",
            region_name=region,
        )

        # Invoke the Lambda function
        response = lambda_client.invoke(
            FunctionName=function_name,
            InvocationType="RequestResponse",  # Synchronous invocation
            Payload=json.dumps(input_data),  # Convert the input data to JSON
        )

        # Read and parse the response payload
        response_payload = response["Payload"].read().decode("utf-8")
        return json.loads(response_payload)

    except (BotoCoreError, ClientError) as error:
        print(f"An error occurred: {error}")
        return None
