Here is the code for the file "anti_spam.py" in the specified file structure:

```python
import discord
from discord.ext import commands

class AntiSpam(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.spam_count = {}

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        author_id = str(message.author.id)
        if author_id not in self.spam_count:
            self.spam_count[author_id] = 0

        self.spam_count[author_id] += 1

        if self.spam_count[author_id] > 5:
            await message.channel.send(f"{message.author.mention}, please refrain from spamming.")

    @commands.command()
    async def clear_spam_count(self, ctx):
        self.spam_count = {}
        await ctx.send("Spam count has been cleared.")

def setup(bot):
    bot.add_cog(AntiSpam(bot))
```

Explanation:
1. The "AntiSpam" class is defined as a subclass of `commands.Cog` to create a Discord bot cog for anti-spam functionality.
2. The `__init__` method initializes the bot and creates a dictionary to keep track of spam counts for each user.
3. The `on_message` event listener is triggered whenever a message is sent in a server the bot is a part of. It checks if the message author is not the bot itself and increments the spam count for the author.
4. If the spam count exceeds 5, a warning message is sent to the channel asking the author to refrain from spamming.
5. The `clear_spam_count` command allows the bot to clear the spam count dictionary.
6. The `setup` function is used to add the `AntiSpam` cog to the bot.

Note: This code assumes that the Discord bot has already been set up with the `discord.py` library and the cog has been registered with the bot.