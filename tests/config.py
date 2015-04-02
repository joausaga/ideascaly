import os
import sys
import unittest
sys.path.append('../ideascaly')

from ideascaly.auth import AuthNonSSO
from ideascaly.api import API

testing_community = 'fiveheads.ideascale.com'
testing_token = os.environ.get('TOKEN', '')


class IdeascalyTestCase(unittest.TestCase):

    def setUp(self):
        self.auth = create_auth()
        self.api = API(self.auth)
        self.api.community_url = testing_community


def create_auth():
    auth = AuthNonSSO(testing_token)
    return auth