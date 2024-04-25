import json
from dataclasses import dataclass


with open('.env.json', 'r') as config:
    conf_dict = json.load(config)


@dataclass
class Config_dj():
    secret_key: str = conf_dict['SECRET_KEY']
    debug: str = conf_dict['DEBUG']
    db_user: str = conf_dict['DJ_DB_USER']
    db_pass: str = conf_dict['DJ_DB_PASS']
    
    conf_dict = conf_dict


def get_config():
    config = Config_dj()
    return config


if __name__ == '__main__':
    pass
