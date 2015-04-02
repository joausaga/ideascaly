import ConfigParser
from ideascaly.auth import AuthNonSSO
from ideascaly.api import API

config = ConfigParser.ConfigParser()
config.read('config')

community = config.get('example','community_url')
token = config.get('example','token')
campaign_id = 28416  # Replace with yours


# ---
# Create a new idea
#
# Required parameters
# 'title': string with the title of the idea (max 64 characters)
# 'text': string with the body of the idea
# 'campaignId': integer of the id of the campaign under which the idea will be posted
#
# Option parameters
# 'tags': list of words to label the idea
# 'custom fields': dictionary of defined custom fields
# ---
def create_new_idea(api):
    new_idea = api.create_idea(title='IdeaScaly Example', text='This is just an example', campaignId=campaign_id)
    print('The new idea was created successfully, its id is: {}'.format(new_idea.id))
    return new_idea.id


# ---
# Delete an idea
#
# Required parameters
# 'ideaId': integer of the id of the idea to be removed
# ---
def delete_idea(api, idea_id):
    deleted_idea = api.delete_idea(ideaId=idea_id)
    print('The idea {} was successfully removed'.format(deleted_idea.id))

if __name__ == '__main__':
    auth = AuthNonSSO(token)
    api = API(auth)
    api.community_url = community
    new_idea_id = create_new_idea(api)
    delete_idea(api, new_idea_id)



