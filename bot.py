# Daodelightful Discord Bot
# Prints out quotations from the Dao De Jing!


# imports
import discord
import responses
from discord import app_commands


def rundiscbot():
    TOKEN = 'x' # noqa
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    tree = app_commands.CommandTree(client)

    @tree.command(name="about", description="About info for daodelightful")
    async def about(interaction):
        await interaction.response.send_message("""Hello, I'm Daodelightful! I'm a Dao De Jing quotation bot created by viridianskies! You can use the /chapter command with the chapter number you want!""")  # noqa

    @tree.command(name="chapter", description="Prints requested chapter")
    async def chapterreq(interaction, chapter: int, translation: str):
        response = responses.hanresp(int(chapter), translation)
        await interaction.response.send_message(response)

    @tree.command(name="translations", description="Lists the current available translations.")  # noqa: E501
    async def translist(interaction):
        await interaction.response.send_message("""Available translations:\n
    - (sm) - Stephen Mitchell\n
    - (gia) - Gia-Fu Feng\n
    - (wtc) - Wing-Tsit Chan\n""")

    @client.event
    async def on_ready():
        await tree.sync()
        print("\33[32mBot is up!\033[0m")
    client.run(TOKEN)
