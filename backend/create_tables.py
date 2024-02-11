import boto3
from botocore.exceptions import NoCredentialsError
from DynamoDBManager.DynamoDBManager import DynamoDBManager
  # Assuming your DynamoDBManager class is defined in a separate file

# Specify the names of the DynamoDB tables
USER_TABLE_NAME = 'user'
REQUEST_TABLE_NAME = 'request'

def create_dynamodb_table(dynamodb_manager, table_name, key_schema, attribute_definitions, provisioned_throughput):
    try:
        table = dynamodb_manager.dynamodb.create_table(
            TableName=table_name,
            KeySchema=key_schema,
            AttributeDefinitions=attribute_definitions,
            ProvisionedThroughput=provisioned_throughput
        )

        table.wait_until_exists()
        print(f"Table '{table_name}' created successfully.")

    except NoCredentialsError:
        print("AWS credentials not available.")
    except Exception as e:
        print(f"Error creating table '{table_name}': {e}")

def main():
    # Initialize DynamoDBManager with configurable AWS profile and region
    dynamo_manager = DynamoDBManager()

    # Define key schema, attribute definitions, and provisioned throughput for the 'user' table
    user_key_schema = [
        {'AttributeName': 'username', 'KeyType': 'HASH'}
    ]

    user_attribute_definitions = [
        {'AttributeName': 'username', 'AttributeType': 'S'}
    ]

    user_provisioned_throughput = {
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }

    # Create 'user' table
    create_dynamodb_table(dynamo_manager, USER_TABLE_NAME, user_key_schema, user_attribute_definitions, user_provisioned_throughput)

    # Define key schema, attribute definitions, and provisioned throughput for the 'request' table
    request_key_schema = [
        {'AttributeName': 'request_id', 'KeyType': 'HASH'}
    ]

    request_attribute_definitions = [
        {'AttributeName': 'request_id', 'AttributeType': 'N'}
    ]

    request_provisioned_throughput = {
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }

    # Create 'request' table
    create_dynamodb_table(dynamo_manager, REQUEST_TABLE_NAME, request_key_schema, request_attribute_definitions, request_provisioned_throughput)

if __name__ == '__main__':
    main()
