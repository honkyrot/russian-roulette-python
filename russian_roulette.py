# Author: Hong "Honkyrot" Rot
# Created on July 7, 2024

# A game of russian roulette in python
# special effects are done by manipulating the terminal window

# get packages
import time
import random

# import window manipulation python file
import window_manipulation

# game start

def intro():
    """intro"""
    print("Welcome to Russian Roulette!")
    print("You will be playing against the computer.")
    print("Good luck!\n")

intro()

# create window manipulation object
wm = window_manipulation.WindowManipulation()

class Game():
    """A class to represent the game of Russian Roulette, will contain all the game logic"""

    def __init__(self):
        # game variables
        self.bullets = 1 # number of bullets currently chambered
        self.bullet_position = [1, 0, 0, 0, 0, 0] # position of the bullet in the chambers [1, 0, 0, 0, 0, 0] means the bullet is in the first chamber
        self.chamber = 1 # current chamber where the hammer is (1-6)
        self.chamber_max = 6 # number of chambers in the revolver (6 for a standard revolver, more for some reason)
        self.clicks = 0 # number of clicks the gun has made
        self.player_turn = True # player's turn or computer's turn
        self.player_alive = True # self explanatory
        self.enemy_alive = True 
        
        # stat tracking
        self.shots_fired = 0
        self.shots_hit = 0
        self.chamber_spun = 0

        # enemy stats
        self.enemy_shots_fired = 0
        self.enemy_shots_hit = 0
        self.enemy_chamber_spun = 0

        # enemy name
        self.enemy_name = "Your opponent"

        # window manipulation class


    def spin_chamber(self):
        """spin the chamber"""
        self.chamber = random.randint(1, self.chamber_max)
        self.chamber_spun += 1
        self.clicks = 0 # reset clicks

    def cycle_chamber(self):
        """cycle the chamber"""
        self.chamber += 1
        if self.chamber > self.chamber_max:
            self.chamber = 1

    def player_shoot(self):
        """player shoots"""
        self.cycle_chamber() # cycle the chamber
        self.clicks += 1

        # shoot
        if self.bullet_position[self.chamber - 1] == 1:
            wm.shake_window()

            time.sleep(2)

            print("You died!")
            self.player_alive = False
            self.shots_hit += 1
        else:
            print("You survived!")
        self.shots_fired += 1

    def computer_shoot(self):
        """computer shoots"""
        self.cycle_chamber() # cycle the chamber
        self.clicks += 1

        # shoot
        if self.bullet_position[self.chamber - 1] == 1:
            wm.shake_window()

            time.sleep(1)

            print(f"{self.enemy_name} died!")
            self.enemy_alive = False
            self.shots_hit += 1
        else:
            print(f"{self.enemy_name} survived!")
        self.shots_fired += 1

    def reset_game(self):
        """reset the game"""
        self.bullets = 1
        self.bullet_position = [1, 0, 0, 0, 0, 0]
        self.chamber = 1
        self.clicks = 0
        self.player_turn = True
        self.player_alive = True
        self.enemy_alive = True
        self.shots_fired = 0
        self.shots_hit = 0
        self.chamber_spun = 0
        self.enemy_shots_fired = 0
        self.enemy_shots_hit = 0
        self.enemy_chamber_spun = 0

# run the game
game = Game()
game_active = True

while game_active:
    game.reset_game()
    # create game
    # game loop
    while game.player_alive and game.enemy_alive:
        # player turn
        if game.player_turn:
            print("\nPlayer's turn")
            player_input = input("[S]hoot or S[p]in the chamber: ").lower()
            
            if player_input == "s":
                print("Shooting...")
                time.sleep(1)

                game.player_shoot()
                game.player_turn = False
            elif player_input == "p":
                print("Spinning...")
                time.sleep(1)

                game.spin_chamber()
                # player can spin the chamber as many times as they want
            elif player_input == "q":
                # secret quit command
                game_active = False
                break
            else:
                print("Invalid input")
        else:
            print(f"\n{game.enemy_name}'s turn")
            rng_spin = random.randint(1, 8) # 1 in 8 chance the computer will spin the chamber
            # or spin if clicks > 4
            if rng_spin == 1 or game.clicks > 4:
                print(f"{game.enemy_name} is spinning the chamber...")
                time.sleep(1)

                game.spin_chamber()
                game.enemy_chamber_spun += 1
            else:
                print(f"{game.enemy_name} decides to shoot.")
                time.sleep(1)

                game.computer_shoot()
                game.player_turn = True
        
        time.sleep(1)

    # game over
    print("\nGame over!")
    print(f"Player stats: {game.shots_fired} shots fired, {game.chamber_spun} chambers spun")
    print(f"{game.enemy_name} stats: {game.enemy_shots_fired} shots fired, {game.enemy_chamber_spun} chambers spun")

    # play again
    play_again = input("Play again? [Y/N]: ").lower()
    if play_again != "y":
        game_active = False
        print("Goodbye!")
    else:
        print("Restarting game...")
        time.sleep(1)
        for i in range(10):
            print("\n")
            time.sleep(0.01) 
        game_active = True