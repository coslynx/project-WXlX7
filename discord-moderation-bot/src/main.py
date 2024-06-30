import discord
from discord.ext import commands
import logging

# Import other files
from src.commands.automated_mod_commands import AutomatedModCommands
from src.commands.moderation_actions import ModerationActions
from src.commands.role_commands import RoleCommands
from src.commands.custom_commands import CustomCommands
from src.features.logging_system import LoggingSystem
from src.features.scheduled_messages import ScheduledMessages
from src.features.anti_spam import AntiSpam
from src.features.word_filter import WordFilter
from src.features.user_reputation_system import UserReputationSystem
from src.integrations.third_party_bots import ThirdPartyBots
from src.integrations.ai_moderation import AIModeration
from src.utils.helper_functions import HelperFunctions

# Set up logging
logging.basicConfig(filename='logs/moderation_logs.txt', level=logging.INFO)

# Load environment variables from .env file
load_dotenv()

# Create instance of Discord bot
bot = commands.Bot(command_prefix='!')

# Initialize features and commands
automated_mod_commands = AutomatedModCommands(bot)
moderation_actions = ModerationActions(bot)
role_commands = RoleCommands(bot)
custom_commands = CustomCommands(bot)
logging_system = LoggingSystem(bot)
scheduled_messages = ScheduledMessages(bot)
anti_spam = AntiSpam(bot)
word_filter = WordFilter(bot)
user_reputation_system = UserReputationSystem(bot)
third_party_bots = ThirdPartyBots(bot)
ai_moderation = AIModeration(bot)
helper_functions = HelperFunctions()

# Bot events
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    print('------')

# Run the bot
bot.run(TOKEN)