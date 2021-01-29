if not __name__.endswith("sample_config"):
    import sys
    print("The README is there to be read. Extend this sample config to a config file, don't just rename and change "
          "values here. Doing that WILL backfire on you.\nBot quitting.", file=sys.stderr)
    quit(1)


# Create a new config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = "1585695572:AAGxOtT82b-KLoYaQYFq6qBvFo7aR-EuCCc"
    OWNER_ID = "1180249738" # If you dont know, run the bot and do /id in your private chat with it
    OWNER_USERNAME = "I_Am_An_PRINCES"

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 'sqldbtype://username:pw@hostname:port/db_name'  # needed for any database modules
    MESSAGE_DUMP = '-1001410340369'  # needed to make sure 'save from' messages persist
    LOAD = []
    NO_LOAD = ['translation', 'rss']
    WEBHOOK = False
    URL = 'https://batman-robot.herokuapp.com'

    # OPTIONAL
    SUDO_USERS = []  # List of id's (not usernames) for users which have sudo access to the bot.
    SUPPORT_USERS = []  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = []  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = False  # Whether or not you should delete "blue text must click" commands
    STRICT_GBAN = False
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = 'CAADAgADOwADPPEcAXkko5EB3YGYAg'  # banhammer marie sticker
    ALLOW_EXCL = True  # Allow ! commands as well as /
    STRICT_GMUTE = True
    STRICT_GBAN = True
    WALL_API = '75de53c034d94bba532321b4fcbb4943'
    AI_API_KEY = '4d12b1129a21dcd4d828b128bd28df83253865a8b9c8b0926037db9614720118d88b5082deed4afd444abb26e581cef44ab840e613dcd14aa358a7185895c9b3'

class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
