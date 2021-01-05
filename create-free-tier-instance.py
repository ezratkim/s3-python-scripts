import boto3

def create_free_tier_instance():
    ec2 = boto3.resource('ec2')

    instances = ec2.create_instances(
        ImageId='ami-0be2609ba883822ec',
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro'
    )
    print ("Instance Created")

created = create_free_tier_instance()
