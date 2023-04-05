# Author: Michael Ilao
# Date: March 12th, 2023
# Description: 
# Modules to convert entity & helper module funtions into a Command objects to utilize the Command design pattern
# the actions in this file are related to building bridges

from env.command import Command
from env.helpers.build_bridge import BuildBridge

action_family = "Build Bridge"


class BuildBridge1Reward1(Command):

    def __init__(self, player, engine):
        super().__init__(player, engine)
        self.location = 1
        self.reward = 1
        self.action = action_family
        self.action_details = "Location " + str(self.location) + " Reward " + str(self.reward)

    def execute(self):
        BuildBridge.build_bridge(self.engine, self.location, self.player, self.reward)

    def check(self):
        return BuildBridge.is_legal_move(self.player, self.engine, self.location)


class BuildBridge1Reward2(Command):

    def __init__(self, player, engine):
        super().__init__(player, engine)
        self.location = 1
        self.reward = 2
        self.action = action_family
        self.action_details = "Location " + str(self.location) + " Reward " + str(self.reward)

    def execute(self):
        BuildBridge.build_bridge(self.engine, self.location, self.player, self.reward)

    def check(self):
        return BuildBridge.is_legal_move(self.player, self.engine, self.location)


class BuildBridge2Reward1(Command):

    def __init__(self, player, engine):
        super().__init__(player, engine)
        self.location = 2
        self.reward = 1
        self.action = action_family
        self.action_details = "Location " + str(self.location) + " Reward " + str(self.reward)

    def execute(self):
        BuildBridge.build_bridge(self.engine, self.location, self.player, self.reward)

    def check(self):
        return BuildBridge.is_legal_move(self.player, self.engine, self.location)


class BuildBridge2Reward2(Command):

    def __init__(self, player, engine):
        super().__init__(player, engine)
        self.location = 2
        self.reward = 2
        self.action = action_family
        self.action_details = "Location " + str(self.location) + " Reward " + str(self.reward)

    def execute(self):
        BuildBridge.build_bridge(self.engine, self.location, self.player, self.reward)

    def check(self):
        return BuildBridge.is_legal_move(self.player, self.engine, self.location)


class BuildBridge3Reward1(Command):

    def __init__(self, player, engine):
        super().__init__(player, engine)
        self.location = 3
        self.reward = 1
        self.action = action_family
        self.action_details = "Location " + str(self.location) + " Reward " + str(self.reward)

    def execute(self):
        BuildBridge.build_bridge(self.engine, self.location, self.player, self.reward)

    def check(self):
        return BuildBridge.is_legal_move(self.player, self.engine, self.location)


class BuildBridge3Reward2(Command):

    def __init__(self, player, engine):
        super().__init__(player, engine)
        self.location = 3
        self.reward = 2
        self.action = action_family
        self.action_details = "Location " + str(self.location) + " Reward " + str(self.reward)

    def execute(self):
        BuildBridge.build_bridge(self.engine, self.location, self.player, self.reward)

    def check(self):
        return BuildBridge.is_legal_move(self.player, self.engine, self.location)


class BuildBridge4Reward1(Command):

    def __init__(self, player, engine):
        super().__init__(player, engine)
        self.location = 4
        self.reward = 1
        self.action = action_family
        self.action_details = "Location " + str(self.location) + " Reward " + str(self.reward)

    def execute(self):
        BuildBridge.build_bridge(self.engine, self.location, self.player, self.reward)

    def check(self):
        return BuildBridge.is_legal_move(self.player, self.engine, self.location)


class BuildBridge4Reward2(Command):

    def __init__(self, player, engine):
        super().__init__(player, engine)
        self.location = 4
        self.reward = 2
        self.action = action_family
        self.action_details = "Location " + str(self.location) + " Reward " + str(self.reward)

    def execute(self):
        BuildBridge.build_bridge(self.engine, self.location, self.player, self.reward)

    def check(self):
        return BuildBridge.is_legal_move(self.player, self.engine, self.location)


class BuildBridge5Reward1(Command):

    def __init__(self, player, engine):
        super().__init__(player, engine)
        self.location = 5
        self.reward = 1
        self.action = action_family
        self.action_details = "Location " + str(self.location) + " Reward " + str(self.reward)

    def execute(self):
        BuildBridge.build_bridge(self.engine, self.location, self.player, self.reward)

    def check(self):
        return BuildBridge.is_legal_move(self.player, self.engine, self.location)


class BuildBridge5Reward2(Command):

    def __init__(self, player, engine):
        super().__init__(player, engine)
        self.location = 5
        self.reward = 2
        self.action = action_family
        self.action_details = "Location " + str(self.location) + " Reward " + str(self.reward)

    def execute(self):
        BuildBridge.build_bridge(self.engine, self.location, self.player, self.reward)

    def check(self):
        return BuildBridge.is_legal_move(self.player, self.engine, self.location)


