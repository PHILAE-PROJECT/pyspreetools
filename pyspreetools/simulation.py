from .replay.pyspree.SpreeAPIManager import SpreeAPIManager
from .replay.pyspree.UserSimulator import UserSimulator
# import argparse
# parser = argparse.ArgumentParser(description='Simulation program')
# parser.add_argument("-c", "--config_filepath", help="config filepath", default="./config/config_file_local.json")
# args = parser.parse_args()


def simulation(config_dict=None,number_of_sessions=2):
    if config_dict is None:
        config_dict = {
            "base_url": "https://demo.spreecommerce.org/",
            "logging": True,
            "log_file": "./logs/log.json",
            "test_mode": True,
            "verbose": False,
            "sleep_time": 0.2
        }
    sam = SpreeAPIManager(config_dict=config_dict)
    for i in range(number_of_sessions):
        u=UserSimulator(sam)
        u.start_navigation()
