# Serverless Image Scaler

This project demonstrates the use of aws lambda and s3 to create a serverless image processing application. Whenever an image is uploaded to an s3 bucket, an aws lambda function is triggered to process the image and move it to a separate destination bucket.

**Note:** The actual image resizing is not implemented in this project. Zhe focus is on using serverless technologies like aws lambda and s3 to demonstrate an automated image processing workflow.

## Technologies used

- **aws lambda:** serverless computing service to run code without provisioning or managing servers.
- **aws s3:** storage solution for uploaded and processed images.
- **python 3.x:** programming language used for the lambda function.
- **boto3:** aws sdk for python to interact with s3.
- **cloudwatch:** monitoring and logging service for the lambda function.

## Architecture overview

the following diagram illustrates the flow of image processing with aws lambda and s3:

![image](https://github.com/user-attachments/assets/422a6625-b45c-4ff7-a334-a0d7ee0c9ec1)



-   **Source S3 Bucket:** Where the images are uploaded.
-   **AWS Lambda Function:** This function is automatically triggered whenever a new image is uploaded to the source bucket. The function processes the images (without resizing in this implementation) and stores them in the destination bucket.
-   **Destination S3 Bucket:** Where the processed images are stored.


## Project Overview

The goal of this project is to demonstrate how serverless technologies like **AWS Lambda** and **S3** can be used to create a simple image processing solution. The solution automatically triggers a Lambda function when an image is uploaded to a **source S3 bucket**. This function processes the image (without resizing) and stores it in a **destination S3 bucket**.



## Prerequisites

-   An AWS account.
-   Permissions to create and manage S3 buckets and Lambda functions.
-   Familiarity with **AWS IAM policies** to grant Lambda the necessary permissions.



## Setup Instructions

### 1. Create S3 Buckets

-   **Step 1:** Log in to the [AWS Management Console](https://aws.amazon.com/console/).
-   **Step 2:** Create two S3 buckets:
    -   **Source Bucket:** Where images will be uploaded.
    -   **Destination Bucket:** Where processed images will be stored.


### 2. Create an AWS Lambda Function

-   **Step 1:** Go to the AWS Lambda console and create a new function.
-   **Step 2:** Choose **Python 3.x** as the runtime.
-   **Step 3:** In the following subsections, we will explain the code located in the `lambda_function.py` file.

---
### 3. Code Explanation
#### 3.1. Importing Libraries and Initial Setup

At the beginning of `lambda_function.py`, we import the necessary libraries. We use the **boto3** library to interact with AWS S3 and **json** for handling the response structure.


```import json
import boto3

#Creating an S3 client to interact with S3
s3_client = boto3.client('s3')
dest_bucket_name = 'destination-bucket-name'  # Change this to your destination bucket` 
```

-   **`boto3.client('s3')`:** This line creates an S3 client that allows the Lambda function to perform operations on S3, such as reading from the source bucket and writing to the destination bucket.
-   **`dest_bucket_name`:** This variable should be set to the name of your destination bucket where the processed images will be stored.

#### 3.2. Lambda Handler Function

The `lambda_handler` function in `lambda_function.py` is the entry point of the Lambda function. It is triggered automatically when an image is uploaded to the source S3 bucket.


```
def lambda_handler(event, context):
    try:
        # Process S3 event
        s3_event = event['Records'][0]['s3']
        bucket_name = s3_event['bucket']['name']
        object_key = s3_event['object']['key']` 
```

-   **`event`:** Contains information about the event that triggered the function, including details about the uploaded image. The event object is passed by S3 when a new file is uploaded.
-   **`s3_event`:** This extracts details of the S3 event, such as the name of the bucket (`bucket_name`) and the key (or filename) of the uploaded image (`object_key`).

#### 3.3. Retrieving the Image from S3

The function then retrieves the uploaded image from the source bucket using the S3 client.



```
# Retrieve the image from the S3 bucket
response = s3_client.get_object(Bucket=bucket_name, Key=object_key)
image_content = response['Body'].read()` 
```
-   **`get_object`:** This method retrieves the image from the source S3 bucket. It requires the `Bucket` and `Key` parameters.
-   **`response['Body'].read()`:** Reads the content of the image file.

#### 3.4. Storing the Image in the Destination Bucket

Once the image has been retrieved from the source bucket, it is uploaded to the destination bucket. In this implementation, no processing is done on the image.


```
# Store the image (without processing) in the destination bucket
s3_client.put_object(
    Body=image_content,
    Bucket=dest_bucket_name,
    Key=f'resized/{object_key}'
)` 
```
-   **`put_object`:** This method uploads the image to the destination S3 bucket. The `Body` contains the image data, and the `Key` specifies the location and filename in the destination bucket.
-   **`resized/{object_key}`:** The key includes a prefix `resized/`, which creates a folder in the destination bucket where all the processed images will be stored.

#### 3.5. Error Handling

The function includes a `try-except` block to handle any errors that occur during the process. If an error occurs, it is printed to the logs, and a response with an error message is returned.

```
 except Exception as e:
        print(f'Error {e}')
        return {
            'statusCode': 500,
            'body': json.dumps('Error moving image')
        }` 
```
-   **`Exception handling`:** Catches any errors that occur during the process, logs the error, and returns a failure response with a `500` status code.


-    Save the function and configure the environment variables (e.g., update the destination bucket name).

---


### 4. Configure Event Trigger

-   **Step 1:** Go to the S3 console and select your source bucket.
-   **Step 2:** Click on "Properties" and scroll to "Events."
-   **Step 3:** Create a new event trigger:
    -   **Event:** "PUT Object" (triggered when an object is uploaded).
    -   **Lambda Function:** Choose the Lambda function you created earlier.

### 5. Update IAM Permissions

-   **Step 1:** Go to the IAM console and create a role for the Lambda function.
-   **Step 2:** Attach the following permissions to the role:
    -   **AmazonS3FullAccess** or a custom policy that grants the Lambda function access to both the source and destination buckets.

### 6. Testing the Function

-   **Step 1:** Upload an image to the source bucket.
-   **Step 2:** Check the destination bucket to see if the image was successfully stored.
-   **Step 3:** Check the **CloudWatch Logs** in the Lambda console to ensure no errors occurred.

## Focus on Serverless Technologies

The focus of this project is on leveraging **AWS Lambda** and **S3** as core technologies to create a serverless architecture. By integrating Lambda and S3, the entire process is automatically triggered when a new image is uploaded. This implementation demonstrates how to set up a scalable, serverless workflow without dealing with server infrastructure.


## Monitoring and Logging

-   **CloudWatch Logs:** Check the logs in the AWS CloudWatch console to ensure that the function is executing correctly and no errors occur.
-   **Lambda Monitoring:** You can also monitor the execution time and other metrics of your Lambda function to improve its performance.


