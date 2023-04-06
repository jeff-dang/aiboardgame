from env.command import Command


class Play0(Command):

    def __init__(self, player, engine):
        super().__init__(player, engine)
        self.pos = 0
        self.action = "Pos "+str(self.pos)
        self.action_details = "Pos "+str(self.pos)

    def execute(self):
        if(self.player == "player_0"):
            self.engine.board[self.pos] = 1
        if(self.player == "player_1"):
            self.engine.board[self.pos] = 2

    def check(self) -> bool:
        print(self.engine)
        return not(self.engine.board[self.pos] == 0)
    
class Play1(Command):

    def __init__(self, engine, player):
        super().__init__(player, engine)
        self.pos = 1
        self.action = "Pos "+str(self.pos)
        self.action_details = "Pos "+str(self.pos)

    def execute(self):
        if(self.player == "player_0"):
            self.engine.board[self.pos] = 1
        if(self.player == "player_1"):
            self.engine.board[self.pos] = 2

    def check(self) -> bool:
        return not(self.engine.board[self.pos] == 0)

class Play2(Command):

    def __init__(self, engine, player):
        super().__init__(player, engine)
        self.pos = 2
        self.action = "Pos "+str(self.pos)
        self.action_details = "Pos "+str(self.pos)

    def execute(self):
        if(self.player == "player_0"):
            self.engine.board[self.pos] = 1
        if(self.player == "player_1"):
            self.engine.board[self.pos] = 2

    def check(self) -> bool:
        return not(self.engine.board[self.pos] == 0)
    
class Play3(Command):

    def __init__(self, engine, player):
        super().__init__(player, engine)
        self.pos = 3
        self.action = "Pos "+str(self.pos)
        self.action_details = "Pos "+str(self.pos)

    def execute(self):
        if(self.player == "player_0"):
            self.engine.board[self.pos] = 1
        if(self.player == "player_1"):
            self.engine.board[self.pos] = 2

    def check(self) -> bool:
        return not(self.engine.board[self.pos] == 0)


class Play4(Command):

    def __init__(self, engine, player):
        super().__init__(player, engine)
        self.pos = 4
        self.action = "Pos "+str(self.pos)
        self.action_details = "Pos "+str(self.pos)

    def execute(self):
        if(self.player == "player_0"):
            self.engine.board[self.pos] = 1
        if(self.player == "player_1"):
            self.engine.board[self.pos] = 2

    def check(self) -> bool:
        return not(self.engine.board[self.pos] == 0)

class Play5(Command):

    def __init__(self, engine, player):
        super().__init__(player, engine)
        self.pos = 5
        self.action = "Pos "+str(self.pos)
        self.action_details = "Pos "+str(self.pos)

    def execute(self):
        if(self.player == "player_0"):
            self.engine.board[self.pos] = 1
        if(self.player == "player_1"):
            self.engine.board[self.pos] = 2

    def check(self) -> bool:
        return not(self.engine.board[self.pos] == 0)

class Play6(Command):

    def __init__(self, engine, player):
        super().__init__(player, engine)
        self.pos = 6
        self.action = "Pos "+str(self.pos)
        self.action_details = "Pos "+str(self.pos)

    def execute(self):
        if(self.player == "player_0"):
            self.engine.board[self.pos] = 1
        if(self.player == "player_1"):
            self.engine.board[self.pos] = 2

    def check(self) -> bool:
        return not(self.engine.board[self.pos] == 0)


class Play7(Command):

    def __init__(self, engine, player):
        super().__init__(player, engine)
        self.pos = 7
        self.action = "Pos "+str(self.pos)
        self.action_details = "Pos "+str(self.pos)

    def execute(self):
        if(self.player == "player_0"):
            self.engine.board[self.pos] = 1
        if(self.player == "player_1"):
            self.engine.board[self.pos] = 2

    def check(self) -> bool:
        return not(self.engine.board[self.pos] == 0)


class Play8(Command):

    def __init__(self, engine, player):
        super().__init__(player, engine)
        self.pos = 8
        self.action = "Pos "+str(self.pos)
        self.action_details = "Pos "+str(self.pos)

    def execute(self):
        if(self.player == "player_0"):
            self.engine.board[self.pos] = 1
        if(self.player == "player_1"):
            self.engine.board[self.pos] = 2

    def check(self) -> bool:
        return not(self.engine.board[self.pos] == 0)



