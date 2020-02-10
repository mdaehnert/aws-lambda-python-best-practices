#
# Any code, applications, scripts, templates, proofs of concept, documentation
# and other items provided by AWS under this SOW are "AWS Content," as defined
# in the Agreement, and are provided for illustration purposes only. All such
# AWS Content is provided solely at the option of AWS, and is subject to the
# terms of the Addendum and the Agreement. Customer is solely responsible for
# using, deploying, testing, and supporting any code and applications provided
# by AWS under this SOW
#
class S3BucketModel():
  def __init__(self, list_bucket_entry):
    self.Name         = list_bucket_entry['Name']
    self.CreationDate = list_bucket_entry['CreationDate']


  def __repr__(self):
    """
    Used by logging module and print() function
    """
    return f"{self.__class__}(" \
      f"ID: {self.Name}, " \
      f"Arn: {self.CreationDate}" \
      ")"
