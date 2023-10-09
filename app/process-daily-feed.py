import boto3
import json

# Initialize the S3 client
s3 = boto3.client('s3')

# Bucket and file key
bucket_name = 'cloudeyes'
file_key = 'raw-metrics/Overall Metrics.json'

# Fetch the file and read its contents
obj = s3.get_object(Bucket=bucket_name, Key=file_key)
file_content = obj['Body'].read().decode('utf-8')

# Parse the JSON content
data = json.loads(file_content)

# Now, you can process the JSON data as needed
print(data)

# Example: If it's a dictionary and you want to print all keys
if isinstance(data, dict):
    for key in data:
        print(key)

response['sms'] = client.submit_job(

    jobName="campign_run_sms",

    jobQueue=os.environ["BatchQueueName"],

    jobDefinition=os.environ["JobDefinition"],

    containerOverrides={

        "command": ["php", "artisan", "campaign:sendMessages", "sms"],

        "environment": [

            {"name": "TIMEZONE", "value": "America/Mexico_City"},

            {

                "name": "SMS_CAMPAIGN_SQLURL",

                        "value": os.environ["SMSCampaignSqsUrl"],

            },

        ],

    },

    timeout={"attemptDurationSeconds": 1000},

)
