import json
import boto3
from PIL import Image
from io import BytesIO

# Set your desired dimensions here
width, height = 800, 600
source_bucket_name = ''  # Replace with your actual source bucket name
destination_bucket_name = ''  # Replace with your actual destination bucket name
sns_topic_arn = 'arn:aws:sns:just add your AZ here :123456789012:MyTopic'  # Replace with your SNS topic ARN

s3_client = boto3.client('s3')
sns_client = boto3.client('sns')

def resize_image(image_data):
    image = Image.open(BytesIO(image_data))
    resized_image = image.resize((width // 2, height // 2))  # Adjust dimensions as needed
    return resized_image

def lambda_handler(event, context):
    try:
        bucket_name = event['Records'][0]['s3']['bucket']['name']
        object_key = event['Records'][0]['s3']['object']['key']

        if not object_key.startswith("resized_"):
            s3_response = s3_client.get_object(Bucket=bucket_name, Key=object_key)
            image_data = s3_response['Body'].read()

            resized_image = resize_image(image_data)

            output_buffer = BytesIO()
            resized_image.save(output_buffer, format='JPEG')  # Change format if necessary

            output_buffer.seek(0)
            new_object_key = f"resized_{object_key}"
            s3_client.put_object(Bucket=destination_bucket_name, Key=new_object_key, Body=output_buffer)

            # Publish a notification to the specified SNS topic
            sns_client.publish(TopicArn=sns_topic_arn, Message=f"Image {new_object_key} resized successfully!")

            return {
                'statusCode': 200,
                'body': json.dumps('Image resizing complete!')
            }
        else:
            print(f"Object {object_key} is already resized. Skipping processing.")
            return {
                'statusCode': 200,
                'body': json.dumps('Image already resized.')
            }
    except Exception as e:
        print(f"Error processing image: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps('Error processing image.')
        }
