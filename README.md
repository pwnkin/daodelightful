# Daodelightful Discord Bot

Daodelightful is a Discord bot that provides access to the Dao De Jing text, allowing users to retrieve chapters and verses from this ancient Chinese philosophical text. This README guide will help you get started with Daodelightful.

## Translations Attribution

All of the text within [/translations/](https://codeberg.org/pwnkin/Daodelightful/src/branch/main/translations) is owned by 
the respective owners and is not my work.:

- Gia-Fu Feng & Jane English
- Stephen Mitchell
- Wing Tsit Chan

These translations are used with permission or under the terms specified by the respective licenses provided by the original authors. Please refer to the individual translation files for specific details on licensing and usage.

## Table of Contents

- [Features](#features)
- [Commands](#commands)
- [Setup](#setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- Access specific chapters and verses from the Dao De Jing.
- Retrieve ancient wisdom and philosophical insights from the text.

## Commands

To use Daodelightful, you can use the following command:

- `/about`: Print out about information for the bot.
- `/chapter`: Retrieve a specific chapter from the Dao De Jing by providing its number.
- `/translation`: Print out a list of available translations.

## Setup

To add Daodelightful to your Discord server, follow these steps:

1. **Create a Bot on Discord Developer Portal:**

   - Go to the [Discord Developer Portal](https://discord.com/developers/applications).
   - Create a new application.
   - Under the "Bot" section, create a bot user for your application.

2. **Get Your Bot Token:**

   - In the Bot section of your application on the Developer Portal, you can reveal your bot's token. Copy this token; you will need it later.

3. **Invite Your Bot to Your Server:**

   - In the OAuth2 section of your application on the Developer Portal, generate an OAuth2 URL with the "bot" and "applications.commands" scopes selected.
   - Open this URL in a web browser and select your server to invite the bot.

4. **Configuration:**

   - Clone or download the Daodelightful bot code to your local machine.
   - Find your token for your bot.
   - Edit the following line in the `bot.py` file, replacing `x` with your bot's token:

     ```
     TOKEN = 'x'
     ```


5. **Run the Bot:**

   - Make sure you have Python 3.7 or higher installed.
   - Install the required dependencies by running `pip install discord.py` in your terminal.
   - Run the bot by executing `python main.py` (or the filename of your bot script).

## Usage

After inviting Daodelightful to your server and setting it up, you can use the following command to retrieve chapters from the Dao De Jing:

- To get Chapter X: `/chapter number translation`

Replace `number` with the specific chapter number you want to access, and `translation` with the translation code you want.

## Contributing

If you'd like to contribute to Daodelightful, feel free to fork the repository, make your changes, and submit a pull request. We welcome any improvements, bug fixes, or new features.

## License

This project is licensed under the GNU Affero General Public License v3.0 - see the [LICENSE](LICENSE) file for details.