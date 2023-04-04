# Author: Jeffrey Dang
# Date: January 29th, 2023
# Description: 
# Script containing functions to output logs to a JSON file

from os import path, mkdir, getcwd
from json import load, dump, dumps
from datetime import datetime

# generates a unique file name based on the time & date
def jsonNamer(folder_name='ai_history'):
    now = datetime.now()
    timestamp = now.strftime("%m_%d_%Y_%H_%M_%S")
    name = folder_name+"/simulation_history_"+timestamp+".json"
    return name

# gets the path that the JSON file will be created in
def jsonDirectory(folder_name='ai_history'):
    cur_directory = getcwd()
    folder_path = path.join(cur_directory, folder_name)
    return folder_path

# writes the logs into the JSON file
def jsonWriter(folder_path, json_name):
    if path.exists(folder_path) != True:
        mkdir(folder_path)
    json_object = dumps([])  # create list
    with open(json_name, "w") as outfile:
        outfile.write(json_object)

# dumps all the JSON output
def jsonDump(simulation_history, json_name):
    with open(json_name) as openjson:
        dictObj = load(openjson)
        dictObj.append(simulation_history)

    with open(json_name, "w") as outfile:
        dump(dictObj, outfile, indent=4)

# generates a human readable list of action space and writes it to a file called allActions.json under ./ai_history folder
def jsonActionConverter(folder_name,action_list):
    action_filename = "allActions.json"
    newActionList = {}
    for i in action_list:
        actionName = i.get('action') + ' ' + i.get('action_details')
        newActionList[actionName] = None
    json_object = dumps(actionName)  # create list
    folder_path = jsonDirectory(folder_name)
    if path.exists(folder_path) != True:
        mkdir(folder_path)
    json_object = dumps(newActionList,indent=4)  # create list
    with open(folder_name+'/'+action_filename, "w") as outfile:
        outfile.write(json_object)
   
    

