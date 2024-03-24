# https://github.com/Infamous-Hydra/YaeMiko
# https://github.com/Team-ProjectCodeX


class Config(object):
    # Configuration class for the bot

    # Enable or disable logging
    LOGGER = True

    # <================================================ REQUIRED ======================================================>
    # Telegram API configuration
    API_ID = 6433468  # Get this value from my.telegram.org/apps
    API_HASH = "7895dfd061f656367ccab30032"

    # Database configuration (PostgreSQL)
    DATABASE_URL = "postgres://ierjlkr:OG4dxzO67Zret3Zii43Hhvujkg89WVry0n9KsHE@karma.db.elephantsql.com/ierjlkr"

    # Event logs chat ID and message dump chat ID
    EVENT_LOGS = -1002044251414
    MESSAGE_DUMP = -1002044251414

    # MongoDB configuration
    MONGO_DB_URI = "mongodb+srv://t45:t45@cluster0.plfylpo.mongodb.net/?retryWrites=true&w=majority"

    # Support chat and support ID
    SUPPORT_CHAT = "https://t.me/Zero_Two_Support96"
    SUPPORT_ID = -1002044251414

    # Database name
    DB_NAME = "MikoDB"

    # Bot token
    TOKEN = "6826048528:AAFlu77TQlrl2zPEhKZ_IrwAe95ZyLu0nOg"  # Get bot token from @BotFather on Telegram

    # Owner's Telegram user ID (Must be an integer)
    OWNER_ID = 6924654187
    # <=======================================================================================================>

    # <================================================ OPTIONAL ======================================================>
    # Optional configuration fields

    # List of groups to blacklist
    BL_CHATS = []

    # User IDs of sudo users, dev users, support users, tiger users, and whitelist users
    DRAGONS = []  # Sudo users
    DEV_USERS = []  # Dev users
    DEMONS = []  # Support users
    TIGERS = []  # Tiger users
    WOLVES = []  # Whitelist users

    # Toggle features
    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True

    # Modules to load or exclude
    LOAD = []
    NO_LOAD = []

    # Global ban settings
    STRICT_GBAN = True

    # Temporary download directory
    TEMP_DOWNLOAD_DIRECTORY = "./"
    # <=======================================================================================================>


# <=======================================================================================================>


class Production(Config):
    # Production configuration (inherits from Config)

    # Enable or disable logging
    LOGGER = True


class Development(Config):
    # Development configuration (inherits from Config)

    # Enable or disable logging
    LOGGER = True
