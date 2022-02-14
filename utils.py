from datetime import datetime
from dateutil import tz
import os
channel_id = 942662187669930034
whitelist_roles = [895446805154766918,936281488855552000]

API_HOST = os.getenv("API_HOST")

def get_token():
  token = os.getenv("TOKEN")
  return (token)

tzstr = "EST"
tz = tz.gettz(tzstr)
def now():
  return datetime.now(tz)
 
def get_authorised_users():
  return ["Bunyod#0503","sergexzx#4287"]

admins = [237063450646282241, 849457807518335006]
