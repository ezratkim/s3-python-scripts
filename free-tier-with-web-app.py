import boto3
import os

def create_key_pair():
    ec2 = boto3.resource('ec2')

    key_pair = ec2.create_key_pair(KeyName='test-key-pair')
    with open('test-key-pair.txt', 'w') as f:
        print(key_pair.key_material, file=f)
    print('Key Pair Created and Saved in test-key-pair.txt')

    return key_pair

def create_security_group():
    ec2 = boto3.client('ec2')

    security_group = ec2.create_security_group(
        Description='SSH and port 5000',
        GroupName='SSH and port 5000')
    data = ec2.authorize_security_group_ingress(
        GroupName='SSH and port 5000',
        IpPermissions=[
            {'IpProtocol': 'tcp',
             'FromPort': 22,
             'ToPort': 22,
             'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
            {'IpProtocol': 'tcp',
             'FromPort': 5000,
             'ToPort': 5000,
             'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}
        ]
    )

    print('Security Group Created')
    print('Ingress Successfully Set at port 22, 5000')

    return security_group

def create_free_tier_instance():
    ec2 = boto3.resource('ec2')

    instances = ec2.create_instances(
        ImageId='ami-0be2609ba883822ec',
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        SecurityGroupIds=[create_security_group()['GroupId']],
        KeyName=create_key_pair().key_name,
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'test',
                        'Value': 'test'
                    }
                ]
            }
        ]
    )
    print ("Instance Created")

'''def install-python():
    ssm = boto3.client('ssm')
    response = ec2.send_command(
        Targets=[
            {
                'Key': 'test'
            }
        ]
    )'''
created = create_free_tier_instance()
os.system("chmod 400 test-key-pair.txt")
