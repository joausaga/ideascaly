# IdeaScaly
# Copyright 2015 Jorge Saldivar
# See LICENSE for details.

import json
import requests

from ideascaly.error import IdeaScalyError


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

        def __init__(self, args, kwargs):
            self.parser = kwargs.pop('parser', self.api.parser)
            self.post_data = kwargs.pop('post_data', {})
            self.headers = kwargs.pop('headers', {})
            self.headers.update(self.api.auth_handler.token)
            self.build_parameters(args, kwargs)
            self.build_path(args, kwargs)
            if 'content-type' in self.headers.keys() and self.headers['content-type'] == 'application/json':
                self.post_data = json.dumps(self.post_data)
            self.build_request_url()
            self.post_file = kwargs.pop('file', None)

        def build_path(self, args, kwargs):
            order_keys = ['date-down', 'date-up', 'votes-down', 'votes-up', 'comments-down', 'random-down',
                          'amount-pledged-down', 'vote.and.comments-down', 'status-down', 'status.change.date-down']

            for index, arg in enumerate(args):
                if arg is None:
                    continue
                try:
                    self.path = self.path.replace("{%s}" % self.allowed_param[index], str(arg))
                except IndexError:
                    raise IdeaScalyError('Wrong number of parameters supplied!')

            for k, arg in kwargs.items():
                if arg is None:
                    continue
                if k not in self.allowed_param:
                    continue
                self.path = self.path.replace("{%s}" % k, str(arg))

            if 'campaign_id' in kwargs.keys():
                self.path = '/campaigns/' + str(kwargs['campaign_id']) + self.path

            # set status key
            if 'status_key' in kwargs.keys() and 'status_key' in self.pagination_param:
                self.path = self.path + '/' + str(kwargs['status_key'])

            # set pagination
            if 'page_number' in kwargs.keys() and 'page_number' in self.pagination_param and \
               'page_size' in kwargs.keys() and 'page_size' in self.pagination_param:
                if isinstance(kwargs['page_number'],int) and isinstance(kwargs['page_size'],int):
                    self.path = self.path + '/' + str(kwargs['page_number'])
                    self.path = self.path + '/' + str(kwargs['page_size'])
                else:
                    raise IdeaScalyError('Error with pagination parameters, they both have to be numeric')

            # set result order
            if 'order_key' in kwargs.keys() and 'order_key' in self.pagination_param:
                if kwargs['order_key'] in order_keys:
                    self.path = self.path + '/' + str(kwargs['order_key'])
                else:
                    raise IdeaScalyError('Error with order key parameter, it must be one of these: %s' % order_keys)

            # create new users without sending a verification email
            if 'silent' in kwargs.keys():
                if kwargs['silent']:
                    self.path += '/create/silent'

        def build_parameters(self, args, kwargs):
            if self.post_param:
                for index, arg in enumerate(args):
                    if arg is None:
                        continue
                    try:
                        self.post_data.update({self.post_param[index]:arg})
                    except IndexError:
                        raise IdeaScalyError('Too many parameters supplied!')

            for k, arg in kwargs.items():
                if arg is None:
                    continue
                if k not in self.post_param:
                    continue
                if k in self.post_data:
                    raise IdeaScalyError('Multiple values for parameter %s supplied!' % k)
                self.post_data.update({k:arg})

        def build_request_url(self):
            url = self.api.url + self.path
            if self.api.community_url.find("http") == -1:
                self.request_url = 'http://' + self.api.community_url + url
            else:
                self.request_url = self.api.community_url + url

        def execute(self):
            # Execute request
            try:
                if self.method == 'POST':
                    resp = requests.post(self.request_url, headers=self.headers, timeout=self.api.timeout,
                                         files=self.post_file, data=self.post_data)
                elif self.method == 'DELETE':
                    resp = requests.delete(self.request_url, headers=self.headers, timeout=self.api.timeout,
                                           data=self.post_data)
                else:
                    resp = requests.get(self.request_url, headers=self.headers, timeout=self.api.timeout)
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