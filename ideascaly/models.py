# IdeaScaly
# Copyright 2015 Jorge Saldivar
# See LICENSE for details.

from ideascaly.utils import parse_datetime


class Model(object):

    def __init__(self, api=None):
        self._api = api

    def __getstate__(self):
        # pickle
        pickle = dict(self.__dict__)
        try:
            del pickle['_api']  # do not pickle the API reference
        except KeyError:
            pass
        return pickle

    @classmethod
    def parse(cls, api, json):
        """Parse a JSON object into a model instance."""
        raise NotImplementedError

    @classmethod
    def parse_list(cls, api, json_list):
        """
            Parse a list of JSON objects into
            a result set of model instances.
        """
        results = []
        for json_obj in json_list:
            if json_obj:
                obj = cls.parse(api, json_obj)
                results.append(obj)

        return results

    def __repr__(self):
        state = ['%s=%s' % (k, repr(v)) for (k, v) in vars(self).items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(state))


class Author(Model):

    @classmethod
    def parse(cls, api, json):
        author = cls(api)
        setattr(author, '_json', json)

        for k, v in json.items():
            setattr(author, k, v)

        return author

    @classmethod
    def parse_list(cls, api, json_list):
        if isinstance(json_list, list):
            item_list = json_list
        else:
            item_list = json_list['authors']

        results = []
        for obj in item_list:
            results.append(cls.parse(api, obj))

        return results


class Campaign(Model):

    @classmethod
    def parse(cls, api, json):
        campaign = cls(api)
        setattr(campaign, '_json', json)

        for k, v in json.items():
            setattr(campaign, k, v)

        return campaign


class Idea(Model):

    @classmethod
    def parse(cls, api, json):
        idea = cls(api)
        setattr(idea, '_json', json)

        for k, v in json.items():
            if k == 'authorInfo':
                author_model = getattr(api.parser.model_factory, 'author') if api else Author
                author = author_model.parse(api, v)
                setattr(idea, k, author)
            elif k == 'creationDateTime':
                setattr(idea, k, parse_datetime(v))
            elif k == 'editedAt':
                setattr(idea, k, parse_datetime(v))
            elif k == 'statusChangeDate':
                setattr(idea, k, parse_datetime(v))
            elif k == 'tags':
                tags = []
                for tag in v:
                    tags.append(tag)
                setattr(idea, k, tags)
            else:
                setattr(idea, k, v)

        return idea


class Vote(Model):

    @classmethod
    def parse(cls, api, json):
        vote = cls(api)
        setattr(vote, '_json', json)

        for k, v in json.items():
            if k == 'creationDate':
                setattr(vote, k, parse_datetime(v))
            else:
                setattr(vote, k, v)

        return vote


class Comment(Model):

    @classmethod
    def parse(cls, api, json):
        comment = cls(api)
        setattr(comment, '_json', json)

        for k, v in json.items():
            if k == 'authorInfo':
                author_model = getattr(api.parser.model_factory, 'author') if api else Author
                author = author_model.parse(api, v)
                setattr(comment, k, author)
            elif k == 'creationDateTime':
                setattr(comment, k, parse_datetime(v))
            elif k == 'editedAt':
                setattr(comment, k, parse_datetime(v))
            elif k == 'statusChangeDate':
                setattr(comment, k, parse_datetime(v))
            elif k == 'tags':
                tags = []
                for tag in v:
                    tags.append(tag)
                setattr(comment, k, tags)
            else:
                setattr(comment, k, v)

        return comment


class JSONModel(Model):

    @classmethod
    def parse(cls, api, json):
        return json


class ModelFactory(object):
    """
    Used by parsers for creating instances
    of models.
    """

    campaign = Campaign
    author = Author
    idea = Idea
    vote = Vote
    comment = Comment
    json = JSONModel
