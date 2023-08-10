import boto3

# Specify your Ubuntu server's private IP address
ubuntu_private_ip = "192.168.0.100"

# Specify your AWS credentials and region (replace with your own values)
aws_access_key = "YOUR_ACCESS_KEY"
aws_secret_key = "YOUR_SECRET_KEY"
aws_region = "us-east-1"

# Create a Boto3 EC2 client
ec2_client = boto3.client('ec2', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key, region_name=aws_region)

# Example: Describe instances on the Ubuntu server
def describe_instances():
    response = ec2_client.describe_instances(
        Filters=[
            {'Name': 'private-ip-address', 'Values': [ubuntu_private_ip]}
        ]
    )
    return response

if __name__ == "__main__":
    instances = describe_instances()
    print(instances)
