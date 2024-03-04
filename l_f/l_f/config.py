import json
import dataclasses


with open('../.env.json', 'r') as config:
    conf_dict = json.read(config)


@dataclasses
class Config:
    secret_key: str = conf_dict['SECRET_KEY']
    debug: str = conf_dict['DEBUG']


def get_config():
    config = Config()
    return config


if __name__ == '__main__':
    pass