class BuildBridge6Reward1(Command):

    def __init__(self, player, engine):
        super().__init__(player, engine)
        self.location = 6
        self.reward = 1
        self.action = action_family
        self.action_details = "Location " + str(self.location) + " Reward " + str(self.reward)

    def execute(self):
        BuildBridge.build_bridge(self.engine, self.location, self.player, self.reward)

    def check(self):
        return BuildBridge.is_legal_move(self.player, self.engine, self.location)


class BuildBridge6Reward2(Command):

    def __init__(self, player, engine):
        super().__init__(player, engine)
        self.location = 6
        self.reward = 2
        self.action = action_family
        self.action_details = "Location " + str(self.location) + " Reward " + str(self.reward)

    def execute(self):
        BuildBridge.build_bridge(self.engine, self.location, self.player, self.reward)

    def check(self):
        return BuildBridge.is_legal_move(self.player, self.engine, self.location)


class BuildBridge7Reward1(Command):

    def __init__(self, player, engine):
        super().__init__(player, engine)
        self.location = 7
        self.reward = 1
        self.action = action_family
        self.action_details = "Location " + str(self.location) + " Reward " + str(self.reward)

    def execute(self):
        BuildBridge.build_bridge(self.engine, self.location, self.player, self.reward)

    def check(self):
        return BuildBridge.is_legal_move(self.player, self.engine, self.location)


class BuildBridge7Reward2(Command):

    def __init__(self, player, engine):
        super().__init__(player, engine)
        self.location = 7
        self.reward = 2
        self.action = action_family
        self.action_details = "Location " + str(self.location) + " Reward " + str(self.reward)

    def execute(self):
        BuildBridge.build_bridge(self.engine, self.location, self.player, self.reward)

    def check(self):
        return BuildBridge.is_legal_move(self.player, self.engine, self.location)


class BuildBridge8Reward1(Command):

    def __init__(self, player, engine):
        super().__init__(player, engine)
        self.location = 8
        self.reward = 1
        self.action = action_family
        self.action_details = "Location " + str(self.location) + " Reward " + str(self.reward)

    def execute(self):
        BuildBridge.build_bridge(self.engine, self.location, self.player, self.reward)

    def check(self):
        return BuildBridge.is_legal_move(self.player, self.engine, self.location)


class BuildBridge8Reward2(Command):

    def __init__(self, player, engine):
        super().__init__(player, engine)
        self.location = 8
        self.reward = 2
        self.action = action_family
        self.action_details = "Location " + str(self.location) + " Reward " + str(self.reward)

    def execute(self):
        BuildBridge.build_bridge(self.engine, self.location, self.player, self.reward)

    def check(self):
        return BuildBridge.is_legal_move(self.player, self.engine, self.location)


class BuildBridge9Reward1(Command):

    def __init__(self, player, engine):
        super().__init__(player, engine)
        self.location = 9
        self.reward = 1
        self.action = action_family
        self.action_details = "Location " + str(self.location) + " Reward " + str(self.reward)

    def execute(self):
        BuildBridge.build_bridge(self.engine, self.location, self.player, self.reward)

    def check(self):
        return BuildBridge.is_legal_move(self.player, self.engine, self.location)


class BuildBridge9Reward2(Command):

    def __init__(self, player, engine):
        super().__init__(player, engine)
        self.location = 9
        self.reward = 2
        self.action = action_family
        self.action_details = "Location " + str(self.location) + " Reward " + str(self.reward)

    def execute(self):
        BuildBridge.build_bridge(self.engine, self.location, self.player, self.reward)

    def check(self):
        return BuildBridge.is_legal_move(self.player, self.engine, self.location)


class BuildBridge10Reward1(Command):

    def __init__(self, player, engine):
        super().__init__(player, engine)
        self.location = 10
        self.reward = 1
        self.action = action_family
        self.action_details = "Location " + str(self.location) + " Reward " + str(self.reward)

    def execute(self):
        BuildBridge.build_bridge(self.engine, self.location, self.player, self.reward)

    def check(self):
        return BuildBridge.is_legal_move(self.player, self.engine, self.location)


class BuildBridge10Reward2(Command):

    def __init__(self, player, engine):
        super().__init__(player, engine)
        self.location = 10
        self.reward = 2
        self.action = action_family
        self.action_details = "Location " + str(self.location) + " Reward " + str(self.reward)

    def execute(self):
        BuildBridge.build_bridge(self.engine, self.location, self.player, self.reward)

    def check(self):
        return BuildBridge.is_legal_move(self.player, self.engine, self.location)
