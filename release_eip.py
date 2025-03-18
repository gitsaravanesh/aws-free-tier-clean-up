import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    addresses = ec2.describe_addresses()

    for address in addresses['Addresses']:
        if 'InstanceId' not in address:
            allocation_id = address['AllocationId']
            ec2.release_address(AllocationId=allocation_id)
            print(f"Released unused Elastic IP: {allocation_id}")

    return "Elastic IP cleanup completed."
