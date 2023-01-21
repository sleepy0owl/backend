import boto3

def handler(event, context):
    try:
        print(event)
    except Exception as e:
        # write to sns topic
        print(e)