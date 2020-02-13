import unittest
from unittest.mock import patch
import json

import src.app.index

import botocore.session
from botocore.stub import Stubber

class TestIndex(unittest.TestCase):

  stub_response = {
    "Buckets": [{
      "Name": "baz",
      "CreationDate": "2016-01-20 22:09:00"
    }]
  }


  def get_client_for_test_handler():
    s3_client = botocore.session.get_session().create_client('s3')

    stubber = Stubber(s3_client)
    stubber.add_response('list_buckets', TestIndex.stub_response, {})
    stubber.activate()

    return s3_client


  @patch('src.app.index.get_s3_client', get_client_for_test_handler)
  """
  This test is only for demonstration of mocking/patching a modules function.
  In this example we mock the 'get_s3_client' function to ensure that only mock calls are sent throughout the test.
  """

  def test_handler(self):
    response = src.app.index.handler({}, {})

    self.assertEqual(response, json.dumps(self.stub_response['Buckets']))


