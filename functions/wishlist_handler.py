import json

import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)

def claim_gift(event, context):
    log.info(json.dumps(event));

    item_id = event['pathParameters']['id']

    log.info(f"item_id: {item_id}")
