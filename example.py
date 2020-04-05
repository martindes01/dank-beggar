from dank_beggar import quick_run

from multiprocessing import Process

import time


accounts = [
    (
        'user1@email.com',
        'user1password',
    ),
    # (
    #     'user2@email.com',
    #     'user2password',
    # ),
]

# recipient = 'user1'

server_channel_url = 'https://discordapp.com/channels/000000000000000000/000000000000000000'


if __name__ == '__main__':
    print('Commencing stupidity...')
    print('Spam Ctrl + C to quit.')

    # Create list for processes
    processes = []

    # Call dank_beggar.quick_run for each account
    for account in accounts:
        # Specify required positional arguments (max_retries: int, email: str, password: str, url: str)
        args = (5,) + account + (server_channel_url,)

        # Specify optional keyword arguments (timeout: int, delay: float, css_selector: str, prefix: str, recipient: str)
        # The default value of each argument is shown
        kwargs = {
            # 'timeout': 10,
            # 'delay': 0.5,
            # 'css_selector': '.slateTextArea-1Mkdgw',
            # 'prefix': 'pls',
            # 'recipient': recipient,
        }

        # Start process
        p = Process(target=quick_run, args=args, kwargs=kwargs)
        p.start()

        # Save process
        processes.append(p)

        # Delay before creating next process
        time.sleep(5)

    # Wait for processes to end
    for p in processes:
        p.join()
