import unittest

from tests.config import IdeascalyTestCase
from ideascaly.models import Idea, Vote, Comment, Campaign

"""Unit tests"""


class IdeascalyAPITests(IdeascalyTestCase):

    def testget_ideas_in_progress(self):
        result = self.api.get_ideas_in_progress()
        self.assertEqual(type(result), type([]))
        if len(result) > 0: self.assertTrue(isinstance(result[0], Idea))

    def testget_ideas_in_progress_pagination(self):
        result = self.api.get_ideas_in_progress(page_number=0, page_size=25, order_key='date-down')
        self.assertEqual(type(result), type([]))
        if len(result) > 0: self.assertTrue(isinstance(result[0], Idea))

    def testget_ideas_in_progress_campaign(self):
        result = self.api.get_ideas_in_progress(campaign=31732)
        self.assertEqual(type(result), type([]))
        if len(result) > 0: self.assertTrue(isinstance(result[0], Idea))

    def testget_ideas_complete(self):
        result = self.api.get_ideas_complete()
        self.assertEqual(type(result), type([]))
        if len(result) > 0: self.assertTrue(isinstance(result[0], Idea))

    def testget_ideas_in_review(self):
        result = self.api.get_ideas_in_review()
        self.assertEqual(type(result), type([]))
        if len(result) > 0: self.assertTrue(isinstance(result[0], Idea))

    def testget_votes_idea(self):
        result = self.api.get_votes_idea("155259")
        self.assertEqual(type(result), type([]))
        if len(result) > 0: self.assertTrue(isinstance(result[0], Vote))

    def testget_comments_idea(self):
        result = self.api.get_comments_idea("157400")
        self.assertEqual(type(result), type([]))
        if len(result) > 0: self.assertTrue(isinstance(result[0], Comment))

    def testget_campaigns(self):
        result = self.api.get_campaigns()
        self.assertEqual(type(result), type([]))
        if len(result) > 0: self.assertTrue(isinstance(result[0], Campaign))

    def testget_idea_details(self):
        result = self.api.get_idea_details("157400")
        self.assertTrue(isinstance(result, Idea))

    def testget_ideas_campaign(self):
        result = self.api.get_ideas_campaign("31732")
        self.assertEqual(type(result), type([]))
        if len(result) > 0: self.assertTrue(isinstance(result[0], Idea))

    def testget_active_ideas(self):
        result = self.api.get_active_ideas()
        self.assertEqual(type(result), type([]))
        if len(result) > 0: self.assertTrue(isinstance(result[0], Idea))

    def testget_archived_ideas(self):
        result = self.api.get_archived_ideas()
        self.assertEqual(type(result), type([]))
        if len(result) > 0: self.assertTrue(isinstance(result[0], Idea))

    def testget_top_ideas(self):
        result = self.api.get_top_ideas()
        self.assertEqual(type(result), type([]))
        if len(result) > 0: self.assertTrue(isinstance(result[0], Idea))

    def testget_recent_ideas(self):
        result = self.api.get_recent_ideas()
        self.assertEqual(type(result), type([]))
        if len(result) > 0: self.assertTrue(isinstance(result[0], Idea))

    def testget_hot_ideas(self):
        result = self.api.get_hot_ideas()
        self.assertEqual(type(result), type([]))
        if len(result) > 0: self.assertTrue(isinstance(result[0], Idea))

if __name__ == '__main__':
    unittest.main()
