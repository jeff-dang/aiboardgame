import os
for module in os.listdir(os.path.dirname(__file__)):
    if module == '__init__.py' or module[-3:] != '.py':
        continue
    __import__(module[:-3], locals(), globals())
del module

# __all__ = [ "Command", "ConveyCommand"]

#method 3
# from os.path import dirname, basename, isfile, join
# import glob
# modules = glob.glob(join(dirname(__file__), "*.py"))
# __all__ = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]


#method 1
# from inspect import isclass
# from pkgutil import iter_modules
# from pathlib import Path
# import os
# from importlib import import_module

# # iterate through the modules in the current package
# #package_dir = Path(__file__).resolve().parent #original
# package_dir = os.listdir('.')
# # for (_, module_name, _) in iter_modules([package_dir]): #original
# for (_, module_name, _) in iter_modules(package_dir):

#     # import the module and iterate through its attributes
#     module = import_module(f"{__name__}.{module_name}")
#     for attribute_name in dir(module):
#         attribute = getattr(module, attribute_name)

#         if isclass(attribute):            
#             # Add the class to this package's variables
#             globals()[attribute_name] = attribute

#method 2
# # all = ['command', 'conveyCommand']