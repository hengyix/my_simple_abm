# Hengyi Xing
from numpy import random

class Agent():
    def __init__(self):
        self.agents = ['Agent' + str(num) for num in range(1, 6)] # 5 agents

    def init_loc(self, world):
        random.shuffle(world.locations)
        # use dictionary to map agents to locations
        # random choice
        self.loc = {self.agents[i]: world.locations[i] for i in range(5)}
        
    def move(self, world):
        for agent, location in self.loc.items():
            random.shuffle(world.vacant)  
            new_location = world.vacant[0]  # random choice
            self.loc[agent] = new_location  # update location to avoid overlap
            world.find_vacant()  # get new vacant spots
        
class World():
    def __init__(self):
        grid = [(i, j) for i in range(10) for j in range(10)]
        self.locations = grid # 10x10 grid
    
    def find_vacant(self):
        occupied_patch = list(self.agent.loc.values()) 
        self.vacant = [loc for loc in self.locations if loc not in occupied_patch]

    def run(self, loop):
        self.agent = Agent()
        self.agent.init_loc(self) # initialization
        print('Initial Setting:', self.agent.loc)
        self.find_vacant()
        for n in range(loop):
            self.agent.move(self)
            print(f'Movement {n+1}:', self.agent.loc)
            
world = World()
world.run(5)

