from environs import Env
from tgbot.models.enteties import Bot


def load_config(path: str) -> Bot:
    env = Env()
    env.read_env(path)
    return Bot(
        token=env("BOT_TOKEN"),
        name=None,
        url=None,
    )