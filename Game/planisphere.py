import scenes

class Map(object):
    scenes = {'death': scenes.Death(), 
    'observation_room': scenes.ObservationRoom(),
    'main_corridor': scenes.MainCorridor(),
    'control_room': scenes.ControlRoom(),
    'bomb_room': scenes.BombRoom(),
    'escape_pod': scenes.EscapePod(),
    'the_end': scenes.TheEnd()}

    def __init__(self, start_scene):
        self.start_scene = start_scene
    
    def next_scene(self):
        next_up = Map.scenes.get(self.start_scene)
        return next_up