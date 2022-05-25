# EDIT ME!
# recordReaderS3/lambda_function.py
# This is lambda handler code that will execute each time an object is added to S3
import json

def record_created_handler(event, context):
    # Create a list to store new object keys
    written_objects = []

    # Iterate over each S3 event record
    for record in event['Records']:
       
        # Get the variables to check for
        event_name = record['eventName']
        bucket_name = record['s3']['bucket']['name']
        obj_key = record['s3']['object']['key']

        # Verify that the object was written to S3
        if event_name == 'ObjectCreated:Put' and bucket_name == 'sd-vehicle-data':
           
            # If so, then add it to the written_objects list
            written_objects.append(obj_key)
    
    # Return the collected written objects
    return {
        "bucket": 'sd-vehicle-data',
        "new_objects": written_objects
    }                 