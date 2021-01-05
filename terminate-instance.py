import boto3
import sys

def terminate(instance_id):
    ec2 = boto3.client('ec2')

    try:
        ec2.terminate_instances(
        InstanceIds=[instance_id])

        print("Instance Terminated")
    except:
        print("Terminate Failed")

terminated = terminate(sys.argv[1])