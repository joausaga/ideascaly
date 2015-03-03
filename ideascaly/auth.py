# IdeaScaly
# Copyright 2015 Jorge Saldivar
# See LICENSE for details.


class Auth(object):
    _token = {}

    @property
    def token(self):
        return self._token


class AuthNonSSO(Auth):

    def __init__(self, token):
        Auth.__init__(self)
        self._token = {'api_token':token}


class AuthNonSSOMem(Auth):

    def __init__(self, api_token, member_token):
        Auth.__init__(self)
        self._token = {'api_token': api_token, 'member_token': member_token}


class AuthSSO(Auth):

    def __init__(self, api_token, sso_token):
        Auth.__init__(self)
        self._token = {'api_token': api_token, 'sso_token': sso_token}


class AuthResearch(Auth):

    def __init__(self, token):
        Auth.__init__(self)
        self._token = {'research_api_token':token}
