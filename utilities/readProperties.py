import os
import configparser
import sys

config = configparser.RawConfigParser()

ROOT_DIR_PROJECT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

config_file_path = ROOT_DIR_PROJECT + r'\configurations\config.ini'

ROOT_DIR = sys.path[1]

config.read(config_file_path)


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = (config.get('commonInfo' , 'baseURL'))
        return url



