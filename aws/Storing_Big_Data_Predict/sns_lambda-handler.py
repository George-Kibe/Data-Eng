"""
    Description:
    This script provides functionality to generate custom AWS SNS
    email messages when triggered. 
"""

import boto3
import json

# ======================== EDIT THIS SECTION ========================================
# Insert your SNS topic ARN below
sns_arn = "arn:aws:sns:eu-west-1:179792149144:DEGEOWAM-streaming-sns-topic"
# Insert your full name and surname for marking purposes
student_name = "George Kibe Wambui"
# ===================================================================================


def lambda_handler(event, context):
    client = boto3.client("sns")
    resp = client.publish(TargetArn=sns_arn,
                          Message=json.dumps(event),
                          Subject=f"Failure: {student_name}, could not generate stream")
