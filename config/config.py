import discord
from typing import Dict


class Config():

    def __init__(self, config_file : str, shop_file : str):
        self.config_dict = self.load_config(config_file)
        self.shop_dict = self.load_shop(shop_file)

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

    def load_shop(self, shop_file : str):
        file = open(shop_file)
        shop_dict = {}
        try:
            for line in file:
                parts = line.rstrip().split(":")
                shop_dict[parts[0]] = int(parts[1])
        finally:
            file.close()
            return shop_dict
    
config = Config("config/config.txt", "config/shop.txt")