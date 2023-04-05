# Author: Jonah Ada
# Date: January 10th, 2023
# Description: 
# imports all the modules in env/actions folder to auto generate the action space
import os

for module in os.listdir(os.path.dirname('env/actions/.')):
    #print('looking for the module: ', module)
    if module == '__init__.py' or module[-3:] != '.py':
        continue
    __import__(module[:-3], globals=globals(), level=1)
del module