from env.helpers.constants import GAME_ENGINE_LOGS, MONUMENT_LOGS, ENERGY_LOGS, ACTION_LOGS, HELPER_LOGS, OBSERVATION_SPACE_LOGS, OTHER_LOGS, CONDITION_CHECK_LOGS, FLOW_LOGS, INITIALIZATION_LOGS

class Logger():

    @staticmethod
    def log(message: str, type: str):
        if type == 'OTHER_LOGS' and OTHER_LOGS == True:
            print(message)
        elif type == 'GAME_ENGINE_LOGS' and GAME_ENGINE_LOGS == True:
            print('GAME_ENGINE_LOGS', message)
        elif type == 'MONUMENT_LOGS' and MONUMENT_LOGS == True:
            print('MONUMENT_LOGS', message)
        elif type == 'ENERGY_LOGS' and ENERGY_LOGS == True:
            print('ENERGY_LOGS', message)
        elif type == 'ACTION_LOGS' and ACTION_LOGS == True:
            print('ACTION_LOGS', message)
        elif type == 'HELPER_LOGS' and HELPER_LOGS == True:
            print('HELPER_LOGS', message)
        elif type == 'OBSERVATION_SPACE_LOGS' and OBSERVATION_SPACE_LOGS == True:
            print('OBSERVATION_SPACE_LOGS', message)
        elif type == 'CONDITION_CHECK_LOGS' and CONDITION_CHECK_LOGS == True:
            print('CONDITION_CHECK_LOGS', message)
        elif type == 'FLOW_LOGS' and FLOW_LOGS == True:
            print('FLOW_LOGS', message)
        elif type == 'INITIALIZATION_LOGS' and INITIALIZATION_LOGS == True:
            print('INITIALIZATION_LOGS', message)
