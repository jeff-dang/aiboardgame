from functools import partial

def action1(energyType):
    print('Energy release is: ' + energyType)

def action2(energyType):
    print('Energy gained is: ' + energyType)

actions = [partial(action1, 'type 1'), partial(action2,'type 2')]

actions[0]()
actions[1]()
print('ended')

# # --- First Aim ---
# #Main Action Class
# #Conveying - Inherits from the action class
# #Releasing Energy - Inherits from the action class
# #Bulding the Monuments - Inherits from the action class
# #Selecting the first 3 cards for the conveyer - Inherits from the action class
# #Game Engine - 
# #Game Board - 
# #Transmuter - 
# # --- Later Goals ---
# #Moving on the map
# #Character class - class for each 5 char (dragon etc.)