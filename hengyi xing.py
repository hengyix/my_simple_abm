#Hengyi Xing
from numpy import random

class Agent():
    def __init__(self):
        agents = ['Agent'+str(num) for num in range(1,6)]
        self.agents = agents
    
    def init_loc(self, world):
        random.shuffle(world.locations)
        init_loc = [{self.agents[i]:world.locations[i]} for i in range(0, 5)]
        self.loc = init_loc
        
    def move(self, world):
        random.shuffle(world.vacant)
        move_result = [{self.agents[i]:world.vacant[i]} for i in range(0, 5)]
        self.loc= move_result
        
        
class World():
    def __init__(self):
        pass
    
    def build_grid(self):
        locations = [(i,j) for i in range(0,10) for j in range(0,10)]
        self.locations = locations
        
    def find_vacant(self, agent):
        occupied_patch = []
        for element in agent.loc:
            occupied_patch.append(element.values())
        world.occupied = occupied_patch
        vacant_patch = [patch for patch in self.locations if patch not in self.occupied]
        world.vacant = vacant_patch
        
    def run(self, loop):
        agent = Agent()
        world.build_grid()
        agent.init_loc(world)
        print(f'Initial Setting: {agent.loc}')
        world.find_vacant(agent)
        print(f'Moving {loop} times here:')
        for n in range(0, loop):            
            agent.move(world)
            print(agent.loc) 
            
world = World()
world.run(5)
