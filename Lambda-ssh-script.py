import json
import boto3

sns_topic_arn = 'YOUR_SNS_TOPIC_ARN'

def lambda_handler(event, context):
    sns_client = boto3.client('sns')
    
    # Extract CloudTrail log
    detail = event.get('detail', {})
    event_name = detail.get('eventName')
    source_ip = detail.get('sourceIPAddress')
    
    # Check for SSH attempt
    if event_name == 'RunInstances':
        for item in detail.get('requestParameters', {}).get('instancesSet', {}).get('items', []):
            for group in item.get('groupSet', {}).get('items', []):
                if group.get('groupId') == 'YOUR_SECURITY_GROUP_ID':  # Replace with your security group ID
                    message = f"SSH attempt detected from IP: {source_ip}"
                    sns_client.publish(TopicArn=sns_topic_arn, Message=message)

    return {
        'statusCode': 200,
        'body': json.dumps('Function executed successfully!')
    }
