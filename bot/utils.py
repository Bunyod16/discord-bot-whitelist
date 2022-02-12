from datetime import datetime
from dateutil import tz

channel_id = 940045123994136646
whitelist_roles = ["Whitelist_role"]

tzstr = "EST"
tz = tz.gettz(tzstr)
def now():
  return datetime.now(tz)
 
def get_authorised_users():
  return ["Bunyod#0503","sergexzx#4287", "_.jasmine._#0051"]

admins = [237063450646282241, 849457807518335006]
