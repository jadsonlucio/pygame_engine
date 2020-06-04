import os
import warnings
import logging
import logging.config
import yaml
from ..settings import ENVIRONMENT

logging_env = {
    "dev": "dev.yaml",
    "prod": "prod.yaml"
}

base_path = os.path.dirname(__file__)

def get_logging_config_path():
    return f"{base_path}/configs"


def init():
    if ENVIRONMENT in logging_env:
        logging_file_path = os.path.join(get_logging_config_path(), logging_env[ENVIRONMENT])
        with open(logging_file_path, "r") as f:
            log_cfg = yaml.safe_load(f.read())
            logging.config.dictConfig(log_cfg)
    else:
        warnings.warn(f"Environment logging: {ENVIRONMENT} not set, all of logging" \
                      f" informations will be outputed in default logging system")
