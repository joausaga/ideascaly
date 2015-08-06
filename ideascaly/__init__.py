# IdeaScaly
# Copyright 2015 Jorge Saldivar
# See LICENSE for details.

"""
IdeaScaly: IdeaScale API client
"""

__version__ = '1.0'
__author__ = 'Jorge Saldivar'
__license__ = 'MIT'

from ideascaly.api import API
from ideascaly.auth import AuthNonSSO, AuthNonSSOMem, AuthSSO, AuthResearch
from ideascaly.error import IdeaScalyError
from ideascaly.models import Author, Idea, Campaign, Comment, Vote, JSONModel, ModelFactory, Model
from ideascaly.parsers import Parser, RawParser, JSONParser, ModelParser
