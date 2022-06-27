# Import modules.

import json
import boto3

print('Loading function')

# Initialise the connection to S3 and AWS Data Pipeline
# via the boto3 module.

s3_client = boto3.client('s3')
data_pipeline_client = boto3.client('datapipeline')

# Specify the Data Pipeline ID and S3 bucket name.

data_pipeline_id = "df-072218229DVCGHWT5EKG"
bucket = "george-kibe-de-load-source"

def lambda_handler(event, context):
    # Prints out the contents of the event.
    print("Received event: " + json.dumps(event, indent=2))

    try:
        paginator = s3_client.get_paginator('list_objects')
        response_iterator = paginator.paginate(Bucket=bucket)
        response_pipeline = data_pipeline_client.describe_pipelines(pipelineIds=[data_pipeline_id])

        # Looping through the items in the source bucket to check for the presence of a .csv file.
        for response in response_iterator:
            for object_data in response['Contents']:
                key = object_data['Key']
                print(key)
                if key.endswith('.csv'):
                    if(response_pipeline):
                        activate = data_pipeline_client.activate_pipeline(pipelineId=data_pipeline_id,parameterValues=[])
                        print("activated")
                    else:
                        print("datapipeline not activated")
    except Exception as e:
        print(e)
        print('Error activating Data Pipeline: {}'.format(data_pipeline_id))
        raise e