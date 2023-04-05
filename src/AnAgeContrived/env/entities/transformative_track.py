# Author: Jonah Ada
# Date: March 20th, 2023
# Description: 
# Module to define the "transformative track" entity of the game
from __future__ import annotations
# these imports will not be imported in the runtime, it is just to help coding to do type_checking
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from env.engine import Engine
    from env.entities.player import Player
    from env.entities.energy import EnergyTile
    
from env.entities.energy import Energy
from env.entities.turn_state import TurnType

# defines the transformative track as an object
class TransformativeTrack():

    def __init__(self, player: Player):
        self.owner = player
        self.track = [0, 0, 0, 0]
        self.energy_index = None
        self.is_token_enable = False

    # checks whether an energy is binded to transformative track
    def is_energy_binded(self) -> bool:
        if self.energy_index == None:
            return False
        elif self.energy_index >= 0:
            return True
        
    # binds an energy to the transformative track
    def bind_energy(self, energy: EnergyTile):
        if not self.is_energy_binded():
            self.energy_index = 0
            self.track[self.energy_index] = energy
            self.is_token_enable = False
            
    # advances a binded energy on the transformative track by one tile
    def advance_energy(self, engine: Engine):
        energy = self.track[self.energy_index]
        self.track[self.energy_index] = 0
        if self.energy_index < (len(self.track) - 1):
            self.energy_index += 1
            self.track[self.energy_index] = energy
        elif self.energy_index == (len(self.track) - 1):
            engine.monuments[engine.monument_index].binded_energies.append(energy)
            self.energy_index = None 
        self.is_token_enable = False

    # defines the action mask conditions on whether the player can bind an energy to the transformative track
    def is_bind_transformative_track_legal(self, engine: Engine) -> bool:
        if engine.turn.turn_type == TurnType.ACTION_TURN and self.is_token_enable:
            if len(self.owner.exhausted_energies[Energy.SINGLE]) > 0 and not self.owner.transformative_track.is_energy_binded():
                return True
        return False

    # defines the action mask conditions on whether the player can advance his energy on the transformative track
    def is_advance_transformative_track_legal(self, engine: Engine) -> bool:
        if engine.turn.turn_type == TurnType.ACTION_TURN and self.is_token_enable:
            if len(self.owner.exhausted_energies[Energy.SINGLE]) > 0 and self.owner.transformative_track.is_energy_binded():
                return True
        return False
