from discordapp import Discordapp

from dank_memer import DankMemer

import getpass


def main() -> None:
    # Create Discordapp object
    with Discordapp() as discord:
        # Set timing attributes for Discordapp object
        try:
            discord.timeout = max(discord.timeout, int(input(f'\nEnter web driver timeout in seconds (default minimum {discord.timeout}): ')))
        except:
            pass
        try:
            discord.delay = max(discord.delay, float(input(f'Enter delay for bot response in seconds (default minimum {discord.delay}): ')))
        except:
            pass

        # Log into Discord
        while True:
            email = input('\nEnter Discord email address: ')
            password = getpass.getpass('Enter Discord password (hidden): ')
            if discord.login(email, password):
                # Break loop if login successful
                print(f'Logged in as {email}.')
                break
            else:
                print('Incorrect email or password. Try again.')

        # Load server channel
        while True:
            url = input('\nEnter URL of server channel: ')
            print('Waiting for redirect...')
            if discord.load(url):
                # Break loop if load successful
                print(f'Loaded server channel.')
                break
            else:
                print('Invalid URL. Try again.')

        # Create and initialise DankMemer object
        memer = DankMemer(discord)
        prefix = input(f'\nEnter Dank Memer bot prefix (default "{memer.prefix}"): ')
        if prefix:
            memer.prefix = prefix
        memer.recipient = input(f'Enter username or nickname of recipient for sharing (default None): ')

        # Schedule messages and run
        print('\nBegging like a little baby...')
        print('Ctrl + C to quit.')
        memer.run()


if __name__ == '__main__':
    main()
