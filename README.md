# Testflight Discord Hook
This is a simple webhook for Discord that allows you to post Testflight updates to a Discord channel.
It sends a message once beta spots are available, and once the beta is full again.

## Installation
1. Install the latest Python Version from [python.org](https://www.python.org/downloads/)
2. Clone this repository
3. Open the Terminal and navigate to the folder where you cloned the repository
4. Run `pip install -r requirements.txt` to install the required packages
5. Fill in the config in `config.json`
6. Run `python main.py` to start the script

## Config
`check_interval`: The interval in seconds to check for changes\
`beta_code`: The code of the beta you want to check. This code is visible in the URL of the Testflight page. e.g. Spotify got `1SyedSId`\
`webhook_url`: The URL of the webhook you want to post to. You can create a webhook in the Discord channel settings.\
`available_message`: The message to post when spots are available. You can include mentions to receive notifications\
`full_message`: The message to post when the beta is full again.

## Docker
You can also run this script in a Docker container. To do so, follow these steps:
1. Install Docker
2. Clone this repository
3. Adjust the config in `config.json`. Alternatively, you can also mount a config file into the container.
4. Run `docker build -t testflight-checker .` to build the image

