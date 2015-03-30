# IdeaScaly
# Copyright 2015 Jorge Saldivar
# See LICENSE for details.

from ideascaly.binder import bind_api
from ideascaly.parsers import ModelParser


class API():
    """IdeaScale API http://support.ideascale.com/customer/portal/articles/1001563-ideascale-rest-api"""

    _community_url = ''
    _last_call_pagination = {}

    def __init__(self, auth_handler, api_url='/a/rest/', ver='v1', timeout=60, parser=None):

        """ Api instance Constructor
        :param auth_handler: authentication handler
        :param api_url: API url, default:/a/rest/
        :param ver: API version, default:v1
        :param timeout: delay before to consider the request as timed out in seconds, default:60
        :param parser: ModelParser instance to parse the responses, default:None
        """
        self.auth_handler = auth_handler
        self.url = api_url + ver
        self.timeout = timeout
        self.parser = parser or ModelParser()

    @property
    def community_url(self):
        return self._community_url

    @community_url.setter
    def community_url(self, value):
        self._community_url = value

    @property
    def last_call_pagination(self):
        return self._last_call_pagination

    @last_call_pagination.setter
    def last_call_pagination(self, values):
        self._last_call_pagination['pager_total_count'] = values['pager_total_count']
        self._last_call_pagination['pager_page_size'] = values['pager_page_size']
        self._last_call_pagination['pager_current_page_number'] = values['pager_current_page_number']
        self._last_call_pagination['pager_first_index'] = values['pager_first_index']
        self._last_call_pagination['pager_last_index'] = values['pager_last_index']

    def get_ideas_in_review(self, **kwargs):
        return bind_api(
            api=self,
            path='/ideas/inreview',
            payload_type='idea',
            payload_list=True
        )(**kwargs)

    def get_ideas_in_progress(self, **kwargs):
        return bind_api(
            api=self,
            path='/ideas/inprogress',
            payload_type='idea',
            payload_list=True
        )(**kwargs)

    def get_ideas_complete(self, **kwargs):
        return bind_api(
            api=self,
            path='/ideas/complete',
            payload_type='idea',
            payload_list=True
        )(**kwargs)

    def get_votes_idea(self, *args, **kwargs):
        """ :allowed_param:'ideaId'
        """
        return bind_api(
            api=self,
            path='/ideas/{ideaId}/votes',
            payload_type='vote',
            allowed_param=['ideaId'],
            payload_list=True
        )(*args, **kwargs)

    def get_comments_idea(self, *args, **kwargs):
        """ :allowed_param:'ideaId'
        """
        return bind_api(
            api=self,
            path='/ideas/{ideaId}/comments',
            payload_type='comment',
            allowed_param=['ideaId'],
            payload_list=True
        )(*args, **kwargs)

    @property
    def get_campaigns(self):

        return bind_api(
            api=self,
            path='/campaigns',
            payload_type='campaign',
            payload_list=True
        )

    def get_idea_details(self, *args, **kwargs):
        """ :allowed_param:'ideaId'
        """
        return bind_api(
            api=self,
            path='/ideas/{ideaId}',
            payload_type='idea',
            allowed_param=['ideaId']
        )(*args, **kwargs)

    def get_ideas_campaign(self, *args, **kwargs):
        """ :allowed_param:'campaignId'
        """
        return bind_api(
            api=self,
            path='/campaigns/{campaignId}/ideas',
            payload_type='idea',
            allowed_param=['campaignId'],
            payload_list=True
        )(*args, **kwargs)

    @property
    def get_active_ideas(self):
        return bind_api(
            api=self,
            path='/campaigns/active/ideas',
            payload_type='idea',
            payload_list=True
        )

    @property
    def get_archived_ideas(self):
        return bind_api(
            api=self,
            path='/campaigns/archived/ideas',
            payload_type='idea',
            payload_list=True
        )

    def get_top_ideas(self, **kwargs):
        return bind_api(
            api=self,
            path='/ideas/top',
            payload_type='idea',
            payload_list=True
        )(**kwargs)

    def get_recent_ideas(self, **kwargs):
        return bind_api(
            api=self,
            path='/ideas/recent',
            payload_type='idea',
            payload_list=True
        )(**kwargs)

    def get_hot_ideas(self, **kwargs):
        return bind_api(
            api=self,
            path='/ideas/hot',
            payload_type='idea',
            payload_list=True
        )(**kwargs)

    def create_new_member(self, *args, **kwargs):
        """ :allowed_param: 'name', 'email'
        """
        return bind_api(
            api=self,
            path='/members',
            method='POST',
            payload_type='author',
            allowed_param=['name','email']
        )(*args, **kwargs)

    def get_member_information(self, *args, **kwargs):
        """ :allowed_param: 'memberId'
        """
        return bind_api(
            api=self,
            path='/members/{memberId}',
            payload_type='author',
            allowed_param=['memberId']
        )(*args, **kwargs)

    def get_member_information_by_name(self, *args, **kwargs):
        """ :allowed_param: 'name'
        """
        return bind_api(
            api=self,
            path='/members/name/{name}',
            payload_type='author',
            allowed_param=['name']
        )(*args, **kwargs)

    def get_member_information_by_email(self, *args, **kwargs):
        """ :allowed_param: 'email'
        """
        return bind_api(
            api=self,
            path='/members/email/{email}',
            payload_type='author',
            allowed_param=['email']
        )(*args, **kwargs)

    def get_member_ideas(self, *args, **kwargs):
        """ :allowed_param: 'memberId'
        """
        return bind_api(
            api=self,
            path='/members/{memberId}/ideas',
            payload_type='idea',
            payload_list=True,
            allowed_param=['memberId']
        )(*args, **kwargs)

    def create_new_idea(self, *args, **kwargs):
        """ :allowed_param: 'title', 'text', 'campaignId' (optional), 'tags' (optional), 'customFields' (optional)
        """
        return bind_api(
            api=self,
            path='/idea',
            method='POST',
            payload_type='idea',
            allowed_param=['title', 'text', 'campaignId', 'tags', 'customFields']
        )(*args, **kwargs)

    def attach_media_to_idea(self, *args, **kwargs):
        # TODO
        raise NotImplementedError

    def delete_idea(self, *args, **kwargs):
        """ :allowed_param: 'ideaId'
        """
        return bind_api(
            api=self,
            path='/ideas/{ideaId}/delete',
            method='DELETE',
            payload_type='idea',
            allowed_param=['ideaId']
        )(*args, **kwargs)

    def vote_up_idea(self, *args, **kwargs):
        """ :allowed_param: 'ideaId', 'myVote' (optional)
        """
        return bind_api(
            api=self,
            path='ideas/{ideaId}/vote/up',
            method='POST',
            payload_type='vote',
            allowed_param=['ideaId', 'myVote']
        )(*args, **kwargs)

    def vote_down_idea(self, *args, **kwargs):
        """ :allowed_param: 'ideaId', 'myVote' (optional)
        """
        return bind_api(
            api=self,
            path='ideas/{ideaId}/vote/down',
            method='POST',
            payload_type='vote',
            allowed_param=['ideaId', 'myVote']
        )(*args, **kwargs)

    def comment_idea(self, *args, **kwargs):
        """ :allowed_param: 'ideaId', 'text'
        """
        return bind_api(
            api=self,
            path='ideas/{ideaId}/comment',
            method='POST',
            payload_type='comment',
            allowed_param=['ideaId', 'text']
        )(*args, **kwargs)

    def comment_comment(self, *args, **kwargs):
        """ :allowed_param: 'commentId', 'text'
        """
        return bind_api(
            api=self,
            path='comments/{commentId}/comment',
            method='POST',
            payload_type='comment',
            allowed_param=['commentId', 'text']
        )(*args, **kwargs)

    def delete_comment(self, *args, **kwargs):
        """ :allowed_param: 'commentId'
        """
        return bind_api(
            api=self,
            path='comments/{commentId}/delete',
            method='DELETE',
            payload_type='comment',
            allowed_param=['commentId']
        )(*args, **kwargs)

    @property
    def get_all_comments(self):
        return bind_api(
            api=self,
            path='/comments',
            payload_type='comment',
            payload_list=True
        )

    def get_votes_comment(self, *args, **kwargs):
        """ :allowed_param: 'commentId'
        """
        return bind_api(
            api=self,
            path='/comments/{commentId}/votes',
            payload_type='vote',
            payload_list=True,
            allowed_param=['commentId']
        )(*args, **kwargs)

    @property
    def get_votes_comments(self):
        return bind_api(
            api=self,
            path='comments/votes',
            payload_type='vote',
            payload_list=True
        )

    @property
    def get_votes_ideas(self):
        return bind_api(
            api=self,
            path='/ideas/votes',
            payload_type='vote',
            payload_list=True
        )

    def get_votes_ideas_member(self, *args, **kwargs):
        """ :allowed_param: 'memberId'
        """
        return bind_api(
            api=self,
            path='/members/{memberId}/ideas/votes',
            payload_type='vote',
            payload_list=True,
            allowed_param=['memberId']
        )(*args, **kwargs)

    def get_votes_comments_member(self, *args, **kwargs):
        """ :allowed_param: 'memberId'
        """
        return bind_api(
            api=self,
            path='/members/{memberId}/comments/votes',
            payload_type='vote',
            payload_list=True,
            allowed_param=['memberId']
        )(*args, **kwargs)

    def get_comments_member(self, *args, **kwargs):
        """ :allowed_param: 'memberId'
        """
        return bind_api(
            api=self,
            path='/members/{memberId}/comments',
            payload_type='comment',
            payload_list=True,
            allowed_param=['memberId']
        )(*args, **kwargs)

    def get_comment_replies(self, *args, **kwargs):
        """ :allowed_param: 'commentId'
        """
        return bind_api(
            api=self,
            path='/comments/{commentId}',
            payload_type='comment',
            payload_list=True,
            allowed_param=['commentId']
        )(*args, **kwargs)