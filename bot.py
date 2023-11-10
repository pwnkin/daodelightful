# Daodelightful Discord Bot, Prints out quotations from the Dao De Jing!
"""
Copyright (C) 2023-2023 pwnkin and contributors

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""


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
        await interaction.response.send_message("""Hello, I'm Daodelightful! I'm a Dao De Jing quotation bot created by pwnkin! You can use the /chapter command with the chapter number you want!""")  # noqa

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
