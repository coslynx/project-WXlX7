Here is the complete code for the file `discord-moderation-bot/src/commands/custom_commands.py`:

```python
import discord

class CustomCommands:
    def __init__(self, client):
        self.client = client
        
    async def execute_custom_command(self, command):
        if command == "!hello":
            await self.say_hello()
        elif command == "!goodbye":
            await self.say_goodbye()
        elif command == "!help":
            await self.send_help_message()
        else:
            await self.client.send_message(command.channel, "Unknown command")
            
    async def say_hello(self):
        await self.client.send_message(command.channel, "Hello!")
        
    async def say_goodbye(self):
        await self.client.send_message(command.channel, "Goodbye!")
        
    async def send_help_message(self):
        help_message = "Available commands:\n" \
                       "!hello - Say hello\n" \
                       "!goodbye - Say goodbye\n" \
                       "!help - Show this help message"
        await self.client.send_message(command.channel, help_message)
```

Explanation:
- The `CustomCommands` class represents the custom commands functionality of the discord moderation bot.
- It has an `__init__` method that takes the `client` as a parameter. The `client` is an instance of the discord bot client.
- The `execute_custom_command` method is responsible for executing the custom commands based on the input command.
- The `say_hello` method sends a "Hello!" message to the channel where the command was executed.
- The `say_goodbye` method sends a "Goodbye!" message to the channel where the command was executed.
- The `send_help_message` method sends a help message to the channel where the command was executed, listing all available commands.
- The `execute_custom_command` method is called when a custom command is detected. It checks the command and calls the respective method to execute the command.
- If the command is unknown, it sends an "Unknown command" message to the channel.

Note: This code assumes that the `command` object is provided as a parameter to the `execute_custom_command` method. Please make sure to pass the correct parameter when calling this method.