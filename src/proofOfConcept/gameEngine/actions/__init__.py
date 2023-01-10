import os
import importlib
for module in os.listdir(os.path.dirname('gameEngine/actions/.')):
    #print('looking for the module: ', module)
    if module == '__init__.py' or module[-3:] != '.py':
        continue
    __import__(module[:-3], globals=globals(), level=1)
del module