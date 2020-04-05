from discordapp import Discordapp

from dank_memer import DankMemer

import getpass


def main() -> None:
    # Create Discordapp object
    with Discordapp() as discord:
        # Set timing attributes of Discordapp object
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
                print('Incorrect email or password, or connection error. Try again.')

        # Load server channel
        while True:
            url = input('\nEnter URL of server channel: ')
            print('Waiting for redirect...')
            if discord.load(url):
                # Break loop if load successful
                print(f'Loaded server channel.')
                break
            else:
                print('Invalid URL or connection error. Try again.')

        # Set message box CSS selector attribute of Discordapp object
        css_selector = input(f'Enter CSS selector of message box (default {discord.css_selector} correct as of version \'Stable 57334 (b1437cc)\' released 10/03/2020): ').strip()
        if css_selector:
            discord.css_selector = css_selector

        # Create and initialise DankMemer object
        memer = DankMemer(discord)
        prefix = input(f'\nEnter Dank Memer bot prefix (default "{memer.prefix}"): ').strip()
        if prefix:
            memer.prefix = prefix
        memer.recipient = input(f'Enter username or nickname of recipient for sharing (default None): ')

        # Schedule messages and run
        print('\nBegging like a little baby...')
        print('Ctrl + C to quit.')
        memer.run()

def quick_run(
    max_retries,     # type: int
    email,           # type: str
    password,        # type: str
    url,             # type: str
    timeout=0,       # type: int
    delay=0,         # type: float
    css_selector='', # type: str
    prefix='',       # type: str
    recipient='',    # type: str
    ) -> None:
    # Create Discordapp object
    with Discordapp() as discord:
        # Set timing attributes of Discordapp object
        try:
            discord.timeout = max(discord.timeout, timeout)
        except:
            pass
        try:
            discord.delay = max(discord.delay, delay)
        except:
            pass

        # Log into Discord
        for retry in range(max_retries):
            if discord.login(email, password):
                # Break loop if login successful
                print(f'\nLogged in as {email}.')
                break
            else:
                print(f'Login for {email} failed {retry + 1} times. Retrying...')
        else:
            # All retries failed; return
            print(f'Login for {email} failed {max_retries} times. Exiting...')
            return

        # Load server channel
        for retry in range(max_retries):
            if discord.load(url):
                # Break loop if load successful
                break
            else:
                print(f'Server channel load for {email} failed {retry + 1} times. Retrying...')
        else:
            # All retries failed; return
            print(f'Server channel load for {email} failed {max_retries} times. Exiting...')
            return

        # Set message box CSS selector attribute of Discordapp object
        if css_selector:
            discord.css_selector = css_selector

        # Create and initialise DankMemer object
        memer = DankMemer(discord)
        if prefix:
            memer.prefix = prefix
        memer.recipient = recipient

        # Schedule messages and run
        print(f'\n{email} is begging like a little baby...')
        print('Ctrl + C to quit.')
        memer.run()


if __name__ == '__main__':
    main()
