import boto3

# Specify the AWS profile name from your AWS CLI configuration
aws_profile = 'jack'

# Create a DynamoDB client with the specified profile
session = boto3.Session(profile_name=aws_profile)
dynamodb=session.resource("dynamodb", region_name='us-east-2')
#dynamodb=session.client("dynamodb")

# Specify the table name
table_name = 'user'

# Specify the key to fetch from the DynamoDB table
key_to_fetch = {'id': '1'}

try:
    # Get the DynamoDB table
    table = dynamodb.Table(table_name)

    # Fetch the item using the specified key
    response = table.get_item(Key=key_to_fetch)

    # Check if the item was found
    if 'Item' in response:
        item = response['Item']
        print("Item found:", item)
    else:
        print("Item not found")

except Exception as e:
    print(f"Error: {e}")
