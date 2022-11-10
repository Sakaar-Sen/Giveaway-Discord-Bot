import discord
from discord.ext import commands
import random
import asyncio
import datetime


intents = discord.Intents.all()
# intents.members = True

client = commands.Bot(command_prefix='.', intents=intents)



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))



@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.guild == None:
        return

    if message.content.startswith("!lottery"):
            emoji = "👻"
            #celeb_emoji = ("🎊", "🎀", "🎉")
            celeb_emoji = "🎀"

            
            try:
                pause_time_list = list(message.content.split())
                pause_time = pause_time_list[1]
                pause_time = int(pause_time)
            except:
                pause_time = 1
                
            epoch_timestamp = (datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=pause_time)).timestamp()
            
            epoch_timestamp = int(epoch_timestamp)
           
            msg1 = await message.channel.send(
                '{1} **GIVEAWAY!** {1} \n\nEnding <t:{2}:R> \n\nReact with {0} to participate'.format(emoji,
                                                                                                           celeb_emoji,
                                                                                                           epoch_timestamp))
            await msg1.add_reaction(emoji)

            pause_time = pause_time * 60

            await asyncio.sleep(pause_time)

            cache_msg = discord.utils.get(client.cached_messages, id=msg1.id)
           # print(msg1.id)

            reaction = cache_msg.reactions
            
            users = []
            for i in reaction:
                async for user in i.users():
                    users.append(user)


            winnerpicked = False

            for i in range(50):
                winner = random.choice(users)
                if winner.id != client.user.id:
                    winnerpicked = True
                    break

            if winnerpicked:
                await cache_msg.reply('The winner is <@{}>! 🥳'.format(winner.id))
            else:
                await cache_msg.reply("There was no winner :/")

            await cache_msg.edit(
                content="{1} **GIVEAWAY!** {1} \n\nThe giveaway has now ended. \n\nReact with {0} to participate".format(
                    emoji, celeb_emoji, epoch_timestamp))





client.run("BOT_TOKEN_HERE")