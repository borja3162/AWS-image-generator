import boto3
import os

BUCKET_NAME = 'borja-s3-image-generator-bucket'


def move_file_to_s3(file_path:str):

    """
    Moves a file to the S3 bucket, removing the local copy from the EC2 instance.

    Local file is deleted regardless of upload success to avoid accumulation of files
    """

    if not os.path.exists(file_path):
        return

    s3_client = boto3.client('s3')
    try:
        s3_client.upload_file(file_path, BUCKET_NAME, file_path)
    except Exception as e:
        print( f'Failed to upload file {file_path} to S3 bucket {BUCKET_NAME}: {e}'   )

    try:
        os.remove(file_path)
    except Exception as e:
        print( f'Failed to remove file {file_path} from EC2 instance: {e}' )








