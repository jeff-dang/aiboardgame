from __future__ import annotations
# these imports will not be imported in the runtime, it is just to help coding to do type_checking
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # from env.entities.player import Player
    # from env.entities.energy import EnergyTile
    pass

from env.entities.turn_state import TurnState, TurnType
from env.entities.player import Player
from env.entities.map import Map
from env.entities.monument import Monument
from env.entities.monument_wall import MonumentWall
from env.action_initiater import get_actions
from env.states import States
import env.helpers.constants as constants
from env.entities.energy import EnergyTile, Energy
from env.entities.map_data import MapAreas
from env.helpers.logger import Logger
from env.victorypoints import VictoryPoints
from env.helpers.turn import Turn


class Engine:
    def __init__(self):
        self.turn_counter: int = 0
        self.action_counter: int = 0
        self.game: int = 1
        self.map: Map = Map()
        self.current_player: int = 0
        self.player_turn_queue: list = []
        self.players: list[Player] = []
        self.turn: TurnState = TurnState()
        self.monument_index: int = 0
        self.is_initialized: bool = False
        self.pillars_of_civilization = constants.PILLARS_OF_CIVILIZATION

        monument_a = Monument(
            "THE ANFIRIEN BEACON",
            MapAreas.PLAINS,
            [
                MonumentWall(
                    [Energy.SINGLE, Energy.SINGLE, Energy.SINGLE],
                    [Energy.SINGLE, Energy.SINGLE],
                ),
                MonumentWall(
                    [Energy.SINGLE, Energy.SINGLE, Energy.SINGLE],
                    [Energy.SINGLE],
                ),
                MonumentWall(
                    [Energy.SINGLE, Energy.SINGLE, Energy.SINGLE],
                    [Energy.SINGLE],
                ),
                MonumentWall([Energy.SINGLE, Energy.SINGLE], [Energy.SINGLE]),
            ],
        )

        monument_b = Monument(
            "THE LIBRARY OF VALDUIN",
            MapAreas.PLAINS,
            [
                MonumentWall(
                    [Energy.SINGLE, Energy.SINGLE, Energy.SINGLE],
                    [Energy.SINGLE, Energy.SINGLE],
                ),
                MonumentWall(
                    [Energy.SINGLE, Energy.SINGLE, Energy.SINGLE],
                    [Energy.SINGLE],
                ),
                MonumentWall(
                    [Energy.SINGLE, Energy.SINGLE, Energy.SINGLE],
                    [Energy.SINGLE],
                ),
                MonumentWall([Energy.SINGLE, Energy.SINGLE], [Energy.SINGLE]),
            ],
        )

        monument_c = Monument(
            "THE ERIDONIC GATE",
            MapAreas.PLAINS,
            [
                MonumentWall(
                    [Energy.SINGLE, Energy.SINGLE, Energy.SINGLE],
                    [Energy.SINGLE, Energy.SINGLE],
                ),
                MonumentWall(
                    [Energy.SINGLE, Energy.SINGLE, Energy.SINGLE],
                    [Energy.SINGLE],
                ),
                MonumentWall(
                    [Energy.SINGLE, Energy.SINGLE, Energy.SINGLE],
                    [Energy.SINGLE],
                ),
                MonumentWall([Energy.SINGLE, Energy.SINGLE], [Energy.SINGLE]),
            ],
        )

        monument_d = Monument(
            "THE NAMARILLION FORGE",
            MapAreas.PLAINS,
            [
                MonumentWall(
                    [Energy.SINGLE, Energy.SINGLE, Energy.SINGLE],
                    [Energy.SINGLE, Energy.SINGLE],
                ),
                MonumentWall(
                    [Energy.SINGLE, Energy.SINGLE, Energy.SINGLE],
                    [Energy.SINGLE],
                ),
                MonumentWall(
                    [Energy.SINGLE, Energy.SINGLE, Energy.SINGLE],
                    [Energy.SINGLE],
                ),
                MonumentWall([Energy.SINGLE, Energy.SINGLE], [Energy.SINGLE]),
            ],
        )

        monument_e = Monument(
            "THE FORTRESS OF KOLYM THRIN",
            MapAreas.PLAINS,
            [
                MonumentWall(
                    [Energy.SINGLE, Energy.SINGLE, Energy.SINGLE],
                    [Energy.SINGLE, Energy.SINGLE],
                ),
                MonumentWall(
                    [Energy.SINGLE, Energy.SINGLE, Energy.SINGLE],
                    [Energy.SINGLE],
                ),
                MonumentWall(
                    [Energy.SINGLE, Energy.SINGLE],
                    [Energy.SINGLE],
                ),
                MonumentWall(
                    [Energy.SINGLE, Energy.SINGLE, Energy.SINGLE],
                    [Energy.SINGLE],
                ),
                MonumentWall([Energy.SINGLE, Energy.SINGLE], [Energy.SINGLE]),
            ],
        )

        monument_f = Monument(
            "THE SHIP OF TOLINTHRA",
            MapAreas.PLAINS,
            [
                MonumentWall(
                    [Energy.SINGLE, Energy.SINGLE, Energy.SINGLE],
                    [Energy.SINGLE, Energy.SINGLE],
                ),
                MonumentWall(
                    [Energy.SINGLE, Energy.SINGLE, Energy.SINGLE],
                    [Energy.SINGLE],
                ),
                MonumentWall(
                    [Energy.SINGLE, Energy.SINGLE, Energy.SINGLE],
                    [Energy.SINGLE],
                ),
                MonumentWall([Energy.SINGLE, Energy.SINGLE], [Energy.SINGLE]),
            ],
        )

        self.monuments: list[Monument] = [
            monument_a,
            monument_b,
            monument_c,
            monument_d,
            monument_e,
            monument_f,
        ]

        for i in range(len(constants.CHARACTER_NAMES)):
            self.players.append(
                Player(
                    constants.AGENT_NAMES[i],
                    constants.CHARACTER_NAMES[i],
                    self.map.starting_positions[i],
                )
            )

        Logger.log(
            "New monument index is:" + str(self.monument_index), "INITIALIZATION_LOGS"
        )
        current_monument: Monument = self.monuments[self.monument_index]

    def check_over(self):
        if self._check_if_last_wall_filled():
            Logger.log("MONUMENTS ALL BUILT", "GAME_ENGINE_LOGS")
            return True
        if (
            self.turn_counter == constants.MAX_TURNS
            or self.action_counter == constants.MAX_TURNS * 10
        ):
            Logger.log("MAX MOVES REACHED", "GAME_ENGINE_LOGS")
            return True

        return False

    def reset(self):
        self.__init__()

    def get_agents(self) -> list[str]:
        return constants.AGENT_NAMES

    def get_action_names(self) -> list[dict[str, str]]:
        actions = get_actions(self.players[self.current_player], self)
        action_names: list[dict[str, str]] = []
        for i, a in enumerate(actions):
            action_names.append(
                {"index": i, "action": a.action, "action_details": a.action_details}
            )
        return action_names

    def get_action_index(self, name):
        list = self.get_action_names()
        index = -1
        for action in list:
            if name in action["action_details"]:
                index = action["index"]
                break
        return index

    def get_legal_action_names(self, agent_name: str) -> list[str]:
        actions = get_actions(self.get_agent(agent_name), self)
        legal_actions: list[str] = []
        for i, action in enumerate(actions):
            if action.check():
                legal_actions.append(
                    str(i) + ": " + action.action + " " + action.action_details
                )
        return legal_actions

    def get_characters(self) -> list[str]:
        return constants.CHARACTER_NAMES

    def get_agent(self, name: str) -> Player:
        for player in self.players:
            if player.get_player_name() == name:
                return player

    # Gets number of total actions
    def get_action_space(self) -> int:
        return constants.NUM_MOVES

    def get_legal_actions(self, agent_name: str):
        actions = get_actions(self.get_agent(agent_name), self)
        legal_actions = []
        for action in actions:
            is_legal = action.check()
            legal_actions.append(is_legal)
        if sum(legal_actions) == 0:
            index = self.get_action_index("End Turn")
            legal_actions[index] = 1
        return legal_actions

    def play_turn(self, agent_name: str, action):
        agent: Player = self.get_agent(agent_name)

        # checks whether the player transmuters are initialized. Starts initialization if necessary
        if not self.is_initialized:
            self.turn.update_turn_type(TurnType.INITIALIZATION_TURN)
            if agent.check_is_initialized():
                self.turn.update_turn_type(TurnType.END_TURN)
                Turn.end_turn(self)
            num_initialized = 0
            for i in self.players:
                if i.is_initialized:
                    num_initialized += 1
            if num_initialized == 5:
                self.is_initialized = True
                self.turn.update_turn_type(None)

        # checks whether the action is legal or not
        if not self.get_legal_actions(self.get_agents()[self.current_player])[action]:
            Logger.log("ILLEGAL MOVE, is" + str(action), "GAME_ENGINE_LOGS")
            return False

        actions = get_actions(self.players[self.current_player], self)
        Logger.log(str(self.get_legal_action_names(agent_name)), "GAME_ENGINE_LOGS")
        Logger.log(
            "EXECUTING ACTION " + str(actions[action].action), "GAME_ENGINE_LOGS"
        )

        actions[action].execute()

        # check whether the monument wall is filled and either:
        # 1: start a mini turn for players who have energy tiles on the wall or
        # 2: end the game if all the walls of all the monuments are filled
        # for monument in self.monuments: #TODO: Later convert to this condition
        for i in range(0, 6):
            monument = self.monuments[i]
            if monument.is_top_wall_completed():
                filled_wall: MonumentWall = monument.get_top_wall()
                if filled_wall.is_reward_given == False:
                    if(self.turn.can_build_bridge):
                        self.turn.update_turn_type(TurnType.BUILD_BRIDGE_TURN)
                    else:
                        self.turn.update_turn_type(TurnType.ACTION_TURN)
                    Logger.log("Build Bridge Turn", "GAME_ENGINE_LOGS")
                    players_contributed = []
                    for energy in filled_wall.filled_sections:
                        players_contributed.append(energy.owner)
                        unique_players_contributed = set(
                            players_contributed
                        )  # only rewards once if player contributed multiple times
                        energy.owner.exhausted_energies[energy.energy_type].append(energy) 
                    self.give_energy_rewards(unique_players_contributed, filled_wall)
                    self.turn.temp_rewards += 3000

                # if the current top wall is completed, change the top wall to next wall
                monument.change_top_wall(filled_wall.owner)
                # TODO: start mini turn here, use filled_wall to get the energy and the owner's of the energy to know which players will be part of the mini turn

        num_built = self.check_num_of_build_walls()
        if num_built == 6:
            self.monument_index = 5
            self.check_over()
        else:
            self.monument_index = num_built


        Logger.log(
            "Current monument is: "
            + str(self.monuments[self.monument_index].name)
            + " index is: "
            + str(self.monument_index)
            + " num walls completed "
            + str(self.monuments[self.monument_index].get_num_walls_completed()),
            "GAME_ENGINE_LOGS",
        )
        self.action_counter += 1
        return True

    def check_num_of_build_walls(self) -> int:
        total_built = 0
        for i in self.monuments:
            if i.is_completed():
                total_built += 1
        return total_built


    def get_current_agents_turn(self) -> str:
        return self.get_agents()[self.current_player]

    def get_current_characters_turn(self) -> str:
        return constants.CHARACTER_NAMES[self.current_player]

    def get_game_state(self):
        index_of_agent = self.current_player
        all_character_states = []
        for i in range(len(self.players)):
            index = (i + index_of_agent) % len(self.players)
            player = self.players[index]
            all_character_states.extend(States.get_character_states(self, player))

        return all_character_states

    def get_reward(self, agent_name):
        agent = self.get_agent(agent_name)
        total_reward = 0
        total_reward += VictoryPoints.calcFullyGainedEnergy(self, agent)
        total_reward += VictoryPoints.calcBridgesBuilt(self, agent) 
        total_reward += VictoryPoints.calcMonumentEnergy(self, agent)
        total_reward += VictoryPoints.calcPillarsOfCivilization(self, agent)

        return total_reward

    def get_winner(self):
        max = 0
        winner = ""
        for agent in constants.AGENT_NAMES:
            if self.get_agent(agent).get_transmuter().get_total_empty_cells() > max:
                winner = agent
        return winner

    def render(self, agent_name):
        # agent = self.get_agent(agent_name)
        # Logger.log(str(agent.character), "GAME_ENGINE_LOGS")
        # agent.get_transmuter().print_transmuter()
        # Logger.log(
        #     str(agent.location) + " " + str(agent.initial_location), "GAME_ENGINE_LOGS"
        # )
        # self.turn.print_turn_state()
        pass

    def give_energy_rewards(self, players_contributed: list[Player], monument_wall):
        monument_wall.is_reward_given = True
        for i in monument_wall.rewarded_energy:
            for j in players_contributed:
                if i == "Any":
                    for k in j.remaining_energies:
                        if len(j.remaining_energies[k]) > 0:
                            energy = j.remaining_energies[k].pop()
                            Logger.log(
                                "BEFORE REWARDS energies are: "
                                + str(j.exhausted_energies),
                                "GAME_ENGINE_LOGS",
                            )
                            j.exhausted_energies[energy.energy_type].append(energy)
                            Logger.log(
                                "AFTER REWARDS energies are: "
                                + str(j.exhausted_energies),
                                "GAME_ENGINE_LOGS",
                            )
                            return
                else:
                    if len(j.remaining_energies[i]) > 0:
                        energy = j.remaining_energies[i].pop()
                        Logger.log(
                            "BEFORE REWARDS energies are: " + str(j.exhausted_energies),
                            "GAME_ENGINE_LOGS",
                        )
                        j.exhausted_energies[energy.energy_type].append(energy)
                        Logger.log(
                            "AFTER REWARDS energies are: " + str(j.exhausted_energies),
                            "GAME_ENGINE_LOGS",
                        )

    def _check_if_last_wall_filled(self):
        if self.monument_index == 5:
            if self.monuments[self.monument_index].is_completed():
                return True
        return False

    def _check_if_current_wall_filled(self):
        if self.monuments[self.monument_index].is_completed():
            return True
        return False

    def assign_temp_rewards(self, action):
        action_name = (self.get_action_names()[action])["action"]
        reward = 0
        if action_name == "End Turn":
            reward = -1
        elif action_name == "Convey 1":
            reward = +0
        elif action_name == "Action Tokens":
            reward = +0
        elif action_name == "Fill Monument":
            reward = +0
        elif action_name == "Build Bridge":
            reward = +0
        return reward + self.turn.get_temp_reward()
