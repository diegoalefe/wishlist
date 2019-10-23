import json

import psycopg2

import logging

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)


def claim_gift(event, context):
    log.info(json.dumps(event))

    item_id = event["pathParameters"]["id"]

    log.info(f"item_id: {item_id}")

    conn = psycopg2.connect(
        dbname="wishlist",
        user="postgres",
        password="docker",
        host="localhost",
        port="5432",
    )

    cur = conn.cursor()