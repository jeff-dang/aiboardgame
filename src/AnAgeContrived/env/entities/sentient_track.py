# Author: Jonah Ada
# Date: March 20th, 2023
# Description: 
# Module to define the "sentient track" entity of the game
from __future__ import annotations
# these imports will not be imported in the runtime, it is just to help coding to do type_checking
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from env.engine import Engine
    from env.entities.player import Player
    from env.entities.energy import EnergyTile
    
from env.entities.energy import Energy
from env.entities.turn_state import TurnType

# defines the sentient track as an object
class SentientTrack():

    def __init__(self, player: Player):
        self.owner = player
        self.track = [0, 0, 0, 0]
        self.energy_index = None
        self.is_token_enable = False

    # checks whether an energy is binded to sentient track
    def is_energy_binded(self) -> bool:
        if self.energy_index == None:
            return False
        elif self.energy_index >= 0:
            return True
        
    # binds an energy to the sentient track
    def bind_energy(self, energy: EnergyTile):
        if not self.is_energy_binded():
            self.energy_index = 0
            self.track[self.energy_index] = energy
            self.is_token_enable = False

    # advances a binded energy on the sentient track by one tile
    def advance_energy(self, engine: Engine):
        energy = self.track[self.energy_index]
        self.track[self.energy_index] = 0
        if self.energy_index < (len(self.track) - 1):
            self.energy_index += 1
            self.track[self.energy_index] = energy
        elif self.energy_index == (len(self.track) - 1):
            for pillar in engine.pillars_of_civilization:
                if pillar.is_player_in_same_area(self.owner) and not pillar.is_player_present(self.owner):
                    pillar.set_bind_energy(energy)
                    self.energy_index = None 
        self.is_token_enable = False

    # defines the action mask conditions on whether the player can bind an energy to the sentient track
    def is_bind_sentient_track_legal(self, engine: Engine) -> bool:
        if engine.turn.turn_type == TurnType.ACTION_TURN and self.is_token_enable:
            if len(self.owner.exhausted_energies[Energy.SINGLE]) > 0 and not self.owner.sentient_track.is_energy_binded():
                return True
        return False

    # defines the action mask conditions on whether the player can advance his energy on the sentient track
    def is_advance_sentient_track_legal(self, engine: Engine) -> bool:
        if engine.turn.turn_type == TurnType.ACTION_TURN and self.is_token_enable:
            if len(self.owner.exhausted_energies[Energy.SINGLE]) > 0 and self.owner.sentient_track.is_energy_binded():
                return True
        return False