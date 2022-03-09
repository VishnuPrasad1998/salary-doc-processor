import os
from typing import List, Type

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    CONFIG_NAME = "base"
    DEBUG = False

class DevelopmentConfig(BaseConfig):
    CONFIG_NAME = "dev"
    DEBUG = True
    SECRET_KEY = os.getenv(
        "DEV_SECRET_KEY", "You can't see me"
    )
    MONGO_URI = "mongodb://localhost:27017/DocsDB?readPreference=primary&appname=MongoDB%20Compass&ssl=false"


EXPORT_CONFIGS: List[Type[BaseConfig]] = [
    DevelopmentConfig
]

config_by_name = {cfg.CONFIG_NAME: cfg for cfg in EXPORT_CONFIGS}

