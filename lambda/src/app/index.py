#
# Any code, applications, scripts, templates, proofs of concept, documentation
# and other items provided by AWS under this SOW are "AWS Content," as defined
# in the Agreement, and are provided for illustration purposes only. All such
# AWS Content is provided solely at the option of AWS, and is subject to the
# terms of the Addendum and the Agreement. Customer is solely responsible for
# using, deploying, testing, and supporting any code and applications provided
# by AWS under this SOW
#
import os
import json
import boto3

from typing import List

from .util.logging import configure_logger
from .operation.s3_bucket_operations import S3BucketOperations
from .model.s3_bucket_model import S3BucketModel

LOGGER = configure_logger(__name__)

def handler(event, context):
  test_logger()
  buckets = get_buckets()

  LOGGER.debug(buckets)

  response = []
  for bucket in buckets:
    response.append({
      'Name':         bucket.Name,
      'CreationDate': str(bucket.CreationDate)
    })

  return json.dumps(response)


def test_logger():
  """
  Logger uses python's logging module.
  log level is read by os.environ.LOG_LEVEL for setup.
  @see: https://docs.python.org/3/library/logging.html
  """
  LOGGER.debug("Only logged, if DEBUG level is activated")
  LOGGER.info("Default log level for logger, if nothing mentioned.")


def get_buckets() -> List[S3BucketModel]:
  return S3BucketOperations(get_s3_client()).get_buckets()


def get_s3_client():
  return boto3.client('s3')
