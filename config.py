from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("29717887", ""))
API_HASH = getenv("dbceb604465fabeb200f43b2fd32770d", "")
BOT_TOKEN = getenv("6038053134:AAF70JiVG5iFbMgLlMfXBlS5IJw5kUez_9Q", None)
BOT_NAME = getenv("MUSICJOSHUA","MUSICJOSHUA")
BOT_USERNAME = getenv("MUSICJOSHUABOT", "")
OWNER_USERNAME = getenv("hubertreal", "")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "AzumanProject")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
START_IMG = getenv("START_IMG", "")
PING_IMG = getenv("PING_IMG", "")
SESSION_NAME = getenv("1BVtsOLABuzhXHd3R3C2E-2tblAkS5JyU0LRHhWhSyTZKtINGe0xLs4YyBiSSBvY0xmdX7pjsjCeMa1Ph6vixYQFJCkkiBC92FfUl3Ls0q97PqKtbkj4uzcLkj_4sByYYbCdoJFWHfwnP4Rbl4V503lPH8EYxFF1eJpliWzGmb5Wrz50wQ6JQ3VGK-pJdfGgGTXqC_FqarH9QqIbKpqy_10BW3Z0sqsXwdSCXUDVJtRCdHAHcfSzZswIKBHRKjEPgpjinQ6zrWWYV5jqp_IjWmRPSytX4Le5CBmNLzuNoknneBokuE0sq5G2mT9ttC2ldlKBNl5ied0ihsuu47uL3Wti1ndQktI0=", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
