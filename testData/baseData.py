import os

from utilities.config import *


def getUrl():
    config = getConfig()
    url = config['url']['url']
    return url


def getProjectPath():
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Get the project root (one level up from the script)
    project_path = os.path.abspath(os.path.join(script_directory, '..'))

    return project_path
