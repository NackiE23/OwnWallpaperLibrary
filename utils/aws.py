from typing import List

import boto3

from config.settings import AWS_S3_ACCESS_KEY_ID, AWS_S3_SECRET_ACCESS_KEY, AWS_S3_REGION, AWS_S3_BUCKET


class S3Client:
    # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html
    _bucket = AWS_S3_BUCKET
    _client = None

    @classmethod
    def get_client(cls) -> boto3.client:
        if not cls._client:
            cls._client = boto3.client(
                's3',
                aws_access_key_id=AWS_S3_ACCESS_KEY_ID,
                aws_secret_access_key=AWS_S3_SECRET_ACCESS_KEY,
                region_name=AWS_S3_REGION
            )
        return cls._client

    def get_top_level_folders(self) -> List[str]:
        # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/paginator/ListObjectsV2.html
        response = self.get_client().list_objects_v2(Bucket=self._bucket, Delimiter='/')
        return [prefix['Prefix'] for prefix in response.get('CommonPrefixes', [])]
