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

    @property
    def get_votes_idea(self):
        """ :allowed_param:'ideaId'
        """
        return bind_api(
            api=self,
            path='/ideas/{ideaId}/votes',
            payload_type='vote',
            allowed_param=['ideaId'],
            payload_list=True
        )

    @property
    def get_comments_idea(self):
        """ :allowed_param:'ideaId'
        """
        return bind_api(
            api=self,
            path='/ideas/{ideaId}/comments',
            payload_type='comment',
            allowed_param=['ideaId'],
            payload_list=True
        )

    @property
    def get_campaigns(self):

        return bind_api(
            api=self,
            path='/campaigns',
            payload_type='campaign',
            payload_list=True
        )

    @property
    def get_idea_details(self):
        """ :allowed_param:'ideaId'
        """
        return bind_api(
            api=self,
            path='/ideas/{ideaId}',
            payload_type='idea',
            allowed_param=['ideaId']
        )

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
