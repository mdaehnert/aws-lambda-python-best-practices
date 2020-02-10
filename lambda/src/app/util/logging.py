#
# Any code, applications, scripts, templates, proofs of concept, documentation
# and other items provided by AWS under this SOW are "AWS Content," as defined
# in the Agreement, and are provided for illustration purposes only. All such
# AWS Content is provided solely at the option of AWS, and is subject to the
# terms of the Addendum and the Agreement. Customer is solely responsible for
# using, deploying, testing, and supporting any code and applications provided
# by AWS under this SOW
#
import logging
import os

def configure_logger(logger_name):
    """
    Configures a generic logger which can be imported and used as needed
    Params:
      * os.environ.LOG_LEVEL=DEBUG|INFO|WARNING|ERROR
    """

    # Create logger and define INFO as the log level
    logger = logging.getLogger(logger_name)
    logger.setLevel(os.environ.get("LOG_LEVEL", logging.INFO))
    logger.propagate = False

    # Define our logging formatter
    formatter = logging.Formatter(
        '%(asctime)s | %(levelname)s | %(name)s | %(message)s | (%(filename)s:%(lineno)d)')

    # Create our stream handler and apply the formatting
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    # Add the stream handler to the logger
    logger.addHandler(stream_handler)

    return logger
