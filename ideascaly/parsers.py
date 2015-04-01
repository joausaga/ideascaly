# IdeaScaly
# Copyright 2015 Jorge Saldivar
# See LICENSE for details.

from ideascaly.models import ModelFactory
from ideascaly.utils import import_simplejson
from ideascaly.error import IdeaScalyError


class Parser(object):

    def parse(self, method, payload):
        """
        Parse the response payload and return the result.
        Returns a tuple that contains the result data and the cursors
        (or None if not present).
        """
        raise NotImplementedError

    def parse_error(self, payload):
        """
        Parse the error message from payload.
        If unable to parse the message, throw an exception
        and default error message will be used.
        """
        raise NotImplementedError


class RawParser(Parser):

    def __init__(self):
        pass

    def parse(self, method, payload):
        return payload

    def parse_error(self, payload):
        return payload


class JSONParser(Parser):

    payload_format = 'json'

    def __init__(self):
        self.json_lib = import_simplejson()

    def parse(self, method, payload):
        try:
            json = self.json_lib.loads(payload)
        except Exception as e:
            raise IdeaScalyError('Failed to parse JSON payload: %s' % e)

        return json

    def parse_error(self, payload):
        error = self.json_lib.loads(payload)
        if 'error' in error.keys():
            return error['error']
        else:
            if 'message' in error.keys():
                return error['message']
            else:
                return error['errors']


class ModelParser(JSONParser):

    def __init__(self, model_factory=None):
        JSONParser.__init__(self)
        self.model_factory = model_factory or ModelFactory

    def parse(self, method, payload):
        try:
            if method.payload_type is None:
                return
            model = getattr(self.model_factory, method.payload_type)
        except AttributeError:
            raise IdeaScalyError('No model for this payload type: %s' % method.payload_type)

        json = JSONParser.parse(self, method, payload)

        if method.payload_list:
            result = model.parse_list(method.api, json)
        else:
            result = model.parse(method.api, json)

        return result
