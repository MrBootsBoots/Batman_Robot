from batman.sample_config import Config


class Development(Config):
    OWNER_ID = 1180249738  # my telegram ID
    OWNER_USERNAME = "i_am_an_princes"  # telegram username
    API_KEY = "your bot api key"  # my api key, as provided by the botfather
    DB_URI = 'mysql80-afe9.euw2.cloud.ametnes.com'  # cloud/ametness/com
    MESSAGE_DUMP = '-1001410340369' # some group chat that your bot is a member of
    USE_MESSAGE_DUMP = True
    SUDO_USERS = [1358136299, 784606914, 1368562787, 1229419906]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['sed']
    AI_API_KEY = '4d12b1129a21dcd4d828b128bd28df83253865a8b9c8b0926037db9614720118d88b5082deed4afd444abb26e581cef44ab840e613dcd14aa358a7185895c9b3' #ai api key by intellivoid
    INFOPIC = True
    WHITELIST_USERS = [1229419906, 1358136299, 784606914, 1368562787] #Users Cannot be banned via your bot.
    STRICT_GMUTE = True  
    STRICT_GBAN = True
    WORKERS = 6
    URL = https://batman-robot.herokuapp.com/
    ENV = ANYTHING
    PORT = 8443
    SUPPORT_USERS = 1399308798 # A space separated list of user IDs who you wanna assign as support users(gban perms only).
    ALLOW_EXCL = True
    SUPPORT_CHAT = DragonAssociationSupport
    WALL_API = 
