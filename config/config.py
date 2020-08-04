import discord
from typing import Dict


class Config():

    def __init__(self, config_file : str):
        self.config_dict = self.load_config(config_file)

    def load_config(self, config_file : str):
        file = open(config_file)
        try :
            config_dict = self.load_commander_role(file.readline())
        finally:
            file.close()

        return config_dict

    def load_commander_role(self, commander : str):
        temp = commander.rstrip().split(":")
        config_dict = {temp[0] : temp[1]}
        return config_dict
    
config = Config("config/config.txt")
print(config.config_dict["commander"])