import boto3
import sys

def create_free_tier_instance():
    ec2 = boto3.resource('ec2')

    response = ec2.create_key_pair(KeyName='test-key-pair')
    with open('test-key-pair.txt', 'w') as f:
        print(response.key_material, file=f)

    instances = ec2.create_instances(
        ImageId='ami-0be2609ba883822ec',
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        KeyName=response.key_name
    )
    print ("Instance Created")

created = create_free_tier_instance()
