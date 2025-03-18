import boto3
from datetime import datetime, timezone

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    instances = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            launch_time = instance['LaunchTime'].replace(tzinfo=timezone.utc)
            current_time = datetime.now(timezone.utc)
            instance_id = instance['InstanceId']
            
            if (current_time - launch_time).total_seconds() > 1800:  # 30 minutes
                ec2.terminate_instances(InstanceIds=[instance_id])
                print(f"Terminated instance: {instance_id}")

    return "EC2 cleanup completed."
