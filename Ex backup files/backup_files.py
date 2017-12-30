"""
This script backup the important files specified int the config.json.

@author: kenneth.shu
"""

import json
import os
import time
import zipfile

# zip all the files in a folder
def zipdir(path2zip, zipfile):
    assert os.path.isdir(path2zip)
    upperpath = os.path.abspath(path2zip + os.sep + "..")
    #print("upperpath:" + upperpath)

    for root, dirs, files in os.walk(path2zip):
        for dirn in dirs:
            absdirn = os.path.join(root, dirn)
            zdirn = absdirn[len(upperpath)+len(os.sep):] #XXX: relative path
            #print("**" + absdirn + "*" + zdirn)
            zipfile.write(absdirn, zdirn)
        for fn in files:
            absfn = os.path.join(root, fn)
            zfn = absfn[len(upperpath)+len(os.sep):] #XXX: relative path
            #print("||" + absfn + "|" + zfn)
            zipfile.write(absfn, zfn)


# read the configuration file in json format
with open('/Users/kenneth.shu/dev/Python/PythonStudy/Ex backup files/config.json') as config_file:
    config_entries = json.load(config_file)
    files_to_backup = config_entries['important_files']
    backup_folder_path = config_entries['backup_folder']


# create the backup folder
date_format = '%Y%m%d'
backup_folder_path = backup_folder_path + os.sep + time.strftime(date_format)

if not os.path.exists(backup_folder_path):
    os.mkdir(backup_folder_path)

# get the comment of the backup and prepare the zip file name
comment = input('Please input the backup comment: ')
time_format = '%H%M%S'
if len(comment) == 0:
    zip_file_name = time.strftime(time_format) + ".zip"
else:
    zip_file_name = time.strftime(time_format) + "_" + comment.replace(' ', '_') + ".zip"

# add all the specified files in the config file to the backup zip file
backup_file_name = backup_folder_path + os.sep + zip_file_name

with zipfile.ZipFile(backup_file_name, 'x') as backup_file:
    for file_name in files_to_backup:
        if os.path.isdir(file_name):
            zipdir(file_name, backup_file)
        else:
            backup_file.write(file_name, os.path.basename(file_name))

backup_file.close()

print('Files backup successfully.')

# show the backup folder
#ls_command = 'ls -l -R "' + backup_folder_path + os.sep + '.."'
#os.system(ls_command)
