# IdeaScaly
# Copyright 2015 Jorge Saldivar
# See LICENSE for details.

import six


class IdeaScalyError(Exception):
    """IdeaScaly exception"""

    def __init__(self, reason, response=None):
        self.reason = six.text_type(reason)
        self.response = response
        Exception.__init__(self, reason)

    def __str__(self):
        return self.reason