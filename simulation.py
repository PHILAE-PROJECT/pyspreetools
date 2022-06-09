from pyspree.SpreeAPIManager import SpreeAPIManager
from pyspree.UserSimulator import UserSimulator
import argparse
parser = argparse.ArgumentParser(description='Simulation program')
parser.add_argument("-c", "--config_filepath", help="config filepath", default="./config/config_file_local.json")
args = parser.parse_args()
sam=SpreeAPIManager(config_file_path=args.config_filepath)
for i in range(2):
    u=UserSimulator(sam)
    u.start_navigation()
    print(u.abstract_trace)