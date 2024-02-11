# database.py

import boto3
from boto3.dynamodb.conditions import Attr

class DynamoDBManager:
    def __init__(self, aws_profile='jack', region_name='us-east-2'):
        try:
            self.session = boto3.Session(profile_name=aws_profile)
            self.dynamodb = self.session.resource('dynamodb', region_name=region_name)
            print("Connected to database")
        except Exception as e:
            print(f"Error connecting to the database: {e}")
            self.dynamodb = None

    def create_user_table(self):
        try:
            table_name = 'user'
            table = self.dynamodb.create_table(
                TableName=table_name,
                KeySchema=[
                    {'AttributeName': 'username', 'KeyType': 'HASH'}
                ],
                AttributeDefinitions=[
                    {'AttributeName': 'username', 'AttributeType': 'S'}
                ],
                ProvisionedThroughput={
                    'ReadCapacityUnits': 5,
                    'WriteCapacityUnits': 5
                }
            )
            table.wait_until_exists()
            print(f"Table {table_name} created successfully.")
        except Exception as e:
            print(f"Error creating user table: {e}")

    def create_request_table(self):
        try:
            table_name = 'request'
            table = self.dynamodb.create_table(
                TableName=table_name,
                KeySchema=[
                    {'AttributeName': 'request_id', 'KeyType': 'HASH'}
                ],
                AttributeDefinitions=[
                    {'AttributeName': 'request_id', 'AttributeType': 'N'}
                ],
                ProvisionedThroughput={
                    'ReadCapacityUnits': 5,
                    'WriteCapacityUnits': 5
                }
            )
            table.wait_until_exists()
            print(f"Table {table_name} created successfully.")
        except Exception as e:
            print(f"Error creating request table: {e}")

    def put_user_item(self, item):
        try:
            table_name = 'user'
            user_table = self.dynamodb.Table(table_name)
            response = user_table.put_item(Item=item)
            print(f"User item added successfully. Response: {response}")
        except Exception as e:
            print(f"Error adding user item: {e}")

    def put_request_item(self, item):
        try:
            table_name = 'request'
            request_table = self.dynamodb.Table(table_name)
            response = request_table.put_item(Item=item)
            print(f"Request item added successfully. Response: {response}")
        except Exception as e:
            print(f"Error adding request item: {e}")

    def get_user_item(self, key):
        try:
            table_name = 'user'
            user_table = self.dynamodb.Table(table_name)
            response = user_table.get_item(Key=key)
            return response.get('Item')
        except Exception as e:
            print(f"Error getting user item: {e}")
            return None

    def get_request_item(self, key):
        try:
            table_name = 'request'
            request_table = self.dynamodb.Table(table_name)
            response = request_table.get_item(Key=key)
            return response.get('Item')
        except Exception as e:
            print(f"Error getting request item: {e}")
            return None

    def update_user_item(self, key, update_expression, expression_attribute_values):
        try:
            table_name = 'user'
            user_table = self.dynamodb.Table(table_name)
            response = user_table.update_item(
                Key=key,
                UpdateExpression=update_expression,
                ExpressionAttributeValues=expression_attribute_values
            )
            print(f"User item updated successfully. Response: {response}")
        except Exception as e:
            print(f"Error updating user item: {e}")

    def update_request_item(self, key, update_expression, expression_attribute_values):
        try:
            table_name = 'request'
            request_table = self.dynamodb.Table(table_name)
            response = request_table.update_item(
                Key=key,
                UpdateExpression=update_expression,
                ExpressionAttributeValues=expression_attribute_values
            )
            print(f"Request item updated successfully. Response: {response}")
        except Exception as e:
            print(f"Error updating request item: {e}")

    def get_requests_by_user(self, username):
        try:
            table_name = 'request'
            request_table = self.dynamodb.Table(table_name)
            response = request_table.scan(FilterExpression=Attr('buyer_username').eq(username) | Attr('seller_username').eq(username))
            return response.get('Items', [])
        except Exception as e:
            print(f"Error getting requests for user {username}: {e}")
            return []
