import ConfigParser
from ideascaly.auth import AuthNonSSO
from ideascaly.api import API

config = ConfigParser.ConfigParser()
config.read('config')

community = config.get('example','community_url')
token = config.get('example','token')
member_id = 119793  # Replace with yours
img_file_name = 'pic.jpg'


# ---
# Create a new member
#
# Required parameters
# 'name': string containing the new member's name
# 'email': string containing the new member's email address
#
# Optional parameters
# 'silent': boolean indicating whether the creation of the member should be made without sending a verification email
# ---
def create_new_member(api):
    new_member = api.create_new_member(name="ideascaly_example", email="ideascaly-example@xyz.info")
    print('A new member with the id {} was created'.format(new_member.id))


# ---
# Get existing member's email address
#
# Required parameters
# 'memberId': integer containing the id of the member
# ---
def get_member_email(api):
    member = api.get_member_info_by_id(memberId=member_id)
    print('The member with the id {} has the email address {}'.format(member_id, member.email))


# ---
# Attach an image as a member's avatar
#
# Required parameters
# 'memberId': integer containing the id of the member
# 'filename': string containing the name of the file to attach
# ---
def attach_avatar_member(api):
    img = api.attach_avatar_to_member(filename=img_file_name, memberId=member_id)
    print('The avatar was successfully attached, the url of the attached image is {}'.format(img['url']))


if __name__ == '__main__':
    auth = AuthNonSSO(token)
    api = API(auth)
    api.community_url = community
    create_new_member(api)
    get_member_email(api)
    attach_avatar_member(api)

