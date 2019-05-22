from __future__ import print_function
from crhelper import CfnResource
import logging
import json

logger = logging.getLogger(__name__)
# Initialise the helper, all inputs are optional, this example shows the defaults
helper = CfnResource(json_logging=False, log_level='DEBUG', boto_level='CRITICAL')

@helper.create
def create(event, context):
    logger.info("Got Create")
    
    print("Received event: " + json.dumps(event, indent=2))
    print("value1 = " + event['ResourceProperties']['key1'])
    print("value2 = " + event['ResourceProperties']['key2'])
    print("value3 = " + event['ResourceProperties']['key3'])
    return event['ResourceProperties']['key1']  # Echo back the first key value

@helper.delete
def delete(event, context):
    logger.info("Got Delete")
    
def handler(event, context):
    helper(event, context)