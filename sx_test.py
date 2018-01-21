"""
This is a test script file for Python
@author: kenneth.shu
Created in 2017 Dec.
"""

import test_module_2

print("Invoke saySth function.")
test_module_2.saySth()

# this is a tes of the walk function
# basically the dirs and files are filled with all the diretionaries and files under the root
import os
for root, dirs, files in os.walk("/Users/kenneth.shu/dev/Python/PythonStudy/Ex backup files/file_folder"):
    for aDir in dirs:
        print(root + "*" + aDir)
    for fn in files:
        print(root + '|' + fn)
        #absfn = os.path.join(root, fn)
        #zfn = absfn[len(path2zip)+len(os.sep):] #XXX: relative path
        #zipfile.write(absfn, zfn)

# see how the os.path.split function works
os.path.split("/Users/kenneth.shu/dev/Python/PythonStudy/Ex backup files/file_folder/1.txt")

# see how the multiple vars in the for statement works
for a, b in ((1, 2), (3, 4), (5, 6), (99, 100)):
    print(str(a) + "|" + str(b))
