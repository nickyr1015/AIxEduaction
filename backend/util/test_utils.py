import os
import sys
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from config.configuration import get_config
from model.database_connection import DatabaseConnection
from util.writer import *


if __name__ == "__main__":
    config = get_config()
    path_output = config["base_dir"]+"/backend/data/output/"
    filename = "react.txt"

    db = DatabaseConnection()
    

