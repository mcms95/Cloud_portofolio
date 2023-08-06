import boto3
import os

def lambda_handler(event: any, context: any):
    user = event["user"]
    visit_count : int = 0
    
    # Create a DynamoDb client
    dynamodb = boto3.resource("dynamodb")
    # Set table name through enviroment variable name
    table_name = os.environ["TABLE_NAME"]
    # Create table object
    table = dynamodb.Table(table_name)
    
    #Get current visit count
    response = table.get_item(Key={"user": user})
    if "Item" in response:
        visit_count = response["Item"]["count"]
    
    #Increment visit count
    visit_count += 1
    
    # Put new visit count into the table    
    table.put_item(Item={"user": user, "count" : visit_count})
    

    message = f"Hello {user} you have visited this page {visit_count} times !"
    return {"message": message}


if __name__ == "__main__":
    os.environ["TABLE_NAME"] = "visit-count-table"
    event = {"user" : "nuno_local"}
    print(lambda_handler(event, None))