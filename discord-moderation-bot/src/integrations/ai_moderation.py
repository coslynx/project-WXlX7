import discord
from discord.ext import commands
from google.cloud import language_v1

# Load environment variables
load_dotenv()

# Create a client for Google Cloud Natural Language API
client = language_v1.LanguageServiceClient()

class AIModeration(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        # Check if the message is sent by a bot
        if message.author.bot:
            return

        # Analyze the message using Google Cloud Natural Language API
        document = language_v1.Document(content=message.content, type_=language_v1.Document.Type.PLAIN_TEXT)
        response = client.analyze_sentiment(request={'document': document})
        sentiment_score = response.document_sentiment.score

        # Perform moderation actions based on the sentiment score
        if sentiment_score < -0.5:
            await message.delete()
            await message.channel.send(f"{message.author.mention}, your message has been deleted due to its negative sentiment.")
        elif sentiment_score < 0:
            await message.add_reaction("👎")
        elif sentiment_score > 0.5:
            await message.add_reaction("👍")

def setup(bot):
    bot.add_cog(AIModeration(bot))