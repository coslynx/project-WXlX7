Here is the complete code for the file discord-moderation-bot/src/features/word_filter.py:

```python
import discord
from discord.ext import commands

class WordFilter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if self.is_inappropriate(message.content):
            await message.delete()
            await message.channel.send(f"{message.author.mention}, please refrain from using inappropriate language.")

    def is_inappropriate(self, content):
        # Add your logic to check for inappropriate words here
        return False

def setup(bot):
    bot.add_cog(WordFilter(bot))
```

Explanation:
- The code includes the necessary imports for discord and discord.ext libraries.
- The `WordFilter` class is defined as a subclass of `commands.Cog`, which allows it to be used as a cog in the discord bot.
- The `__init__` method initializes the WordFilter cog with the bot instance.
- The `on_message` method is a listener that triggers whenever a new message is sent in any channel the bot has access to. It checks if the message contains inappropriate language using the `is_inappropriate` method, and deletes the message if necessary.
- The `is_inappropriate` method is a placeholder for your logic to check if a message contains inappropriate words. You can replace the `return False` statement with your own implementation.
- The `setup` function is required by the discord.py library to set up the WordFilter cog.

Please note that this code is just a starting point and the `is_inappropriate` method needs to be implemented with your own logic to check for inappropriate words.