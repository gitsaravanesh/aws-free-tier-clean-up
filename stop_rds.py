import boto3

rds = boto3.client('rds')

def lambda_handler(event, context):
    instances = rds.describe_db_instances()

    for db in instances['DBInstances']:
        db_instance_id = db['DBInstanceIdentifier']
        status = db['DBInstanceStatus']
        
        if status == 'available':  # Consider idle if available
            rds.stop_db_instance(DBInstanceIdentifier=db_instance_id)
            print(f"Stopped idle RDS instance: {db_instance_id}")

    return "RDS cleanup completed."
