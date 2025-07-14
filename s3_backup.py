import boto3

s3 = boto3.resource('s3')
def show_buckets(s3):
    """List all S3 buckets."""
    buckets = s3.buckets.all()
    for bucket in buckets:
        print(bucket.name)

show_buckets(s3)

# def create_bucket(s3):
#     s3.create_bucket(Bucket="vivekmodh-python-aws-bucket",CreateBucketConfiguration={
#         'LocationConstraint': 'us-west-2',},)
#     print("new python-bucket created successfully")

# create_bucket(s3)

def upload_bucket(s3,file_name,bucket_name,key_name):
    data = open(file_name, 'rb')
    s3.Bucket(bucket_name).put_object(Key=key_name, Body=data)
    print("file uploaded successfully")
bucket_name = "vivekmodh-python-aws-bucket"
region = "us-west-2"
file_name =   "F:\python-for-devops\hello.txt"

upload_bucket(s3, file_name, bucket_name,"hello")
