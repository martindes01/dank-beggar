# dank-beggar

## About

This project is an entertaining personal test of the browser automation features of the [selenium](https://pypi.org/project/selenium/) package, and the scheduling and multi-processing features of the Python language.
It is not intended to be taken seriously.

The documentation of the Python implementation of Selenium WebDriver can be found at https://selenium-python.readthedocs.io/.

## Disclaimer

:warning: **DO NOT use these scripts without first reading and understanding the [Terms of Service](https://dankmemer.lol/terms) and [Rules](https://dankmemer.lol/rules) of the Dank Memer Discord bot.** :warning:

## Pre-requisites

* It is assumed that you have already

  1. created a [Discord](https://discordapp.com/) account, and
  1. created a test server with at least one text channel on Discord.

  You may also wish to add the [Dank Memer](https://dankmemer.lol/) bot to the test server.
  However, note that the bot does not need to be present in order to observe the selenium and Python features that are tested in this project.
  In fact, it is recommended that you do not use the Dank Memer bot when testing these scripts (see [Disclaimer](#disclaimer)).

* [Python 3.6 or greater](https://www.python.org/downloads/) is required to use these scripts.

* Currently, this project uses the [Google Chrome](https://www.google.com/chrome/) interface of Selenium WebDriver.
  Hence, you will need to have the Google Chrome web browser installed on your system.

  If you wish to use an alternative browser, refer to the [selenium-python](https://selenium-python.readthedocs.io/) documentation.
  You will need to redefine the `__init__` method of the `Discordapp` class in [discordapp.py](discordapp.py).

## Installation

1. In your working directory, clone this repository.
   ```bash
   $ git clone https://github.com/martindes01/dank-beggar
   ```

1. Create and activate a virtual environment.
   ```bash
   $ python3 -m venv myenv
   $ source myenv/Scripts/activate
   ```

1. Install the packages listed in [requirements.txt](requirements.txt).
   ```bash
   (myenv) $ pip install -r requirements.txt
   ```

1. Download the version of [ChromeDriver](https://chromedriver.chromium.org/home) that corresponds to your version of Google Chrome.
   1. In Google Chrome, navigate to [chrome://version/](chrome://version/) and note the version number.
   2. Download the correct version of ChromeDriver from https://chromedriver.chromium.org/downloads.
   3. Either add the ChromeDriver executable to your system path or place it in your working directory.

   With some changes to the code, other web browsers and drivers are available (see [Pre-requisites](#pre-requisites)).

## Usage

### Parameters

Parameter | Definition | Default value
--- | --- | :---:
`max_retries: int` | Maximum number of times to retry a failed process that requires web driver navigation |
`timeout: int` | Number of seconds to wait for web driver page load or redirect | `10`
`delay: float` | Number of seconds to wait for bot reply between sending messages | `0.5`
`css_selector: str` | CSS selector for Discord web app message box | `'.slateTextArea-1Mkdgw'` [*](#footnote-a)
`prefix: str` | Dank Memer Discord bot command prefix | `'pls'`
`recipient: str` | Username or server nickname of primary account for coin sharing | `''`

<span id="footnote-a">*</span> CSS selector correct as of version `Stable 57334 (b1437cc)` of the Discord web app (released 10/03/2020).

### Method 1 ([dank_beggar.py](dank_beggar.py))

Run [dank_beggar.py](dank_beggar.py) from the command line and follow the prompts.
```bash
$ python3 dank_beggar.py
```

You will need
* the email and password of your Discord account, and
* the full URL of the text channel in your Discord test server.

### Method 2 ([example.py](example.py))

#### Notice

The [example.py](example.py) script is provided for the convenience of those who may wish to run [dank_beggar.py](dank_beggar.py) multiple times without the need to repeat each prompt.
Note, however, that this requires saving your Discord password as a string in the script.

Therefore, please observe the following advice.

* :warning: **DO NOT use this method if you are using a public computer or if there is a possibility that anyone else could access your files.** :warning:

* :warning: **It is recommended that you rename [example.py](example.py) to `personal_test.py` and make sure that the file has been added to your [.gitignore](.gitignore).** :warning:

#### Definition

Each account is defined as a tuple of `(email, password)` in the `accounts` list.

Additional accounts can be used to accrue and deposit coins (Dank Memer currency) into the primary account.
To enable this, the username or server nickname of the primary account must be defined in the `recipient` string, and the `'recipient': recipient` keyword argument of the `kwargs` dictionary must be uncommented.

The full URL of the `dank-memer` channel of your test server must be defined in the `server_channel_url` string.

Assuming you have renamed [example.py](example.py) to `personal_test.py` (and made sure that the file has been added to your [.gitignore](.gitignore)) as recommended in [Notice](#notice), you can now run the script as follows.
```bash
$ python3 personal_test.py
```

All parameters listed in [Parameters](#parameters) can be altered.
`max_retries` is the first positional argument of the `args` tuple.
The remaining parameters are keyword arguments defined in the `kwargs` dictionary.

## License

This project is licensed under the terms of the [MIT license](LICENSE).
