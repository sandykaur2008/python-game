from engine import Engine
from planisphere import Map

a_map = Map('observation_room')
a_game = Engine(a_map)
a_game.play()