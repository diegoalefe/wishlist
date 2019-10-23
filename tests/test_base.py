import os

from functions.wishlist_handler import claim_gift


class TestBase(object):

    def setup(self):
        os.environ["dbname"] = 'wishlist'
        os.environ["user"] = 'alefe'
        os.environ["password"] = 'aem2007d'
        os.environ["host"] = 'localhost'
        os.environ["port"] = '5432'

    def test_base(self):

        event = {"pathParameters": {"id": 1}}

        claim_gift(event, None)
