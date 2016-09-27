import boto3
import json


def hello(event, context):
    return { "message": "Go Serverless v1.0! Your function executed successfully!", "event": event }


def push_to_sqs(event, context):
    sqs = boto3.resource('sqs')
    queue = sqs.get_queue_by_name(QueueName='serverless-demo')

    message_body = {'from': 'Javier Bravo', 'text': 'message text', 'to': {'emails': ['bob@email.com', 'mike@email.com']}}
    response = queue.send_message(MessageBody=json.dumps(message_body))

    return response
