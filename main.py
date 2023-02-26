import asyncio
import json

import aiohttp
import discord
from discord.ext import tasks

BASE_URL = 'https://testflight.apple.com/join/'

last_state = True


@tasks.loop(minutes=10)
async def check_loop(config: dict):
    print('Checking...')
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{BASE_URL}{config["beta_code"]}') as response:
            if response.status != 200:
                print('Failed to get page with status code: ', response.status)
                return
            text = await response.text()
            beta_full = 'This beta is full.' in text
            global last_state
            if beta_full == last_state:
                return
            webhook = discord.Webhook.from_url(config['webhook_url'], session=session)
            await webhook.send(config['full_message'] if beta_full else config['available_message'])
            last_state = beta_full


async def main():
    config = json.load(open('config.json'))
    check_loop.change_interval(seconds=config['check_interval'])
    await check_loop.start(config)


if __name__ == '__main__':
    asyncio.run(main())
