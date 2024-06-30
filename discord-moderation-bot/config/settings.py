import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    def __init__(self):
        self.token = os.getenv('DISCORD_TOKEN')
        self.prefix = os.getenv('BOT_PREFIX')
        self.mute_role = os.getenv('MUTE_ROLE')
        self.log_channel = os.getenv('LOG_CHANNEL')
        self.reputation_system_enabled = os.getenv('REPUTATION_SYSTEM_ENABLED')
        self.ai_moderation_enabled = os.getenv('AI_MODERATION_ENABLED')
        self.google_cloud_api_key = os.getenv('GOOGLE_CLOUD_API_KEY')

settings = Settings()