# Import the required libraries.
import numpy as np # Used for data manipulation.
import time # Used for timing the pipeline execution.
import boto3 # Library for interacting with Amazon services.
from botocore.exceptions import ClientError # Library for logging exceptions or errors.
from datetime import date # Get the date of the pipeline failure.
import random # Generate a random number iteratively to simulate a data pipeline running.

# Create the pipeline simulation.
def simulate_pipeline():
    # Characters are used to form a random data pipeline name.
    name = ['0','1','2','3','4','5','6','7','8','9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', '#', '!', '^', '@']
    # Create a random data pipeline name from the defined characters.
    name = "".join(random.sample(name, 15))
    # Log the start time of the pipeline execution.
    start = time.time()
    # Set the initial condition of the pipeline to True.
    pipeline = True
    # Add a variable used to count the number of pipeline executions.
    i = 0
    # While the pipeline status is True, we run the pipeline.
    while pipeline:
        # Generate a random number between 1 and 1000000000.
        iters = np.random.randint(0, 1_000_000_000,1)[0]
        # Logic to check if the generated number is between the defined bounds.
        # If Yes, then the pipeline status is changed from True to False, the metadata is logged, and the run is terminated.
        if ((iters <= 50_000_000) & (iters >= 49_999_500)):
            pipeline = False
            end = time.time()
            return f'On {date.today()} pipeline {name} failed after {i} iterations and ran for {np.round(((end - start)/3600),5)} hours', False
        # If No, then the pipeline status is still healthy, i.e. True and we add one more count to the counter variable and continue running the pipeline.
        else:
            pipeline = True
        i+=1


# Create the Amazon SES email functionality.
def simulate_pipeline_monitoring(aws_secret_key = 'YOURSECRETKEY',
                                 aws_access_key = 'YOURACCESSKEY',
                                 message_sender = "YOURVERIFIEDEMAIL",
                                 message_receiver = "YOURVERIFIEDEMAIL",
                                 aws_region_name = "YOURREGION",
                                 email_subject = 'EXAMPLEHEDDING'):

    SECRET_KEY = aws_secret_key
    KEY_ID = aws_access_key

    # Replace sender@example.com with your "From" address.
    # This address must be verified with Amazon SES.

    SENDER = message_sender

    # Replace recipient@example.com with a "To" address. If your account 
    # is still in the sandbox, this address must be verified.

    RECIPIENT = message_receiver

    # The AWS region you're using for Amazon SES.
    AWS_REGION = aws_region_name

    # The subject line for the email.
    SUBJECT = email_subject

    # The email body for recipients with non-HTML email clients.
    BODY_TEXT = ("Data pipeline failure alert\r\n"
                "This email was sent with Amazon SES using the "
                "AWS SDK for Python (Boto). It is an alert that your data pipeline has failed."
                )

    # The HTML body of the email.
    string_date = email_subject[3:14] # Extract the date from the email subject.
    iterations_before_failure = email_subject[52:59] # Extract the number of iterations from the email subject.
    hours_before_failure = email_subject[83:91] # Extract the number of hours from the email subject.
    BODY_HTML = """<html>
    <head></head>
    <body>
    <h1>Amazon SES Test Data Pipeline Failure Email</h1>
    <h2>Date of pipeline failure: {string_date}</h2>
    <h2>Iterations pipeline ran successfully before failure: {iterations_before_failure}</h2>
    <h2>Hours pipeline ran successfully before failure: {hours_before_failure}</h2>
    </body>
    </html>
                """.format(string_date=string_date, iterations_before_failure = iterations_before_failure, hours_before_failure = hours_before_failure)            

    # The character encoding for the email.
    CHARSET = "UTF-8"

    # Create a new SES resource and specify a region.
    client = boto3.client('ses', region_name=AWS_REGION, aws_secret_access_key=SECRET_KEY, aws_access_key_id = KEY_ID)

    # Try to send the email.
    try:
        # Provide the contents of the email.
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    RECIPIENT,
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': BODY_HTML,
                    },
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER,

        )

    # Display an error if something goes wrong. 

    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])
    

# Run the pipeline and send an email upon pipeline failure.

pipeline_health = simulate_pipeline()

if pipeline_health[1] == False:

    simulate_pipeline_monitoring(aws_secret_key = 'Ah3C9j7Yg',
                                 aws_access_key = 'AKIA5XNJCI',
                                 message_sender = "example@expl.net",
                                 message_receiver = "example@expl.net",
                                 aws_region_name = "eu-west-1",
                                 email_subject =  f'{pipeline_health[0]}')