import scenes
from planisphere import Map

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map
    def play(self):
        current_scene = self.scene_map.next_scene()
        last_scene = scenes.TheEnd()
        
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = Map(next_scene_name).next_scene()

        return current_scene.enter()

        