from batman.sample_config import Config


class Development(Config):
    OWNER_ID = 254318997  # my telegram ID
    OWNER_USERNAME = "i_am_an_princes"  # my telegram username
    API_KEY = "your bot api key"  # my api key, as provided by the botfather
    DB_URI = 'mysql80-afe9.euw2.cloud.ametnes.com'  # sample db credentials
    MESSAGE_DUMP = '-1004567890' # some group chat that your bot is a member of
    USE_MESSAGE_DUMP = True
    SUDO_USERS = [18673980, 83489514]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['sed']
    AI_API_KEY = "AI_API_KEY get from coffeehouse.intellivoid.net" #ai api key by intellivoid
    INFOPIC = True
    WHITELIST_USERS = 
    STRICT_GMUTE = True  
    STRICT_GBAN = True
    WORKERS = 6
    URL = https://batman-robot.herokuapp.com/
    ENV = ANYTHING
    PORT = 8443
    SUPPORT_USERS = #A space separated list of user IDs who you wanna assign as support users(gban perms only).
