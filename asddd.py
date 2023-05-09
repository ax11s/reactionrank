import discord
from discord.ext import commands
import json



bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_reaction_add(reaction, user):
    message = reaction.message
    recipient_id = message.author.id
    recipient = await bot.fetch_user(recipient_id)
    print(f"{user.id} added a reaction to a message sent by {recipient.id}, he reacted with {reaction} username: {bot.get_user(user.id)}")
    
    with open("data.json", "r") as f:
        data = json.load(f)

    if str(user.id) in data:
        print('Record already exists!')

        #not sure if this code is works
        for d in data:
            if str(reaction) in data[str(user.id)]:
                exists = True
                olddata = data[str(user.id)][str(reaction)]
                newdata = int(olddata) + 1
                data[str(user.id)][str(reaction)] = newdata
            else:
                data[str(user.id)][str(reaction)] = str(1)

        with open('data.json', 'w') as f:
                json.dump(data, f)

    else:
        print('Record not found')
        data[user.id] = {
            str(reaction): str(1)
        }
        with open('data.json', 'w') as f:
            json.dump(data, f)





@bot.command()
async def stats(ctx, *, name):
    with open("data.json", "r") as f:
        data = json.load(f)

    if ctx in data:
        print('Record found!')
        print(name)
        output = ""
        for d in data:
            if name.id in d:
                output += f"{name.id}: {d[name.id]}, "
                await ctx.send(f'{bot.get_user(name.id)} has the following reactions: {output}')
            
    else:
        print('Record not found')
    



#for sending the emoji from unicode

#emoji_str = "\ud83d\udc80"
#emoji = discord.PartialEmoji.from_unicode(emoji_str)





bot.run("MTEwNTIwNDI5MTcxNjc4MDExMw.GtscM5.7uxYm_i-fzgJG9C1IqcTzefKQK2GmCHb3Cr6JY")