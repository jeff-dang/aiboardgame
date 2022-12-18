from abc import ABC, abstractmethod


class ActionBase(ABC):

    @abstractmethod
    def availableActions(self):
        # Returns the list of available actions
        raise NotImplementedError

    @abstractmethod
    def isLegalAction(self, agent):
        # Returns the list of available actions
        raise NotImplementedError
