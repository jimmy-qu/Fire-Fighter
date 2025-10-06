import random
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class tree():
    def __init__(self):
        self.state = True  # True means not on fire, False means on fire

def TreeStatus(Forest):
    for i in range(len(Forest)):
        if Forest[i].state:
            print(f"Tree {i+1} is not on fire")
        else:
            print(f"Tree {i+1} is on fire")

def win_condition(Forest):
    return all(t.state for t in Forest)

def Forest_Simulator(Forest):
    while not win_condition(Forest):
        for i in range(len(Forest)):
            print("--------------------------------------------------")
            print(f"You are on Tree {i+1}\n")
            TreeStatus(Forest)
            if not Forest[i].state:
                print("Firefighter's turn")
                print("Do you want to put out the fire? (y/n): ")
                answer = input()
                if answer == 'y':
                    Forest[i].state = True
                else:
                    print("Not putting out the fire")

            else:
                print("Pyromaniac's turn")
                print("Do you want to ignite the fire? (y/n): ")
                answer = input()
                if answer == 'y':
                    Forest[i].state = False
                else:
                    print("Not igniting the fire")
                    

            ## end early if win condition is met
            if win_condition(Forest):
                break

if __name__ == "__main__":
    print("Firefighter and Pyromaniac Simulation")
    print("How many trees: ")
    tree_count = int(input())

    Forest = [tree() for _ in range(tree_count)]

    print(f"How many trees are on fire given {len(Forest)} trees: ")
    start_fire = int(input())
    while start_fire > len(Forest):
        print("Number of trees on fire cannot exceed total number of trees. Please enter again:")
        start_fire = int(input())
        if start_fire < 1:
            print("Number of trees on fire must be at least 1. Please enter again:")
            start_fire = int(input())

    
    for x in range(start_fire):
        while not Forest[x].state:
            x = random.randint(0, len(Forest)-1)
        Forest[x].state = False
    
    Forest_Simulator(Forest)

    print("--------------------------------------------------")
    print("All fires have been removed! You win!")