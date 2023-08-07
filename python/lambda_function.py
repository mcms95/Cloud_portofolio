import boto3
import os
import json
from decimal import Decimal  # Import the Decimal class

def lambda_handler(event, context):
    
    # Create a connection to DynamoDB
    dynamodb = boto3.resource("dynamodb")
    
    # Get the name of the table from an environment variable
    table_name = os.environ["TABLE_NAME"]
    
    # Connect to the specific table in DynamoDB
    table = dynamodb.Table(table_name)

    # Get the current visit count from the database
    response = table.get_item(Key={"id": "website_visits"})
    
    # If the item exists in the table, get the current count
    if "Item" in response:
        visit_count = response["Item"]["count"]
    else:
        # If the item doesn't exist, it's the first visit, so set the count to 0
        visit_count = 0
    
    # Convert Decimal to int for serialization
    visit_count = int(visit_count)
    
    # Increment the visit count by 1 for each visit
    visit_count += 1
    
    # Update the new visit count in the table
    table.put_item(Item={"id": "website_visits", "count": visit_count})
    
    # Return the total visit count as the response
    return {
    'statusCode': 200,
    'headers': {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
    },
    'body': json.dumps({'total_visits': visit_count})
}


if __name__ == "__main__":
    os.environ["TABLE_NAME"] = "visit-count-table"
    event = {"user" : "nuno_local"}
    print(lambda_handler(event, None))