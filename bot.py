# Daodelightful Discord Bot
# Prints out quotations from the Dao De Jing!

import discord
import responses
from discord import app_commands

def rundiscbot():
    TOKEN = 'x'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    tree = app_commands.CommandTree(client)
    
    @tree.command(name = "about", description = "About info for daodelightful")
    async def about(interaction):
        await interaction.response.send_message("""Hello, I'm Daodelightful! I'm a Dao De Jing quotation bot created by viridianskies! You can use the /chapter command with the chapter number you want!""")

    @tree.command(name = "chapter", description = "Prints requested Daodejing chapter")
    async def chapterreq(interaction, chapter: int):
        response = responses.hanresp(int(chapter))
        await interaction.response.send_message(response)
    
    @client.event
    async def on_ready():
        await tree.sync()
        print("Bot is up!")
    client.run(TOKEN)