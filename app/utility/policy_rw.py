import json
import time

from app.simulator.policy import Action


def save_policy(policy_table: list[Action], custom_filename: str = None):
    filename = custom_filename or f'policy_{int(time.time())}.json'
    with open(filename, 'w') as outfile:
        json.dump(policy_table, outfile)


def load_policy(filename: str) -> list[Action]:
    with open(filename) as json_file:
        return json.load(json_file)
