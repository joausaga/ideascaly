from ideascaly.auth import AuthResearch
from ideascaly.api import API

import ConfigParser
import unittest

config = ConfigParser.ConfigParser()
config.read('config')


class IdeascalyTestCase(unittest.TestCase):

    def setUp(self):
        self.auth = create_auth()
        self.api = API(self.auth, api_url='/a/rest/research/')
        self.api.community_url = config.get('test', 'community_url')


def create_auth():
    auth = AuthResearch(config.get('test', 'token'))
    return auth