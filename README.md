# aws-free-tier-clean-up

## AWS Free Tier Cleanup - Automated Cost Control
Many AWS users unintentionally exceed the Free Tier due to unused resources running in the background. This repository provides automated Lambda functions to clean up AWS resources and avoid unexpected costs.  

    
## Why Use This?  
Prevent EC2 instances from running longer than expected.  
Automatically delete unused EBS volumes.  
Release unassociated Elastic IPs to avoid charges.  
Stop idle RDS instances to save costs.  
Delete old RDS snapshots to optimize storage.  
  

## Setup Guide  
Follow these steps to deploy the automation using AWS Lambda and EventBridge.

1️⃣ Create an IAM Role for Lambda  
  
* Go to the AWS IAM console → Roles → Create Role.  
* Choose AWS Service → Lambda and click Next.  
* Attach the following policies:  
     AmazonEC2FullAccess  
     AmazonRDSFullAccess  
     AWSLambdaBasicExecutionRole  
* Name the role as LambdaCleanupRole and create it.  
  
2️⃣ Create Lambda Functions  
  
Repeat the steps below for each script in this repository:  

* Go to the AWS Lambda console and click Create function.  
* Select Author from scratch, name it (terminate_ec2, delete_ebs, etc.).  
* Choose Python 3.9 as the runtime.  
* Select Use an existing role and choose LambdaCleanupRole.  
* In the Code section, copy-paste the respective script from:  
    terminate_ec2.py  
    delete_ebs.py  
    release_eip.py  
    stop_rds.py  
    delete_rds_snapshots.py  
* Click Deploy.  
  
3️⃣ Schedule Cleanup with EventBridge  
* Go to AWS EventBridge → Rules → Create rule.  
* Name the rule aws-free-tier-cleanup.  
* Under Define pattern, choose Schedule expression.  
        Enter the expression:  
        cron(0 0,6,12,18 * * ? *)  
        (Runs every 6 hours.)  
* Click Next and select Lambda Function as the target.  
* Choose the Lambda function (terminate_ec2, delete_ebs, etc.).  
* Click Create.  
* Repeat these steps for all five Lambda functions.  
    
## Outcome  
Once set up, this automation will:  
✅ Terminate EC2 instances running for 30+ minutes.  
✅ Delete unused EBS volumes.  
✅ Release unassociated Elastic IPs.  
✅ Stop idle RDS databases.  
✅ Delete old RDS snapshots (older than 7 days).  
  

This setup ensures AWS usage remains optimized and prevents unnecessary costs.      
