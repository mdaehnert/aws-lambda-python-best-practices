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
