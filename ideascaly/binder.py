# IdeaScaly
# Copyright 2015 Jorge Saldivar
# See LICENSE for details.

import json
import requests

from ideascaly.error import IdeaScalyError
from ideascaly.utils import convert_to_utf8_str


def bind_api(**config):

    class APIMethod(object):

        api = config['api']
        path = config['path']
        payload_type = config.get('payload_type', None)
        payload_list = config.get('payload_list', False)
        method = config.get('method', 'GET')
        allowed_param = config.get('allowed_param', [])
        pagination_param = config.get('pagination_param', [])
        post_param = config.get('post_param', [])
        session = requests.Session()

        def __init__(self, args, kwargs):
            self.parser = kwargs.pop('parser', self.api.parser)
            self.post_data = {}  # kwargs.pop('post_data', None)
            self.session.headers = self.api.auth_handler.token
            self.build_parameters(args, kwargs)
            self.build_path(args, kwargs)

        def build_path(self, args, kwargs):
            order_keys = ['date-down', 'date-up', 'votes-down', 'votes-up', 'comments-down', 'random-down',
                          'amount-pledged-down', 'vote.and.comments-down', 'status-down', 'status.change.date-down']

            for index, arg in enumerate(args):
                if arg is None:
                    continue
                try:
                    self.path = self.path.replace("{%s}" % self.allowed_param[index], convert_to_utf8_str(arg))
                except IndexError:
                    raise IdeaScalyError('Wrong number of parameters supplied!')

            for k, arg in kwargs.items():
                if arg is None:
                    continue
                if k not in self.allowed_param:
                    continue
                self.path = self.path.replace("{%s}" % k, convert_to_utf8_str(arg))

            if 'campaign_id' in kwargs.keys():
                self.path = '/campaigns/' + convert_to_utf8_str(kwargs['campaign_id']) + self.path

            # set status key
            if 'status_key' in kwargs.keys() and 'status_key' in self.pagination_param:
                self.path = self.path + '/' + convert_to_utf8_str(kwargs['status_key'])

            # set pagination
            if 'page_number' in kwargs.keys() and 'page_number' in self.pagination_param and \
               'page_size' in kwargs.keys() and 'page_size' in self.pagination_param:
                if isinstance(kwargs['page_number'],int) and isinstance(kwargs['page_size'],int):
                    self.path = self.path + '/' + convert_to_utf8_str(kwargs['page_number'])
                    self.path = self.path + '/' + convert_to_utf8_str(kwargs['page_size'])
                else:
                    raise IdeaScalyError('Error with pagination parameters, they both have to be numeric')

            # set result order
            if 'order_key' in kwargs.keys() and 'order_key' in self.pagination_param:
                if kwargs['order_key'] in order_keys:
                    self.path = self.path + '/' + convert_to_utf8_str(kwargs['order_key'])
                else:
                    raise IdeaScalyError('Error with order key parameter, it must be one of these: %s' % order_keys)

            # create new users without sending a verification email
            if 'silent' in kwargs.keys():
                if kwargs['silent']:
                    self.path += '/create/silent'

        def build_parameters(self, args, kwargs):
            self.post_data = {}

            if self.post_param:
                for index, arg in enumerate(args):
                    if arg is None:
                        continue
                    try:
                        self.post_data[self.post_param[index]] = convert_to_utf8_str(arg)
                    except IndexError:
                        raise IdeaScalyError('Too many parameters supplied!')

            for k, arg in kwargs.items():
                if arg is None:
                    continue
                if k not in self.post_param:
                    continue
                if k in self.post_data:
                    raise IdeaScalyError('Multiple values for parameter %s supplied!' % k)

                if isinstance(arg, type('')):
                    self.post_data[k] = convert_to_utf8_str(arg)
                else:
                    self.post_data[k] = arg

        def execute(self):
            # Build the URL of the end-point
            url = self.api.url + self.path
            if self.api.community_url.find("http") == -1:
                full_url = 'http://' + self.api.community_url + url
            else:
                full_url = self.api.community_url + url

            # Execute request
            try:
                self.session.headers['content-type'] = 'application/json'
                json_data = json.dumps(self.post_data)
                resp = self.session.request(self.method, full_url, data=json_data, timeout=self.api.timeout)
            except Exception as e:
                raise IdeaScalyError('Failed to send request: %s' % e)

            # If an error was returned, throw an exception
            if resp.status_code and not 200 <= resp.status_code < 300:
                try:
                    error_msg = self.parser.parse_error(resp.text)
                except Exception:
                    error_msg = "IdeaScale %s error response" % resp.status_code
                raise IdeaScalyError(error_msg, resp)

            # Parse the response payload
            result = self.parser.parse(self, resp.text)

            # Save pagination result
            if 'pager_total_count' in resp.headers.keys():
                self.api.last_call_pagination = resp.headers

            return result

    def _call(*args, **kwargs):
        method = APIMethod(args, kwargs)
        return method.execute()

    return _call