import ConfigParser
from ideascaly.auth import AuthNonSSO
from ideascaly.api import API

config = ConfigParser.ConfigParser()
config.read('config')

community = config.get('example','community_url')
token = config.get('example','token')
idea_id = 139718  # Replace with yours
myfile = 'pic.jpg'  # Replace with yours


# ---
# Attach a file to an idea
#
# Required parameters
# 'ideaId': integer of the id of the idea to which the file will be attached
# 'filename': string indicating the name of the file to be attached
#
# ---
def attach_file_idea(api):
    ret = api.attach_file_to_idea(filename=myfile,ideaId=idea_id)
    print('The file {} was attached to the idea with id {}'.format(myfile, ret.id))


if __name__ == '__main__':
    auth = AuthNonSSO(token)
    api = API(auth)
    api.community_url = community
    attach_file_idea(api)
