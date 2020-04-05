from discordapp import Discordapp

import random, sched, time


# Base spam interval must be a factor of 60
base_interval = 15

default_prefix = 'pls'
default_recipient = ''

# Postmeme types
meme_types = [
    'd',
    'e',
    'n',
    'r',
]


class DankMemer:
    def __init__(self, discordapp):
        # Assign Discordapp object
        self.discord = discordapp

        # Create random number generator
        self.rand = random.SystemRandom()

        # Create scheduler
        self.schedule = sched.scheduler(time.time, time.sleep)

        # Spam settings
        self.interval = base_interval
        self.prefix = default_prefix
        self.recipient = default_recipient

    def run(self) -> None:
        # Run schedule
        # Start at one hour
        self.spam(3600)
        self.schedule.run()

    def spam(self, seconds: int) -> None:
        # Send 'weekly' command every spam interval to increase bank capacity
        self.discord.send(self.prefix + ' weekly')

        # Send 'deposit' and 'beg' commands every minute
        if not seconds % 60:
            self.discord.send(self.prefix + ' beg')
            self.discord.send(self.prefix + ' deposit max')

        # Send 'postmeme' command every two minutes
        if not seconds % 120:
            self.discord.send(self.prefix + ' postmeme')
            self.discord.send(self.rand.choice(meme_types))

        # Share 1000 coins with recipient every ten minutes if specified
        if self.recipient and not seconds % 600:
            self.discord.send(self.prefix + ' withdraw 1000')
            self.discord.send(self.prefix + ' share ' + self.recipient + ' 1000')

        # Send 'daily' command every hour
        # Schedule may have been started less than 24 hours since last successful claim of daily bonus
        # Sending command hourly increases likelihood that next bonus is claimed before schedule is stopped
        if not seconds % 3600:
            self.discord.send(self.prefix + ' daily')
            # Reset seconds
            seconds = 0

        # Repeat
        self.schedule.enter(self.interval, 1, self.spam, argument=(seconds+self.interval,))
