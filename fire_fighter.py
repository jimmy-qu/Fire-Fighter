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

## base class for tree
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

def Forest_Simulator_2P(Forest):
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

def CPU_Turn_Easy():
    # Choose to put tree on fire with 50% chance
    if random.choice([True, False]):
        print("Pyromaniac chose to ignite the fire")
        return False
    else:
        print("Pyromaniac chose not to ignite the fire")
        return True

def CPU_Turn_Medium(tree_index, Forest):
    
    # check total trees not on fire
    total_not_on_fire = sum(1 for t in Forest if t.state)
    if total_not_on_fire <= 1:
        print("Pyromaniac chose not to ignite the fire")
        return True
    elif Forest[tree_index+1].state == False or Forest[tree_index-1].state == False:
        print("Pyromaniac chose not to ignite the fire")
        return True
    else:
        print("Pyromaniac chose to ignite the fire")
        return False
    
    
def Forest_Simulator_1P(Forest, mode):
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
                if mode == "easy":
                    fire = CPU_Turn_Easy()
                else:
                    fire = CPU_Turn_Medium(i, Forest)
                Forest[i].state = fire
                

if __name__ == "__main__":

    ## Initial Setup
    print("Firefighter and Pyromaniac Simulation")
    print("How many trees: ")
    tree_count = int(input())
    Forest = [tree() for _ in range(tree_count)]

    ## Start with some trees on fire
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


    ## Choose Game Mode
    print("Single Player Mode OR Multi Player Mode, choose 1 or 2: ")
    mode = int(input())
    while mode not in [1, 2]:
        print("Invalid mode. Please choose 1 or 2: ")
        mode = int(input())

    ## Start Game Mode Single Player
    if mode == 1:

        ## Choose Difficulty
        print("Choose Difficulty: Easy or Medium (e/m): ")
        difficulty = input().lower()
        while difficulty not in ['e', 'm']:
            print("Invalid difficulty. Please choose e or m: ")
            difficulty = input().lower()

        print("Starting One Player Mode")

        if difficulty == 'e':
            Forest_Simulator_1P(Forest, mode="easy")
        else:
            Forest_Simulator_1P(Forest, mode="medium")
    else:
        print("Starting Two Player Mode")
        Forest_Simulator_2P(Forest)

    print("--------------------------------------------------")
    print("All fires have been removed! You win!")