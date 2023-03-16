from __future__ import annotations
# these imports will not be imported in the runtime, it is just to help coding to do type_checking
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from env.entities.player import Player
    from env.engine import Engine
    pass

from env.command import Command
from env.helpers.convey import Convey
from env.entities.energy import Energy

action_family_1 = "Convey 1"
action_family_2 = "Convey 2"


class ConveyOnceFirstCard(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = action_family_1
        self.action_details = "First Card"

    def execute(self):
        Convey.convey(self.engine, self.player, 1, 0)

    def check(self) -> bool:
        return Convey.convey1Legal(self.engine)
    
class ConveyOnceFirstCardTopConstructiveBottomConstructive(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = action_family_1
        self.action_details = "First Card - [Constructive, Constructive]"

    def execute(self):
        Convey.convey(self.engine, self.player, 1, 0, [Energy.CONSTRUCTIVE, Energy.CONSTRUCTIVE])

    def check(self) -> bool:
        return Convey.convey1_top_constructive_bottom_constructive_legal(self.player, self.engine)
    
class ConveyOnceFirstCardTopConstructiveBottomInvertible(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = action_family_1
        self.action_details = "First Card - [Constructive, Invertible]"

    def execute(self):
        Convey.convey(self.engine, self.player, 1, 0, [Energy.CONSTRUCTIVE, Energy.INVERTIBLE])

    def check(self) -> bool:
        return Convey.convey1_top_constructive_bottom_invertible_legal(self.player, self.engine)
    
class ConveyOnceFirstCardTopConstructiveBottomGenerative(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = action_family_1
        self.action_details = "First Card - [Constructive, Generative]"

    def execute(self):
        Convey.convey(self.engine, self.player, 1, 0, [Energy.CONSTRUCTIVE, Energy.GENERATIVE])

    def check(self) -> bool:
        return Convey.convey1_top_constructive_bottom_generative_legal(self.player, self.engine)
    
class ConveyOnceFirstCardTopConstructiveBottomPrimal(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = action_family_1
        self.action_details = "First Card - [Constructive, Primal]"

    def execute(self):
        Convey.convey(self.engine, self.player, 1, 0, [Energy.CONSTRUCTIVE, Energy.PRIMAL])

    def check(self) -> bool:
        return Convey.convey1_top_constructive_bottom_primal_legal(self.player, self.engine)
    
class ConveyOnceFirstCardTopInvertibleBottomInvertible(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = action_family_1
        self.action_details = "First Card - [Invertible, Invertible]"

    def execute(self):
        Convey.convey(self.engine, self.player, 1, 0, [Energy.INVERTIBLE, Energy.INVERTIBLE])

    def check(self) -> bool:
        return Convey.convey1_top_invertible_bottom_invertible_legal(self.player, self.engine)
    
class ConveyOnceFirstCardTopInvertibleBottomConstructive(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = action_family_1
        self.action_details = "First Card - [Invertible, Constructive]"

    def execute(self):
        Convey.convey(self.engine, self.player, 1, 0, [Energy.INVERTIBLE, Energy.CONSTRUCTIVE])

    def check(self) -> bool:
        return Convey.convey1_top_invertible_bottom_constructive_legal(self.player, self.engine)
    
class ConveyOnceFirstCardTopInvertibleBottomGenerative(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = action_family_1
        self.action_details = "First Card - [Invertible, Generative]"

    def execute(self):
        Convey.convey(self.engine, self.player, 1, 0, [Energy.INVERTIBLE, Energy.GENERATIVE])

    def check(self) -> bool:
        return Convey.convey1_top_invertible_bottom_generative_legal(self.player, self.engine)
    
class ConveyOnceFirstCardTopInvertibleBottomPrimal(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = action_family_1
        self.action_details = "First Card - [Invertible, Primal]"

    def execute(self):
        Convey.convey(self.engine, self.player, 1, 0, [Energy.INVERTIBLE, Energy.PRIMAL])

    def check(self) -> bool:
        return Convey.convey1_top_invertible_bottom_primal_legal(self.player, self.engine)
    
class ConveyOnceFirstCardTopGenerativeBottomGenerative(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = action_family_1
        self.action_details = "First Card - [Generative, Generative]"

    def execute(self):
        Convey.convey(self.engine, self.player, 1, 0, [Energy.GENERATIVE, Energy.GENERATIVE])

    def check(self) -> bool:
        return Convey.convey1_top_generative_bottom_generative_legal(self.player, self.engine)
    
class ConveyOnceFirstCardTopGenerativeBottomConstructive(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = action_family_1
        self.action_details = "First Card - [Generative, Constructive]"

    def execute(self):
        Convey.convey(self.engine, self.player, 1, 0, [Energy.GENERATIVE, Energy.CONSTRUCTIVE])

    def check(self) -> bool:
        return Convey.convey1_top_generative_bottom_constructive_legal(self.player, self.engine)
    
class ConveyOnceFirstCardTopGenerativeBottomInvertible(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = action_family_1
        self.action_details = "First Card - [Generative, Invertible]"

    def execute(self):
        Convey.convey(self.engine, self.player, 1, 0, [Energy.GENERATIVE, Energy.INVERTIBLE])

    def check(self) -> bool:
        return Convey.convey1_top_generative_bottom_invertible_legal(self.player, self.engine)
    
class ConveyOnceFirstCardTopGenerativeBottomPrimal(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = action_family_1
        self.action_details = "First Card - [Generative, Primal]"

    def execute(self):
        Convey.convey(self.engine, self.player, 1, 0, [Energy.GENERATIVE, Energy.PRIMAL])

    def check(self) -> bool:
        return Convey.convey1_top_generative_bottom_primal_legal(self.player, self.engine)
    
class ConveyOnceFirstCardTopPrimalBottomPrimal(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = action_family_1
        self.action_details = "First Card - [Primal, Primal]"

    def execute(self):
        Convey.convey(self.engine, self.player, 1, 0, [Energy.PRIMAL, Energy.PRIMAL])

    def check(self) -> bool:
        return Convey.convey1_top_primal_bottom_primal_legal(self.player, self.engine)
    
class ConveyOnceFirstCardTopPrimalBottomConstructive(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = action_family_1
        self.action_details = "First Card - [Primal, Constructive]"

    def execute(self):
        Convey.convey(self.engine, self.player, 1, 0, [Energy.PRIMAL, Energy.CONSTRUCTIVE])

    def check(self) -> bool:
        return Convey.convey1_top_primal_bottom_constructive_legal(self.player, self.engine)
    
class ConveyOnceFirstCardTopPrimalBottomInvertible(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = action_family_1
        self.action_details = "First Card - [Primal, Invertible]"

    def execute(self):
        Convey.convey(self.engine, self.player, 1, 0, [Energy.PRIMAL, Energy.INVERTIBLE])

    def check(self) -> bool:
        return Convey.convey1_top_primal_bottom_invertible_legal(self.player, self.engine)
    
class ConveyOnceFirstCardTopPrimalBottomGenerative(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = action_family_1
        self.action_details = "First Card - [Primal, Invertible]"

    def execute(self):
        Convey.convey(self.engine, self.player, 1, 0, [Energy.PRIMAL, Energy.GENERATIVE])

    def check(self) -> bool:
        return Convey.convey1_top_primal_bottom_generative_legal(self.player, self.engine)


class ConveyOnceSecondCard(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = action_family_1
        self.action_details = "Second Card"

    def execute(self):
        Convey.convey(self.engine, self.player, 1, 1)

    def check(self) -> bool:
        return Convey.convey1Legal(self.engine)
    
class ConveyOnceFirstCardTopConstructiveBottomConstructive(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = action_family_1
        self.action_details = "Second Card - [Constructive, Constructive]"

    def execute(self):
        Convey.convey(self.engine, self.player, 1, 1, [Energy.CONSTRUCTIVE, Energy.CONSTRUCTIVE])

    def check(self) -> bool:
        return Convey.convey1_top_constructive_bottom_constructive_legal(self.player, self.engine)
    
class ConveyOnceFirstCardTopConstructiveBottomInvertible(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = action_family_1
        self.action_details = "Second Card - [Constructive, Invertible]"

    def execute(self):
        Convey.convey(self.engine, self.player, 1, 1, [Energy.CONSTRUCTIVE, Energy.INVERTIBLE])

    def check(self) -> bool:
        return Convey.convey1_top_constructive_bottom_invertible_legal(self.player, self.engine)
    
class ConveyOnceFirstCardTopConstructiveBottomGenerative(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = action_family_1
        self.action_details = "Second Card - [Constructive, Generative]"

    def execute(self):
        Convey.convey(self.engine, self.player, 1, 1, [Energy.CONSTRUCTIVE, Energy.GENERATIVE])

    def check(self) -> bool:
        return Convey.convey1_top_constructive_bottom_generative_legal(self.player, self.engine)
    
class ConveyOnceFirstCardTopConstructiveBottomPrimal(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = action_family_1
        self.action_details = "Second Card - [Constructive, Primal]"

    def execute(self):
        Convey.convey(self.engine, self.player, 1, 1, [Energy.CONSTRUCTIVE, Energy.PRIMAL])

    def check(self) -> bool:
        return Convey.convey1_top_constructive_bottom_primal_legal(self.player, self.engine)
    
class ConveyOnceFirstCardTopInvertibleBottomInvertible(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = action_family_1
        self.action_details = "Second Card - [Invertible, Invertible]"

    def execute(self):
        Convey.convey(self.engine, self.player, 1, 1, [Energy.INVERTIBLE, Energy.INVERTIBLE])

    def check(self) -> bool:
        return Convey.convey1_top_invertible_bottom_invertible_legal(self.player, self.engine)
    
class ConveyOnceFirstCardTopInvertibleBottomConstructive(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = action_family_1
        self.action_details = "Second Card - [Invertible, Constructive]"

    def execute(self):
        Convey.convey(self.engine, self.player, 1, 1, [Energy.INVERTIBLE, Energy.CONSTRUCTIVE])

    def check(self) -> bool:
        return Convey.convey1_top_invertible_bottom_constructive_legal(self.player, self.engine)
    
class ConveyOnceFirstCardTopInvertibleBottomGenerative(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = action_family_1
        self.action_details = "Second Card - [Invertible, Generative]"

    def execute(self):
        Convey.convey(self.engine, self.player, 1, 1, [Energy.INVERTIBLE, Energy.GENERATIVE])

    def check(self) -> bool:
        return Convey.convey1_top_invertible_bottom_generative_legal(self.player, self.engine)
    
class ConveyOnceFirstCardTopInvertibleBottomPrimal(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = action_family_1
        self.action_details = "Second Card - [Invertible, Primal]"

    def execute(self):
        Convey.convey(self.engine, self.player, 1, 1, [Energy.INVERTIBLE, Energy.PRIMAL])

    def check(self) -> bool:
        return Convey.convey1_top_invertible_bottom_primal_legal(self.player, self.engine)
    
class ConveyOnceFirstCardTopGenerativeBottomGenerative(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = action_family_1
        self.action_details = "Second Card - [Generative, Generative]"

    def execute(self):
        Convey.convey(self.engine, self.player, 1, 1, [Energy.GENERATIVE, Energy.GENERATIVE])

    def check(self) -> bool:
        return Convey.convey1_top_generative_bottom_generative_legal(self.player, self.engine)
    
class ConveyOnceFirstCardTopGenerativeBottomConstructive(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = action_family_1
        self.action_details = "Second Card - [Generative, Constructive]"

    def execute(self):
        Convey.convey(self.engine, self.player, 1, 1, [Energy.GENERATIVE, Energy.CONSTRUCTIVE])

    def check(self) -> bool:
        return Convey.convey1_top_generative_bottom_constructive_legal(self.player, self.engine)
    
class ConveyOnceFirstCardTopGenerativeBottomInvertible(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = action_family_1
        self.action_details = "Second Card - [Generative, Invertible]"

    def execute(self):
        Convey.convey(self.engine, self.player, 1, 1, [Energy.GENERATIVE, Energy.INVERTIBLE])

    def check(self) -> bool:
        return Convey.convey1_top_generative_bottom_invertible_legal(self.player, self.engine)
    
class ConveyOnceFirstCardTopGenerativeBottomPrimal(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = action_family_1
        self.action_details = "Second Card - [Generative, Primal]"

    def execute(self):
        Convey.convey(self.engine, self.player, 1, 1, [Energy.GENERATIVE, Energy.PRIMAL])

    def check(self) -> bool:
        return Convey.convey1_top_generative_bottom_primal_legal(self.player, self.engine)
    
class ConveyOnceFirstCardTopPrimalBottomPrimal(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = action_family_1
        self.action_details = "Second Card - [Primal, Primal]"

    def execute(self):
        Convey.convey(self.engine, self.player, 1, 1, [Energy.PRIMAL, Energy.PRIMAL])

    def check(self) -> bool:
        return Convey.convey1_top_primal_bottom_primal_legal(self.player, self.engine)
    
class ConveyOnceFirstCardTopPrimalBottomConstructive(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = action_family_1
        self.action_details = "Second Card - [Primal, Constructive]"

    def execute(self):
        Convey.convey(self.engine, self.player, 1, 1, [Energy.PRIMAL, Energy.CONSTRUCTIVE])

    def check(self) -> bool:
        return Convey.convey1_top_primal_bottom_constructive_legal(self.player, self.engine)
    
class ConveyOnceFirstCardTopPrimalBottomInvertible(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = action_family_1
        self.action_details = "Second Card - [Primal, Invertible]"

    def execute(self):
        Convey.convey(self.engine, self.player, 1, 1, [Energy.PRIMAL, Energy.INVERTIBLE])

    def check(self) -> bool:
        return Convey.convey1_top_primal_bottom_invertible_legal(self.player, self.engine)
    
class ConveyOnceFirstCardTopPrimalBottomGenerative(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = action_family_1
        self.action_details = "Second Card - [Primal, Invertible]"

    def execute(self):
        Convey.convey(self.engine, self.player, 1, 1, [Energy.PRIMAL, Energy.GENERATIVE])

    def check(self) -> bool:
        return Convey.convey1_top_primal_bottom_generative_legal(self.player, self.engine)


class ConveyTwiceFirstOrder(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = action_family_2
        self.action_details = "First Order"

    def execute(self):
        Convey.convey(self.engine, self.player, 2, 0)

    def check(self) -> bool:
        return Convey.convey2Legal(self.engine)


class ConveyTwiceSecondOrder(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = action_family_2
        self.action_details = "Second Order"

    def execute(self):
        Convey.convey(self.engine, self.player, 2, 1)

    def check(self) -> bool:
        return Convey.convey2Legal(self.engine)
