#
# Any code, applications, scripts, templates, proofs of concept, documentation
# and other items provided by AWS under this SOW are "AWS Content," as defined
# in the Agreement, and are provided for illustration purposes only. All such
# AWS Content is provided solely at the option of AWS, and is subject to the
# terms of the Addendum and the Agreement. Customer is solely responsible for
# using, deploying, testing, and supporting any code and applications provided
# by AWS under this SOW
#

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
