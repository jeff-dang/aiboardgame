# Main game runner
from engine import Engine


engine = Engine()
engine.makeMove(1, [0, 0, 1, 0, 0, 0, 0, 0, 0])
engine.makeMove(2, [0, 1, 0, 0, 0, 0, 0, 0, 0])
engine.makeMove(1, [1, 0, 0, 0, 0, 0, 0, 0, 0])
engine.makeMove(2, [0, 0, 0, 0, 0, 0, 0, 1, 0])
engine.makeMove(1, [0, 0, 0, 0, 0, 0, 0, 0, 1])
engine.makeMove(2, [0, 0, 0, 0, 1, 0, 0, 0, 0])
print(engine.getState(1))
