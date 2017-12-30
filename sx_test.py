"""
This is a test script file for Python
@author: kenneth.shu
Created in 2017 Dec.
"""

import test_module_2

print("This is a test Python scripts file created by Kenneth.")
print(dir())
print("Invoke saySth function.")
test_module_2.saySth()

#the new print command line
print("Let's start a new branch for development of new features")


import os
for root, dirs, files in os.walk("/Users/kenneth.shu/dev/Python/PythonStudy/Ex backup files/file_folder"):
    for aDir in dirs:
        print(root + "*" + aDir)
    for fn in files:
        print(root + '|' + fn)
        #absfn = os.path.join(root, fn)
        #zfn = absfn[len(path2zip)+len(os.sep):] #XXX: relative path
        #zipfile.write(absfn, zfn)

os.path.split("/Users/kenneth.shu/dev/Python/PythonStudy/Ex backup files/file_folder/1.txt")

for a, b in ((1, 2), (3, 4)):
    print(str(a) + "|" + str(b))
