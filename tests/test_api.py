import os
import unittest

from tests.config import IdeascalyTestCase
from ideascaly.models import Idea, Vote, Comment, Campaign, Author

"""Unit tests"""


class IdeascalyAPITests(IdeascalyTestCase):

    # ---
    # Testing variables
    # ---
    campaign_id = 28416
    idea_id_votes = 139718
    idea_id_comments = 135840
    idea_id_attachment = 139717
    title_idea = "From the TestCase of IdeaScaly"
    text_idea = "Hello from IdeaScaly!"
    text_comment = "From the TestCase of IdeaScaly!"
    comment_id = 718829
    member_id = 691840
    member_email = "example@domain.com"
    member_name = "example"
    member_name_d = "donald"
    member_email_d = "donald@disney.info"
    member_id_ideas = 119840
    member_id_votes = 119793
    filename = str(os.path.join(os.path.dirname(__file__), 'pic.jpg'))

    # ----
    # Test cases related with community actions
    # ----
    def testget_all_ideas(self):
        result = self.api.get_all_ideas()
        self.assertEqual(type(result), type([]))
        if len(result) > 0: self.assertTrue(isinstance(result[0], Idea))

    def testget_all_votes(self):
        result = self.api.get_all_votes()
        self.assertEqual(type(result), type([]))
        if len(result) > 0: self.assertTrue(isinstance(result[0], Vote))

    def testget_all_comments(self):
        result = self.api.get_all_comments()
        self.assertEqual(type(result), type([]))
        if len(result) > 0: self.assertTrue(isinstance(result[0], Comment))

    def testget_all_members(self):
        result = self.api.get_all_members()
        self.assertEqual(type(result), type([]))
        if len(result) > 0: self.assertTrue(isinstance(result[0], Author))

    # ----
    # Test cases related with campaign actions
    # ----

    def testget_campaigns(self):
        result = self.api.get_campaigns()
        self.assertEqual(type(result), type([]))
        if len(result) > 0: self.assertTrue(isinstance(result[0], Campaign))

    def testget_active_ideas(self):
        result = self.api.get_active_ideas()
        self.assertEqual(type(result), type([]))
        if len(result) > 0: self.assertTrue(isinstance(result[0], Idea))

    def testget_archived_ideas(self):
        result = self.api.get_archived_ideas()
        self.assertEqual(type(result), type([]))
        if len(result) > 0: self.assertTrue(isinstance(result[0], Idea))

    def testget_ideas_campaign(self):
        result = self.api.get_ideas_campaign(self.campaign_id)
        self.assertEqual(type(result), type([]))
        if len(result) > 0: self.assertTrue(isinstance(result[0], Idea))

    # ----
    # Test cases related with idea actions
    # ----

    def testget_ideas_in_progress(self):
        result = self.api.get_ideas_in_progress()
        self.assertEqual(type(result), type([]))
        if len(result) > 0: self.assertTrue(isinstance(result[0], Idea))

    def testget_ideas_in_progress_pagination(self):
        result = self.api.get_ideas_in_progress(page_number=0, page_size=25, order_key='date-down')
        self.assertEqual(type(result), type([]))
        if len(result) > 0: self.assertTrue(isinstance(result[0], Idea))

    def testget_ideas_in_progress_campaign(self):
        result = self.api.get_ideas_in_progress(campaign_id=self.campaign_id)
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
        result = self.api.get_votes_idea(ideaId=self.idea_id_votes)
        self.assertEqual(type(result), type([]))
        if len(result) > 0: self.assertTrue(isinstance(result[0], Vote))

    def testget_comments_idea(self):
        result = self.api.get_comments_idea(ideaId=self.idea_id_comments)
        self.assertEqual(type(result), type([]))
        if len(result) > 0: self.assertTrue(isinstance(result[0], Comment))

    def testget_idea_details(self):
        result = self.api.get_idea_details(self.idea_id_comments)
        self.assertTrue(isinstance(result, Idea))

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

    def testcreate_and_delete_idea(self):
        result = self.api.create_idea(title=self.title_idea, text=self.text_idea, campaignId=self.campaign_id)
        self.assertTrue(isinstance(result, Idea))
        result = self.api.delete_idea(ideaId=result.id)
        self.assertTrue(isinstance(result, Idea))

    def testvote_up_idea(self):
        result = self.api.vote_up_idea(ideaId=self.idea_id_comments)
        self.assertTrue(isinstance(result, Vote))

    def testvote_down_idea(self):
        result = self.api.vote_down_idea(ideaId=self.idea_id_votes)
        self.assertTrue(isinstance(result, Vote))

    def testadd_comment_idea(self):
        result = self.api.comment_idea(ideaId=self.idea_id_comments, text=self.text_comment)
        self.assertTrue(isinstance(result, Comment))

    def testattach_file_idea(self):
        result = self.api.attach_file_to_idea(filename=self.filename,ideaId=self.idea_id_attachment)
        self.assertTrue(isinstance(result, Idea))

    # ----
    # Test cases related with comment actions
    # ----

    def testadd_and_delete_comment_comment(self):
        result = self.api.comment_comment(commentId=self.comment_id, text=self.text_comment)
        self.assertTrue(isinstance(result, Comment))
        result = self.api.delete_comment(commentId=result.id)
        self.assertTrue(isinstance(result, Comment))

    def testget_votes_comment(self):
        result = self.api.get_votes_comment(commentId=self.comment_id)
        self.assertEqual(type(result), type([]))
        if len(result) > 0: self.assertTrue(isinstance(result[0], Vote))

    def testget_votes_comments(self):
        result = self.api.get_votes_comments()
        self.assertEqual(type(result), type([]))
        if len(result) > 0: self.assertTrue(isinstance(result[0], Vote))

    def testget_comment(self):
        result = self.api.get_comment(commentId=self.comment_id)
        self.assertEqual(type(result), Comment)

    def testget_all_comments_pagination(self):
        result = self.api.get_all_comments(page_number=0, page_size=25)
        self.assertEqual(type(result), type([]))
        if len(result) > 0: self.assertTrue(isinstance(result[0], Comment))

    # -----
    # Test cases related with member actions
    # -----

    def testcreate_new_member(self):
        result = self.api.create_new_member(name="me", email="me@xyz.info")
        self.assertTrue(isinstance(result, Author))

    def testcreate_new_member_silent(self):
        result = self.api.create_new_member(name="Pato Donald", email="donald@disney.info", silent=True)
        self.assertTrue(isinstance(result, Author))

    def testget_member_info_by_id(self):
        result = self.api.get_member_info_by_id(memberId=self.member_id)
        self.assertTrue(isinstance(result, Author))
        self.assertEqual(result.email,self.member_email)

    def testget_member_info_by_name(self):
        result = self.api.get_member_info_by_name(name=self.member_name_d)
        self.assertEqual(type(result), type([]))
        if len(result) > 0:
            self.assertTrue(isinstance(result[0], Author))
            self.assertEqual(result[0].email,self.member_email_d)

    def testget_member_info_by_email(self):
        result = self.api.get_member_info_by_email(email=self.member_email)
        self.assertTrue(isinstance(result, Author))
        self.assertEqual(result.name,self.member_name)

    def testget_member_ideas(self):
        result = self.api.get_member_ideas(memberId=self.member_id_ideas)
        self.assertEqual(type(result), type([]))
        if len(result) > 0: self.assertTrue(isinstance(result[0], Idea))

    def testget_member_ideas_pagination(self):
        result = self.api.get_member_ideas(memberId=self.member_id_ideas, page_number=0, page_size=25)
        self.assertEqual(type(result), type([]))
        if len(result) > 0: self.assertTrue(isinstance(result[0], Idea))

    def testget_member_comments_votes(self):
        result = self.api.get_votes_comments_member(memberId=self.member_id_votes)
        self.assertEqual(type(result), type([]))
        if len(result) > 0: self.assertTrue(isinstance(result[0], Vote))

    def testget_member_ideas_votes(self):
        result = self.api.get_votes_ideas_member(memberId=self.member_id_votes)
        self.assertEqual(type(result), type([]))
        if len(result) > 0: self.assertTrue(isinstance(result[0], Vote))

    def testget_member_comments(self):
        result = self.api.get_comments_member(memberId=self.member_id_ideas)
        self.assertEqual(type(result), type([]))
        if len(result) > 0: self.assertTrue(isinstance(result[0], Comment))

    def testattach_image_member_avatar(self):
        result = self.api.attach_avatar_to_member(filename=self.filename, memberId=self.member_id_votes)
        self.assertTrue('url' in result.keys())


if __name__ == '__main__':
    unittest.main()
