## Description
The Discord Lottery Bot is a Python-based bot designed to host giveaways in Discord servers. The bot uses the Discord.py library to create and manage the lottery. It allows users/admins to initiate a giveaway by typing "!lottery" in the server, and then the bot announces the giveaway with a set duration. Users can react to the giveaway message with a designated emoji to participate.

# Key Features:

1. Giveaway Setup: 
Users initiate a giveaway by typing "!lottery" followed by the desired duration (in minutes) as a command in the server. eg !lottery 10 (winner will be picked after 10 minutes)
2. Duration Control:
  The bot calculates the end time of the giveaway based on the specified duration and displays the end time in a user-friendly format.
4. Participation: Users react to the giveaway message with a specific emoji (e.g., "👻") to enter the giveaway.
5. Winner Selection: Once the giveaway duration ends, the bot randomly selects a winner from the participants who reacted to the giveaway message with the designated emoji.
6. Winner Announcement: The bot announces the winner by tagging them in a reply to the giveaway message. 
7. Emoji Customization: The bot allows customization of emojis used for the giveaway and winner celebration.

# Images

<img src="./UI/img1.png" alt="1">
<img src="./UI/img2.png" alt="1">


# Usage
The bot requires a Discord bot token ("BOT_TOKEN_HERE") to run. Users should replace this placeholder with their actual bot token to use the bot in their Discord server.




