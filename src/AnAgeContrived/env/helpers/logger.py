class Logger:
    ALL_LOGS = True

    GAME_ENGINE_LOGS = True
    MONUMENT_LOGS = True
    ENERGY_LOGS = True
    ACTION_LOGS = True
    HELPER_LOGS = True
    OBSERVATION_SPACE_LOGS = True
    OTHER_LOGS = True
    CONDITION_CHECK_LOGS = True
    FLOW_LOGS = True
    INITIALIZATION_LOGS = True
    TURN_LOGS = True
    TRANSMUTER_LOGS = True

    @staticmethod
    def log(message: str, type: str):
        if Logger.ALL_LOGS == False:
            pass
        else:
            if type == "OTHER_LOGS" and Logger.OTHER_LOGS == True:
                print("OTHER_LOGS", message)
            elif type == "GAME_ENGINE_LOGS" and Logger.GAME_ENGINE_LOGS == True:
                print("GAME_ENGINE_LOGS", message)
            elif type == "MONUMENT_LOGS" and Logger.MONUMENT_LOGS == True:
                print("MONUMENT_LOGS", message)
            elif type == "ENERGY_LOGS" and Logger.ENERGY_LOGS == True:
                print("ENERGY_LOGS", message)
            elif type == "ACTION_LOGS" and Logger.ACTION_LOGS == True:
                print("ACTION_LOGS", message)
            elif type == "HELPER_LOGS" and Logger.HELPER_LOGS == True:
                print("HELPER_LOGS", message)
            elif (
                type == "OBSERVATION_SPACE_LOGS"
                and Logger.OBSERVATION_SPACE_LOGS == True
            ):
                print("OBSERVATION_SPACE_LOGS", message)
            elif type == "CONDITION_CHECK_LOGS" and Logger.CONDITION_CHECK_LOGS == True:
                print("CONDITION_CHECK_LOGS", message)
            elif type == "FLOW_LOGS" and Logger.FLOW_LOGS == True:
                print("FLOW_LOGS", message)
            elif type == "INITIALIZATION_LOGS" and Logger.INITIALIZATION_LOGS == True:
                print("INITIALIZATION_LOGS", message)
            elif type == "TURN_LOGS" and Logger.TURN_LOGS == True:
                print("TURN_LOGS", message)
            elif type == "TRANSMUTER_LOGS" and Logger.TRANSMUTER_LOGS == True:
                print("TRANSMUTER_LOGS", message)
