import sys
sys.path.append('../ideascaly')

from ideascaly.auth import AuthNonSSO
from ideascaly.api import API

import unittest

testing_community = 'fiveheads.ideascale.com'
testing_token = '5b3326f8-50a5-419d-8f02-eef6a42fd61a'


class IdeascalyTestCase(unittest.TestCase):

    def setUp(self):
        self.auth = create_auth()
        self.api = API(self.auth)
        self.api.community_url = testing_community


def create_auth():
    auth = AuthNonSSO(testing_token)
    return auth