from pyspreetools.simulation import simulation

config_dict = {
    "base_url": "https://demo.spreecommerce.org/",
    "logging": True,
    "log_file": "./logs/log.json",
    "test_mode": True,
    "verbose": False,
    "sleep_time": 0.2
}

simulation(config_dict=config_dict,number_of_sessions=2)