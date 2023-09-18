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

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
    
    @tree.command(name = "about", description = "Prints about info for daodelightful")
    async def about(interaction):
        await interaction.response.send_message("""Hello, I'm Daodelightful! I'm a Dao De Jing quotations bot created by viridianskies! Simply say 'ddj chapter x' with x being the number of the chapter you want! You can also use the /chapter command!""")

    @tree.command(name = "chapter", description = "Prints requested Daodejing chapter")
    async def chapterreq(interaction, chapter: int):
        response = responses.hanresp(int(chapter))
        await interaction.response.send_message(response)
    
    @client.event
    async def on_ready():
        await tree.sync()
        print("Ready!")
    client.run(TOKEN)
