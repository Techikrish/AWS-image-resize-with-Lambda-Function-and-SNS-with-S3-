# **[AWS image resize with Lambda Function and SNS with S3](https://github.com/Techikrish/AWS-image-resize-with-Lambda-Function-and-SNS-with-S3-)**

This repository contains a Python script that leverages AWS Lambda and the Pillow library (PIL Fork) to resize images stored in an Amazon S3 bucket. The script automatically resizes images to a specified width and height, maintaining the aspect ratio. After resizing, it publishes a notification to an Amazon SNS topic.

 Features:
-   Resizes images using the Pillow library.
-   Integrates with Amazon S3 and AWS Lambda.
-   Publishes notifications to an Amazon SNS topic.
##  Usage:
1.  Set up your AWS environment (S3 bucket, Lambda function, and SNS topic).
2.  Deploy the provided Python script as an AWS Lambda function.
3.  Configure the script with your source and destination bucket names and SNS topic ARN.
4.  Upload images to the source bucket.
5.  The Lambda function will automatically resize the images and publish notifications.
