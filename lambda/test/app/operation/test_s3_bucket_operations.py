#
# Any code, applications, scripts, templates, proofs of concept, documentation
# and other items provided by AWS under this SOW are "AWS Content," as defined
# in the Agreement, and are provided for illustration purposes only. All such
# AWS Content is provided solely at the option of AWS, and is subject to the
# terms of the Addendum and the Agreement. Customer is solely responsible for
# using, deploying, testing, and supporting any code and applications provided
# by AWS under this SOW
#
import unittest
from unittest.mock import patch

import datetime
# @see: https://botocore.amazonaws.com/v1/documentation/api/latest/reference/stubber.html
import botocore.session
from botocore.stub import Stubber

from src.app.operation.s3_bucket_operations import S3BucketOperations
from src.app.model.s3_bucket_model import S3BucketModel

class TestS3BucketOperations(unittest.TestCase):

  def test_get_buckets(self):
    s3_client = botocore.session.get_session().create_client('s3')

    stubber = Stubber(s3_client)
    stub_response = {
      "Owner": {
        "ID": "foo",
        "DisplayName": "bar"
      },
      "Buckets": [{
        "CreationDate": datetime.datetime(2016, 1, 20, 22, 9),
        "Name": "baz"
      }]
    }
    stubber.add_response('list_buckets', stub_response, {})
    stubber.activate()

    buckets: List[S3BucketModel] = S3BucketOperations(s3_client).get_buckets()

    self.assertEqual(len(buckets), 1)
    self.assertEqual(buckets[0].Name, 'baz')





