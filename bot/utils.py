from datetime import datetime
from dateutil import tz

channel_id = 940044789980725298
whitelist_roles = ["Lab Head"]

tzstr = "EST"
tz = tz.gettz(tzstr)
def now():
  return datetime.now(tz)
 
def get_authorised_users():
  return ["Bunyod#0503","sergexzx#4287", "_.jasmine._#0051"]
