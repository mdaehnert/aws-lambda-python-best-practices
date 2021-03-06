from typing import List

from ..util.logging import configure_logger
from ..model.s3_bucket_model import S3BucketModel

LOGGER = configure_logger(__name__)

class S3BucketOperations():
  def __init__(self, s3_client):
    self.s3_client = s3_client

  def get_buckets(self) -> List[S3BucketModel]:
    response = []

    bucket_response = self.s3_client.list_buckets()
    for single_bucket_response in bucket_response['Buckets']:
      response.append(S3BucketModel(single_bucket_response))

    return response
