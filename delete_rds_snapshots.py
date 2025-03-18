import boto3
from datetime import datetime, timezone, timedelta

rds = boto3.client('rds')

def lambda_handler(event, context):
    snapshots = rds.describe_db_snapshots(SnapshotType='manual')
    threshold_date = datetime.now(timezone.utc) - timedelta(days=7)

    for snapshot in snapshots['DBSnapshots']:
        snapshot_id = snapshot['DBSnapshotIdentifier']
        snapshot_date = snapshot['SnapshotCreateTime']

        if snapshot_date < threshold_date:
            rds.delete_db_snapshot(DBSnapshotIdentifier=snapshot_id)
            print(f"Deleted old RDS snapshot: {snapshot_id}")

    return "RDS snapshot cleanup completed."
