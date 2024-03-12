from environs import Env
from dataclasses import dataclass

@dataclass
class TelegramBot:
    token: str
    admin: int


@dataclass
class Config:
    telegram_bot: TelegramBot


def add_config():
    env = Env()
    env.read_env()

    return Config(
        telegram_bot=TelegramBot(
            token=env('BOT_TOKEN'),
            admin=env.int('ADMIN')
        )
    )