import json
import boto3

s3_client = boto3.client('s3')
dest_bucket_name = 'destination-bucket-name'

def lambda_handler(event, context):
    try:
        s3_event = event['Records'][0]['s3']
        bucket_name = s3_event['bucket']['name']
        object_key = s3_event['object']['key']

        response = s3_client.get_object(Bucket=bucket_name, Key=object_key)
        object_content = response['Body'].read()

        s3_client.put_object(
            Body=object_content,
            Bucket=dest_bucket_name,
            Key=f'resized/{object_key}'
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps('Successfully scaled image')
        }
        
    except Exception as e:
        print(f'Error {e}')
        return {
            'statusCode': 500,
            'body': json.dumps('Error scaling image')
        }
