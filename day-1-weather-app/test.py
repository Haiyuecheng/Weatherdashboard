import os
import boto3
from dotenv import load_dotenv

load_dotenv()

s3 = boto3.client(
    's3',
    region_name=os.getenv('AWS_DEFAULT_REGION'),
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
)

try:
    response = s3.list_objects_v2(Bucket=os.getenv('AWS_BUCKET_NAME'))
    for obj in response.get('Contents', []):
        print(obj['Key'])
except Exception as e:
    print(f"Error: {e}")