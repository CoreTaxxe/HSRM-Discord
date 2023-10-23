import discord
import json
from pathlib import Path
from dataclasses import dataclass
from loguru import logger

credentials_file: Path = Path("credentials.txt")

if not credentials_file.exists():
    logger.error("Credentials File does not exist.")
    raise FileNotFoundError("Credentials Files does not exist.")

with credentials_file.open('r') as file:
    credentials_data: dict[str, str] = json.load(file)
    logger.debug("Loaded credentials.")

intents: discord.Intents = discord.Intents.all()
client: discord.Client = discord.Client(intents=intents)


@dataclass(frozen=True)
class Credentials(object):
    token: str


@client.event
async def on_ready() -> None:
    print(f'We have logged in as {client.user}')


credentials: Credentials = Credentials(token=credentials_data["token"])
client.run(token=credentials.token)
