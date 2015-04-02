import ConfigParser
from ideascaly.auth import AuthNonSSO
from ideascaly.api import API

config = ConfigParser.ConfigParser()
config.read('config')

community = config.get('example','community_url')
token = config.get('example','token')
idea_to_vote_id = 139718  # Replace with yours
idea_to_comment_id = 121848  # Replace with yours


# ---
# Vote up an idea
#
# Required parameters
# 'ideaId': integer of the id of the idea to be removed
#
# Optional parameters
# 'myVote': constant equal to 1 (indicate a positive vote)
# ---
def vote_up_idea(api):
    vote = api.vote_up_idea(ideaId=idea_to_vote_id)
    print('The idea {} was voted (id={}) up!'.format(idea_to_vote_id, vote.id))


# ---
# Vote down an idea
#
# Required parameters
# 'ideaId': integer of the id of the idea to be removed
#
# Optional parameters
# 'myVote': constant equal to -1 (indicate a negative vote)
# ---
def vote_down_idea(api):
    vote = api.vote_down_idea(ideaId=idea_to_vote_id)
    print('The idea {} was voted (id={}) down'.format(idea_to_vote_id, vote.id))


# ---
# Comment an idea
#
# Required parameters
# 'ideaId': integer of the id of the idea to be removed
# 'text': string containing the text of the comment
# ---
def comment_idea(api):
    comment = api.comment_idea(ideaId=idea_to_comment_id, text="This comment was placed from an example code!")
    print('The idea {} was commented (id={})'.format(idea_to_comment_id, comment.id))


if __name__ == '__main__':
    auth = AuthNonSSO(token)
    api = API(auth)
    api.community_url = community
    vote_up_idea(api)
    vote_down_idea(api)
    comment_idea(api)