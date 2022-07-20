#creating an s3 bucket from AWS CLI using makebucket command
aws s3 mb  s3://<some-bucket-name>

#creating a folder inside an s3 bucket folder name is Logs
aws s3api put-object --bucket <some-bucket-name> --key "Logs/"

#uploading a file to your S3 source data bucket.
aws s3api put-object --bucket <s3-source-bucket-name> --key path/to/world-happiness-report-2021-2021.csv --body world-happiness-report-2021-2021.csv
# world-happiness-report-2021-2021.csv is the filename
#In this command, --key will be the path to the directory on the S3 bucket, and --body will be the path to the file on your local computer.

#create-pipeline command to create a pipeline
aws datapipeline create-pipeline --name <pipeline_name> --unique-id token
#The above command should create your pipeline and return a pipeline ID
"pipelineId": "df-072218229DVCGHWT5EKG"

#Next, upload the pipeline definition. This uses a JSON object as the source to create the actual structure of our data pipeline.
aws datapipeline put-pipeline-definition --pipeline-id <your-pipeline-id> --pipeline-definition file://pipeline_definition.json

#Verify that the pipeline has been created.
aws datapipeline list-pipelines
#verify that the pipeline succeeds using the below command to activate a run
aws datapipeline activate-pipeline --pipeline-id <your-pipeline-id>

#creating a an instace profile
aws iam create-instance-profile --instance-profile-name DataPipelineDefaultResourceRole

#Add Role to an instance profile
aws iam add-role-to-instance-profile --role-name S3Access --instance-profile-name Webserver
#Verify that the run has been completed successfully by using the list-runs command as well as checking for the presence of the CSV file in your S3 sink.
aws datapipeline list-runs --pipeline-id <your-pipeline-id>

#Once we have verified the pipeline runs successfully, delete the pipeline instance so it does not incur extra costs
aws datapipeline delete-pipeline --pipeline-id <your-pipeline-id>


#delete bucket object
aws s3api delete-object --bucket <s3-source-bucket-name> --key world-happiness-report-2021.csv








