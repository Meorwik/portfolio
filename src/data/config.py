from dataclasses import dataclass, field
from typing import Final
from os import environ


@dataclass
class RedisConnectionConfig:
    HOST: Final[str] = environ.get("REDIS_JOB_STORE_HOST")
    PORT: Final[int] = int(environ.get("REDIS_JOB_STORE_PORT"))
    PASSWORD: Final[str] = environ.get("REDIS_JOB_STORE_PASSWORD")


@dataclass
class AppConfig:
    POSTGRES_ENGINE: Final[str] = environ.get("POSTGRESQL_ENGINE")
    REDIS_URL: Final[str] = environ.get("REDIS_URL")
    REDIS_JOB_STORE_DATA: Final[RedisConnectionConfig] = field(default_factory=RedisConnectionConfig)

@dataclass
class MetaData:
    CONTACT_US_URL: Final[str] = "https://t.me/n1kol4y"
    MAIN_CHANNEL_URL: Final[str] = "https://t.me/n1kol4y"
    CARD_NUMBER: Final[str] = environ.get("CARD_NUMBER")
    MAX_PIN_DAYS_POSSIBLE: Final[int] = 31



#
