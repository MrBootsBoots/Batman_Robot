from batman.sample_config import Config


class Development(Config):
    OWNER_ID = 1180249738  # my telegram ID
    OWNER_USERNAME = "i_am_an_princes"  # my telegram username
    API_KEY = "your bot api key"  # my api key, as provided by the botfather
    DB_URI = 'mysql80-afe9.euw2.cloud.ametnes.com'  # sample db credentials
    MESSAGE_DUMP = '-1001410340369' # some group chat that your bot is a member of
    USE_MESSAGE_DUMP = True
    SUDO_USERS = [18673980, 83489514]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['sed']
    AI_API_KEY = '4d12b1129a21dcd4d828b128bd28df83253865a8b9c8b0926037db9614720118d88b5082deed4afd444abb26e581cef44ab840e613dcd14aa358a7185895c9b3' #ai api key by intellivoid
    INFOPIC = True
    WHITELIST_USERS = 
    STRICT_GMUTE = True  
    STRICT_GBAN = True
    WORKERS = 6
    URL = https://batman-robot.herokuapp.com/
    ENV = ANYTHING
    PORT = 8443
    SUPPORT_USERS = #A space separated list of user IDs who you wanna assign as support users(gban perms only).
