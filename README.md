# Serverless Image Scaler

this project demonstrates the use of aws lambda and s3 to create a serverless image processing application. whenever an image is uploaded to an s3 bucket, an aws lambda function is triggered to process the image and move it to a separate destination bucket.

**note:** the actual image resizing is not implemented in this project. the focus is on using serverless technologies like aws lambda and s3 to demonstrate an automated image processing workflow.

## technologies used

- **aws lambda:** serverless computing service to run code without provisioning or managing servers.
- **aws s3:** storage solution for uploaded and processed images.
- **python 3.x:** programming language used for the lambda function.
- **boto3:** aws sdk for python to interact with s3.
- **cloudwatch:** monitoring and logging service for the lambda function.

## architecture overview

the following diagram illustrates the flow of image processing with aws lambda and s3:

![image](https://github.com/user-attachments/assets/422a6625-b45c-4ff7-a334-a0d7ee0c9ec1)


**note:** update `path_to_image.png` with the correct path to the image in your github repository.

1. **source s3 bucket:** where the images are uploaded.
2. **aws lambda function:** this function is automatically triggered whenever a new image is uploaded to the source bucket. the function processes the images (without resizing in this implementation) and stores them in the destination bucket.
3. **destination s3 bucket:** where the processed images are stored.

## project overview

the goal of this project is to demonstrate how serverless technologies like aws lambda and s3 can be used to create a simple image processing solution. the solution automatically triggers a lambda function when an image is uploaded to a source s3 bucket. this function processes the image (without resizing) and stores it in a destination s3 bucket.

## prerequisites

- an aws account.
- permissions to create and manage s3 buckets and lambda functions.
- familiarity with aws iam policies to grant lambda the necessary permissions.

## setup instructions

### 1. create s3 buckets

1. log in to the aws management console.
2. create two s3 buckets:
   - **source bucket:** where images will be uploaded.
   - **destination bucket:** where processed images will be stored.

### 2. create an aws lambda function

1. go to the aws lambda console and create a new function.
2. choose python 3.x as the runtime.
3. in the next steps, the code in the `lambda_function.py` file will be explained.

#### 1. importing libraries and initial setup

at the beginning of `lambda_function.py`, we import the necessary libraries. we use the `boto3` library to interact with aws s3 and `json` for handling the response structure.

```python
import json
import boto3

# creating an s3 client to interact with s3
s3_client = boto3.client('s3')
dest_bucket_name = 'destination-bucket-name'  # change this to your destination bucket
