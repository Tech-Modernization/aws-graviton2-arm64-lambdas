import json
import platform

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps(f'Hello from {platform.uname()}!')
    }
