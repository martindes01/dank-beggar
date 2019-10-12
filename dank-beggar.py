from discordapp import Discordapp

import getpass, random, sched, time


# Postmeme types
meme_types = [
    'd',
    'e',
    'm',
    'n',
    'r',
]

# Spam interval
spam_interval = 15

# Create Discordapp object
d = Discordapp()

# Create random number generator
r = random.SystemRandom()

# Create scheduler
s = sched.scheduler(time.time, time.sleep)


def spam(seconds):
    # Gamble 1 coin every spam interval to increase bank capacity
    d.send('pls gamble 1')

    # Deposit and beg every minute
    if not seconds % 60:
        d.send('pls deposit max')
        d.send('pls beg')

    # Postmeme every 2 minutes
    if not seconds % 120:
        d.send('pls postmeme')
        d.send(r.choice(meme_types))

    # Daily and weekly every hour
    if not seconds % 3600:
        d.send('pls daily')
        d.send('pls weekly')
        # Reset seconds
        seconds = 0

    # Repeat
    s.enter(spam_interval, 1, spam, argument=(seconds+spam_interval,))

def main():
    # Set timing attributes for Discordapp object
    try:
        d.timeout = max(d.timeout, int(input(f'\nEnter web driver timeout in seconds (default minimum {d.timeout}): ')))
    except:
        pass
    try:
        d.delay = max(d.delay, float(input(f'Enter delay for bot response in seconds (default minimum {d.delay}): ')))
    except:
        pass

    # Set spam interval (must be factor of 60)
    try:
        global spam_interval
        spam_interval = 60 / min(6, max(1, int(input(f'Enter number of gambles per minute (1 ~ 6, default {60 // spam_interval}): '))))
    except:
        pass

    # Log into Discord
    while True:
        email = input('\nEnter Discord email address: ')
        password = getpass.getpass('Enter Discord password (hidden): ')
        if d.login(email, password):
            # Break loop if login successful
            print(f'Logged in as {email}.')
            break
        else:
            print('Incorrect email or password. Try again.')

    # Load server channel
    while True:
        url = input('\nEnter URL of server channel: ')
        print('Waiting for redirect...')
        if d.load(url):
            # Break loop if load successful
            print(f'Loaded server channel {url}.')
            break
        else:
            print('Invalid URL. Try again.')

    # Schedule messages and run
    print('\nBegging like a little baby...')
    print('Ctrl + C to quit.')
    spam(3600)
    s.run()


if __name__ == '__main__':
    main()
