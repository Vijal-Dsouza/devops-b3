import boto3 

client = boto3.client('dynamodb')
table = 'devops-b3'

def lambda_handler(event, context):
    response = client.put_item(
        TableName = table,
        Item={
            "event_time": {"S": event["time"]},
            "EventSource": {"S": event["source"]},
            "EventName": {"S": event["detail-type"]},
            "ResourceName": {"L": [{"S": r} for r in event["resources"]]},
            "AWSRegion": {"S": event["region"]},
            "AccountId": {"S": event["account"]}
        }
    )


    return {
        'status':200,
        'message':'Data inserted successfully'
    }