import json
import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    print(event)
    # Username
    user = event['detail']['userIdentity']['userName']

    # Instance ID
    instanceId = event['detail']['responseElements']['instancesSet']['items'][0]['instanceId'] # get the first element(id)
    
    ec2.create_tags(
        Resources=[
            instanceId
        ],
        Tags=[
            {
                'Key': 'Owner',
                'Value': user
            },
        ]
    )

    return 