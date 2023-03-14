from __future__ import annotations
from .victorypoints import VictoryPoints
from env.helpers.turn import Turn

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
from env.scoring import Scoring
import env.helpers.constants as constants
from env.entities.energy import EnergyTile, Energy
from env.entities.map_data import Map_Areas
from env.helpers.logger import Logger


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

        monument_1 = Monument(
            "THE ANFIRIEN BEACON",
            Map_Areas.PLAINS,
            [
                MonumentWall(
                    [Energy.INVERTIBLE, Energy.INVERTIBLE, Energy.INVERTIBLE],
                    [Energy.CONSTRUCTIVE, Energy.INVERTIBLE],
                ),
                MonumentWall(
                    [Energy.CONSTRUCTIVE, Energy.CONSTRUCTIVE, Energy.GENERATIVE],
                    [Energy.PRIMAL],
                ),
                MonumentWall(
                    [Energy.GENERATIVE, Energy.INVERTIBLE, Energy.INVERTIBLE],
                    [Energy.GENERATIVE],
                ),
                # TODO: Need a mechanism to handle any energy reward
                MonumentWall([Energy.GENERATIVE, Energy.CONSTRUCTIVE], ["Any"]),
            ],
        )

        monument_2 = Monument(
            "THE LIBRARY OF VALDUIN",
            Map_Areas.PLAINS,
            [
                MonumentWall(
                    [Energy.GENERATIVE, Energy.CONSTRUCTIVE, Energy.CONSTRUCTIVE],
                    [Energy.GENERATIVE, Energy.INVERTIBLE],
                ),
                MonumentWall(
                    [Energy.CONSTRUCTIVE, Energy.INVERTIBLE, Energy.INVERTIBLE],
                    [Energy.CONSTRUCTIVE],
                ),
                MonumentWall(
                    [Energy.CONSTRUCTIVE, Energy.GENERATIVE, Energy.GENERATIVE],
                    [Energy.PRIMAL],
                ),
                # TODO: Need a mechanism to handle any energy reward
                MonumentWall([Energy.INVERTIBLE, Energy.GENERATIVE], ["Any"]),
            ],
        )

        monument_3 = Monument(
            "THE ERIDONIC GATE",
            Map_Areas.QUARRY,
            [
                MonumentWall(
                    [Energy.GENERATIVE, Energy.INVERTIBLE, Energy.INVERTIBLE],
                    [Energy.CONSTRUCTIVE, Energy.GENERATIVE],
                ),
                MonumentWall(
                    [Energy.CONSTRUCTIVE, Energy.INVERTIBLE, Energy.GENERATIVE],
                    [Energy.INVERTIBLE],
                ),
                MonumentWall(
                    [Energy.GENERATIVE, Energy.CONSTRUCTIVE, Energy.CONSTRUCTIVE],
                    [Energy.GENERATIVE],
                ),
                # TODO: Need a mechanism to handle any energy reward
                MonumentWall([Energy.CONSTRUCTIVE, Energy.INVERTIBLE], ["Any"]),
            ],
        )

        monument_4 = Monument(
            "THE NAMARILLION FORGE",
            Map_Areas.MOUNTAIN,
            [
                MonumentWall(
                    [Energy.CONSTRUCTIVE, Energy.GENERATIVE, Energy.GENERATIVE],
                    [Energy.INVERTIBLE, Energy.GENERATIVE],
                ),
                MonumentWall(
                    [Energy.CONSTRUCTIVE, Energy.INVERTIBLE, Energy.GENERATIVE],
                    [Energy.PRIMAL],
                ),
                MonumentWall(
                    [Energy.GENERATIVE, Energy.INVERTIBLE, Energy.INVERTIBLE],
                    [Energy.CONSTRUCTIVE],
                ),
                # TODO: Need a mechanism to handle any energy reward
                MonumentWall([Energy.CONSTRUCTIVE, Energy.INVERTIBLE], ["Any"]),
            ],
        )

        monument_5 = Monument(
            "THE FORTRESS OF KOLYM THRIN",
            Map_Areas.FOREST,
            [
                MonumentWall(
                    [Energy.CONSTRUCTIVE, Energy.INVERTIBLE, Energy.GENERATIVE],
                    [Energy.CONSTRUCTIVE, Energy.PRIMAL],
                ),
                MonumentWall(
                    [Energy.INVERTIBLE, Energy.INVERTIBLE, Energy.GENERATIVE],
                    [Energy.GENERATIVE],
                ),
                # TODO: Need a mechanism to handle any energy reward
                MonumentWall([Energy.GENERATIVE, Energy.INVERTIBLE], ["Any"]),
                MonumentWall(
                    [Energy.CONSTRUCTIVE, Energy.CONSTRUCTIVE, Energy.GENERATIVE],
                    [Energy.INVERTIBLE],
                ),
                MonumentWall([Energy.PRIMAL], []),
            ],
        )

        monument_6 = Monument(
            "THE SHIP OF TOLINTHRA",
            Map_Areas.SEA,
            [
                MonumentWall(
                    [Energy.GENERATIVE, Energy.GENERATIVE, Energy.INVERTIBLE],
                    [Energy.CONSTRUCTIVE, Energy.INVERTIBLE],
                ),
                MonumentWall(
                    [Energy.GENERATIVE, Energy.CONSTRUCTIVE, Energy.INVERTIBLE],
                    [Energy.GENERATIVE],
                ),
                MonumentWall(
                    [Energy.INVERTIBLE, Energy.CONSTRUCTIVE, Energy.CONSTRUCTIVE],
                    [Energy.PRIMAL],
                ),
                # TODO: Need a mechanism to handle any energy reward
                MonumentWall([Energy.GENERATIVE, Energy.CONSTRUCTIVE], ["Any"]),
            ],
        )

        self.monuments: list[Monument] = [
            monument_1,
            monument_2,
            monument_3,
            monument_4,
            monument_5,
            monument_6,
        ]

        for i in range(len(constants.CHARACTER_NAMES)):
            self.players.append(
                Player(
                    constants.AGENT_NAMES[i],
                    constants.CHARACTER_NAMES[i],
                    self.map.starting_positions[i],
                )
            )

        Logger.log("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", "INITIALIZATION_LOGS")
        Logger.log("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", "INITIALIZATION_LOGS")
        Logger.log("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", "INITIALIZATION_LOGS")
        Logger.log("INITIALIZING THE GAME ENGINE:", "INITIALIZATION_LOGS")
        Logger.log(
            "New monument index is:" + str(self.monument_index), "INITIALIZATION_LOGS"
        )
        current_monument: Monument = self.monuments[self.monument_index]
        # print('remaining sections:', current_monument.get_top_wall().remaining_sections, 'filled energies:', current_monument.get_top_wall().filled_sections, 'num of empty spaces:', current_monument.get_top_wall().empty_sections)
        # print('current monument is:', current_monument.name, 'monument wall starting accepted:', current_monument.get_top_wall().sections)
        Logger.log("-----------------", "INITIALIZATION_LOGS")
        # print('monuments:', self.monuments)
        Logger.log("-----------------", "INITIALIZATION_LOGS")
        Logger.log("-----------------", "INITIALIZATION_LOGS")
        # print('monument walls:', current_monument.walls)
        Logger.log("-----------------", "INITIALIZATION_LOGS")
        # print('eng.legal actions:', self.get_legal_action_names(self.players[self.current_player].agent))
        # print('eng.action mask:', self.get_legal_actions(self.players[self.current_player].agent))
        Logger.log("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", "INITIALIZATION_LOGS")
        Logger.log("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", "INITIALIZATION_LOGS")
        Logger.log("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", "INITIALIZATION_LOGS")

    def check_over(self):
        if self._check_if_current_wall_filled():
            if self.monument_index < 5:
                self.monument_index += 1
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
        self.num_of_built_monuments: int = 0

        for i in range(0, 6):
            monument = self.monuments[i]
            if monument.is_top_wall_completed():
                filled_wall = monument.get_top_wall()
                if filled_wall.is_reward_given == False:
                    self.turn.update_turn_type(TurnType.B)
                    players_contributed = []
                    for i in filled_wall.filled_sections:
                        players_contributed.append(i.owner)
                        unique_players_contributed = set(
                            players_contributed
                        )  # only rewards once if player contributed multiple times
                    self.give_energy_rewards(unique_players_contributed, filled_wall)
                # if the current top wall is completed, change the top wall to next wall
                monument.change_top_wall()
                # TODO: start mini turn here, use filled_wall to get the energy and the owner's of the energy to know which players will be part of the mini turn
            if monument.is_completed() and self.monument_index < 5:
                self.monument_index += 1
                self.num_of_built_monuments += 1

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
        total_reward += VictoryPoints.calcFullyGainedEnergy(self, agent) * 100
        # total_reward += VictoryPoints.calcMonumentEnergy(self, agent)
        # monument_score = Scoring.get_monument_score(self, agent_name)

        return total_reward

    def get_winner(self):
        max = 0
        winner = ""
        for agent in constants.AGENT_NAMES:
            if self.get_agent(agent).get_transmuter().get_total_empty_cells() > max:
                winner = agent
        return winner

    def render(self, agent_name):
        agent = self.get_agent(agent_name)
        Logger.log(str(agent.character), "GAME_ENGINE_LOGS")
        agent.get_transmuter().print_transmuter()
        Logger.log(
            str(agent.location) + " " + str(agent.initial_location), "GAME_ENGINE_LOGS"
        )
        self.turn.print_turn_state()

    # TODO: fix it in a way that players can select from one of the rewards instead of giving both energies automatically
    def give_energy_rewards(self, players_contributed: list[Player], monument_wall):
        for i in monument_wall.rewarded_energy:
            for j in players_contributed:
                if i == "Any":
                    for k in j.remaining_energies:
                        if len(k) > 0:
                            energy = k.pop()
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
        monument_wall.is_reward_given = True

    def _check_if_last_wall_filled(self):
        if self.monument_index == 5:
            if self.monuments[self.monument_index].is_completed():
                return True
        return False

    def _check_if_current_wall_filled(self):
        if self.monuments[self.monument_index].is_completed():
            return True
        return False
