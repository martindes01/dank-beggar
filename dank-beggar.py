from discordapp import Discordapp

import getpass, sched, time


# Create Discordapp object
d = Discordapp()

# Create scheduler
s = sched.scheduler(time.time, time.sleep)


def beg(seconds):
    # Gamble 1 coin every 10 sconds to increase bank capacity
    d.send('pls gamble 1')

    # Deposit and beg every 60 seconds
    if seconds == 60:
        # Deposit coins
        d.send('pls deposit max')
        # Beg for coins
        d.send('pls beg')
        seconds = 0

    # Repeat
    s.enter(10, 1, beg, argument=(seconds+10,))

def daily():
    # Send daily and weekly commands every hour
    d.send('pls daily')
    d.send('pls weekly')
    s.enter(3600, 2, daily)

def main():
    # Log into Discord
    while True:
        email = input('Enter Discord email address: ')
        password = getpass.getpass('Enter Discord password (hidden): ')
        if d.login(email, password):
            # Break loop if login successful
            print(f'Logged in as {email}.')
            break
        else:
            print('Incorrect email or password. Try again.')

    while True:
        url = input('Enter URL of server channel: ')
        if d.load(url):
            # Break loop if load successful
            print(f'Loaded server channel {url}.')
            break
        else:
            print('Invalid URL. Try again.')

    # Schedule messages and run
    print('Begging like a little baby...')
    print('Ctrl + C to quit.')

    beg(60)
    daily()

    s.run()


if __name__ == '__main__':
    main()
