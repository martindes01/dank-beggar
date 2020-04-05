# dank-beggar

*A background script to get rich quick in the Dank Memer Discord bot currency system. Beg like a little baby and spam your way to virtual affluence!*

## About

This is a novel exploration of the browser automation features of [Selenium WebDriver](https://www.selenium.dev/documentation/), as well as the scheduling and multiprocessing features of the [Python standard library](https://docs.python.org/3/library/).

This project is compatible with build 57334 (version hash `b1437cc`) of the Discord web application by Discord Inc.
The corresponding changelog is dated 2020-03-10.

## Getting Started

### Prerequisites

It is assumed that you have already created a [Discord](https://discordapp.com/) account and set up a personal test server with at least one text channel.

You may also wish to add the [Dank Memer](https://dankmemer.lol/) Discord bot to the test server.
Note, however, that the bot does not need to be present in order to observe the Selenium and Python features that are explored in this project.
In fact, it is recommended that you do not use the bot in this manner without first reading and understanding its [terms of service](https://dankmemer.lol/terms) and [rules](https://dankmemer.lol/rules).

An installation of [Python](https://www.python.org/) version 3.6 or later is required to run the software.

This project currently uses the Google Chrome interface of Selenium WebDriver.
Therefore, an installation of the [Google Chrome](https://www.google.com/chrome/) web browser is required to run the software.

If you wish to use an alternative interface, refer to the [Selenium documentation](https://www.selenium.dev/documentation/).
You will need to redefine the `__init__` method of the `Discordapp` class in [discordapp.py](discordapp.py).

### Installation

Clone the source from this repository.

```shell
git clone https://github.com/martindes01/dank-beggar.git
cd dank-beggar
```

Create and activate a virtual environment, specifying a suitable path `<path>`.
A common name for the environment directory is `.venv`.

```shell
python3 -m venv <path>
source <path>/Scripts/activate
```

Install the dependencies listed in [requirements.txt](requirements.txt).

```shell
pip install --requirement requirements.txt
```

Download the version of [ChromeDriver](https://chromedriver.chromium.org/) that corresponds to the installed version of Google Chrome.
1. In Google Chrome, navigate to `chrome://version/` and note the version number.
1. Download the corresponding version of ChromeDriver from [here](https://chromedriver.chromium.org/downloads).
1. Add the ChromeDriver executable to the system path or place it in the root directory.

## Usage

### Interactive Mode

To start the process in interactive mode, run the `dank_beggar.py` script and follow the prompts.
You will need the email address and password of your Discord account and the full URL of the target text channel in your personal test server.

```bash
python3 dank_beggar.py
```

### Direct Mode

#### Warning

The [example.py](example.py) script allows the process to be started without prompts.
Note, however, that this requires saving your Discord email address and password as strings in the script.
Therefore, please do not use this method if you are using a public machine or if there is any possibility that someone else could access your files.

#### Create the Script

Create a copy of `example.py` named `personal_test.py`, which already has an entry in `.gitignore`.
The following changes should be made only to `personal_test.py` and not to `example.py` or any other tracked file.

Add your Discord login details to the `accounts` list.
Each account is defined as a tuple of a Discord account email address and the corresponding password.

Additional accounts can be added to the list and used to accrue and deposit coins (Dank Memer currency) into the primary account.
To enable this, set the `recipient` string to the username or server nickname of the primary account, and uncomment the `'recipient': recipient` keyword argument of the `kwargs` dictionary.

Set the `server_channel_url` string to the full URL of the target text channel in your personal test server.

The script starts a new process for each account.
Each process targets the `quick_run` method of `dank_beggar.py`.
The required parameters of the method are defined by position in the `args` tuple.
The optional parameters of the method are defined by keyword in the `kwargs` dictionary.
See the [reference](#reference) for more information.

#### Run the Script

To start the process in direct mode, run the `personal_test.py` script.

```shell
python3 personal_test.py
```

### Reference

#### Required Parameters

Parameter | Definition
--- | ---
`max_retries: int` | Maximum number of times to retry a failed page load
`account: tuple[str, str]` | Tuple of a Discord account email address and the corresponding password
`server_channel_url: str` | Full URL of the target text channel in the Discord server

#### Optional Parameters

Parameter | Definition | Default value
--- | --- | :---:
`timeout: int` | Number of seconds to wait for a page load or redirect | `10`
`delay: float` | Number of seconds to wait for a bot reply between sending messages | `0.5`
`prefix: str` | Dank Memer Discord bot command prefix | `'pls'`
`recipient: str` | Username or server nickname of the primary account for coin sharing | `''`

## License

This project is distributed under the terms of the MIT License.
See [LICENSE](LICENSE) for more information.
