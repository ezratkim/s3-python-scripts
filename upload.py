import boto3
import sys
from botocore.exceptions import NoCredentialsError

#ACCESS_KEY = 'XXXXXXXXXXXXXXXXXXXXXXX'
#SECRET_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'


def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client('s3')

    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False


uploaded = upload_to_aws(sys.argv[1], sys.argv[2], sys.argv[3])
