import boto3
import sys
from botocore.exceptions import NoCredentialsError


def delete_from_aws(bucket, s3_object):
    s3 = boto3.client('s3')

    try:
        s3.delete_object(
            Bucket=bucket, 
            gitKey=s3_object)
        print("Delete Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False


deleted = delete_from_aws(sys.argv[1], sys.argv[2])