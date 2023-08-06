Dynamo db
- Change Read/write capacity settings to on-demand beacause provisioned is default

to insert a item in dynamo db, format should be in key-value pairs:

{
  "id": {
    "S": "2"
  },
  "name": {
    "S": "nuno"
  },
  "last_name": {
    "S": "Silva"
  }
}







Lambda

To lambda interact with dynamo db it should have permissions -> IAM role
to specify which table we want to give permissions we must get dynamo db table ARN to attach it to the role we will create:
    1- Create role with permission with basic permission to dynamo db
    2- create inline policy to aloow GetItem and PutItem
    3- add ARN to specify 

JSON dumps vs loads:
1- json.dumps(): This function is used to convert a Python object (usually a dictionary or list) into a JSON-formatted string.
2- json.loads(): This function is used to parse a JSON-formatted string and convert it back into a Python object (dictionary, list, etc.)


Lambda Anatomy:
3 argguments by default:
    1- event -> the event that trigerred lambda
    2- context -> Method and properties that provide information about invocation and execution and envirment
    3- callback -> callback method you can return to calling function that invoke lambda

3 types of events:
    1- Insert
    2- Modify
    3- Remove


AWS SDK for python is boto3, if not installed, just run pip install boto3

Try always to not create code that is hardcoded.
in the folowwing example, in order to acess dynamodb table we instead of hardocode its name, we create a enviroment variables, this way if i need to change table name, i dont need to change in the code, just change in env variables.
In lambda we can do it in configurations -> envirment variables
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

# local test
if __name__ == "__main__":
    os.environ["TABLE_NAME"] = "visit-count-table"
    event = {"user" : "nuno_local"}
    print(lambda_handler(event, None))


lambda permissions - Policy:
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "dynamodb:GetItem",
                "dynamodb:PutItem",
                "dynamodb:UpdateItem",
                "dynamodb:DeleteItem"
            ],
            "Resource": "arn:aws:dynamodb:REGION:ACCOUNT_ID:table/Website-count"
        }
    ]
}
