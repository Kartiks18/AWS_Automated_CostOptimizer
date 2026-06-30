import boto3

ec2 = boto3.client('ec2')

INSTANCE_ID = "i-08eb5d39ede04cab3"

def lambda_handler(event, context):

    ec2.stop_instances(
        InstanceIds=[INSTANCE_ID]
    )

    return {
        "statusCode": 200,
        "body": "EC2 instance stopped successfully."
    }