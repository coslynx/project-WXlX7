Here is the complete code for the file discord-moderation-bot/src/features/logging_system.py:

```python
import logging

class LoggingSystem:
    def __init__(self):
        self.logger = self.setup_logger()

    def setup_logger(self):
        logger = logging.getLogger('moderation_logger')
        logger.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        file_handler = logging.FileHandler('logs/moderation_logs.txt')
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

        return logger

    def log_moderation_action(self, action, user, reason):
        log_message = f"Moderation Action: {action} | User: {user} | Reason: {reason}"
        self.logger.info(log_message)
```

Explanation:
The code above defines a LoggingSystem class that handles logging of moderation actions. It uses the logging module from the Python standard library to create a logger named 'moderation_logger'. The logger is configured to log messages at the INFO level and outputs them to a file named 'moderation_logs.txt' located in the 'logs' directory.

The setup_logger method is responsible for setting up the logger with the appropriate configuration. It creates a formatter that specifies the format of the log messages, creates a file handler that specifies the output file, and adds the file handler to the logger.

The log_moderation_action method is used to log a moderation action. It takes the action, user, and reason as parameters and constructs a log message using f-string formatting. The log message includes the action, user, and reason for the moderation action. The logger's info method is called to log the message.

By using this LoggingSystem class, moderation actions can be logged to the 'moderation_logs.txt' file for transparency and accountability.

Dependencies:
- This file depends on the 'logs' directory being present in the project structure.
- The 'logs' directory should contain the 'moderation_logs.txt' file for the logging to work correctly.

Interconnections:
- The LoggingSystem class can be used by other features or commands in the bot that require logging of moderation actions. They can create an instance of the LoggingSystem class and use its log_moderation_action method to log the actions.

Please note that this is the complete code for the logging_system.py file, and it assumes that all the necessary dependencies and imports are included in the other files of the project.