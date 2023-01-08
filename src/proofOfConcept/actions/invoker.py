
class Invoker():

    def __init__(self):
        self.actions = []

    #maybe add a number to keep the each action in the same spot or always add them in the same order
    def add_action(self, action):
        self.actions.append(action)

    def run(self, index):
        self.actions[index].execute()