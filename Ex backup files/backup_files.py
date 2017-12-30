"""
This script backup the important files specified int the config.json.

@author: kenneth.shu
"""

import json
import os
import time
import zipfile

# read the configuration file in json format
with open('/Users/kenneth.shu/dev/Python/PythonStudy/Ex backup files/config.json') as config_file:
    config_entries = json.load(config_file)
    files_to_backup = config_entries['important_files']
    backup_folder_path = config_entries['backup_folder']

# check whether the backup path exists
if not os.path.exists(backup_folder_path):
    os.mkdir(backup_folder_path)

# backup zip file name is the current timestamp
datetime_format = '%Y%m%d%H%M%S'
zip_file_name = time.strftime(datetime_format) + ".zip"

# add all the specified files in the config file to the backup zip file
backup_file_name = backup_folder_path + os.sep + zip_file_name

with zipfile.ZipFile(backup_file_name, 'x') as backup_file:
    for file_name in files_to_backup:
        backup_file.write(file_name)
