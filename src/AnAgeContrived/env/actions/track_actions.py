# Author: Jonah Ada
# Date: March 20th, 2023
# Description: 
# Modules to convert entity & helper module funtions into a Command objects to utilize the Command design pattern
# the actions in this file are related to the sentient & transformative track actions
# the file is commented out in an effort to simplfy the game to more fundemental functions
# to reduce the AI training time. Can be uncommented anytime and all the actions will be automatically added to the action list

# from __future__ import annotations
# # these imports will not be imported in the runtime, it is just to help coding to do type_checking
# from typing import TYPE_CHECKING
# if TYPE_CHECKING:
#     from env.entities.player import Player
#     from env.engine import Engine
#     pass

# from env.command import Command
# from env.entities.energy import Energy

# action_family_1 = "Transformative Track"
# action_family_2 = "Sentient Track"

# class BindEnergySentientTrack(Command):

#     def __init__(self, player: Player, engine: Engine):
#         super().__init__(player, engine)
#         self.action = action_family_2
#         self.action_details = "Bind Energy"

#     def execute(self):
#         energy = self.player.exhausted_energies[Energy.SINGLE].pop()
#         self.player.sentient_track.bind_energy(energy)

#     def check(self) -> bool:
#         return self.player.sentient_track.is_bind_sentient_track_legal(self.engine)
    
# class AdvanceSentientTrack(Command):

#     def __init__(self, player: Player, engine: Engine):
#         super().__init__(player, engine)
#         self.action = action_family_2
#         self.action_details = "Advance Sentient Track"

#     def execute(self):
#         self.player.sentient_track.advance_energy(self.engine)

#     def check(self) -> bool:
#         return self.player.sentient_track.is_advance_sentient_track_legal(self.engine)
    
# class BindEnergyTransformativeTrack(Command):

#     def __init__(self, player: Player, engine: Engine):
#         super().__init__(player, engine)
#         self.action = action_family_1
#         self.action_details = "Bind Energy"

#     def execute(self):
#         energy = self.player.exhausted_energies[Energy.SINGLE].pop()
#         self.player.transformative_track.bind_energy(energy)

#     def check(self) -> bool:
#         return self.player.transformative_track.is_bind_transformative_track_legal(self.engine)
    
# class AdvanceTransformativeTrack(Command):

#     def __init__(self, player: Player, engine: Engine):
#         super().__init__(player, engine)
#         self.action = action_family_1
#         self.action_details = "Advance Transformative Track"

#     def execute(self):
#         self.player.transformative_track.advance_energy(self.engine)

#     def check(self) -> bool:
#         return self.player.transformative_track.is_advance_transformative_track_legal(self.engine)