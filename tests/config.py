from ideascaly.auth import AuthNonSSO
from ideascaly.api import API

import ConfigParser
import unittest

config = ConfigParser.ConfigParser()
config.read('config')


class IdeascalyTestCase(unittest.TestCase):

    def setUp(self):
        self.auth = create_auth()
        self.api = API(self.auth)
        self.api.community_url = config.get('test', 'community_url')


def create_auth():
    auth = AuthNonSSO(config.get('test', 'token'))
    return auth