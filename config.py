from batman.sample_config import Config


class Development(Config):
    OWNER_ID = 254318997  # my telegram ID
    OWNER_USERNAME = "i_am_an_princes"  # my telegram username
    API_KEY = "your bot api key"  # my api key, as provided by the botfather
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost:5432/database'  # sample db credentials
    MESSAGE_DUMP = '-1004567890' # some group chat that your bot is a member of
    USE_MESSAGE_DUMP = True
    SUDO_USERS = [18673980, 83489514]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation']
    AI_API_KEY = "AI_API_KEY get from coffeehouse.intellivoid.net" #ai api key by intellivoid
    INFOPIC = True
    WHITELIST_USERS = 
    
