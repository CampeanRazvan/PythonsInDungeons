import os
import winsound
import Player

import Enemy
import utils
import random


introMsg = """
****************************************************************************************
* Welcome,stranger.                                                                    * 
* Here in Hinderlands, you'll get to fight dragons and conquer the deadliest dungeons. * 
* In a country where magic rules, anything is possible if you wish so.                 * 
* It all depends on you, brave hero.                                                   * 
********************************************************************************
 """


print(introMsg)
sound = "Main_Menu.wav"
winsound.PlaySound(sound,winsound.SND_ASYNC)
print("Do you want to start the adventure?")
user_answer = input("Yes or No ->")
if user_answer.upper() == "YES":
    print("ok")

    os.system('cls')  # windows
    #os.system('cls')
    print("")
    player_answer = input("""Chose your class -> :
1 for Warrior
2 for Wizard
3 for Ranger
->
  """)
    if player_answer == "1":
        print(   "An Enemy Attacks!" )
        player_name = input("What is your name brave warrior ? ->")
        player = Player.Warrior(player_name)
        print("Intro to the road")
        input("Press a key to continue ...")
        os.system('cls')
        sound = "Exploring.wav"
        winsound.PlaySound(sound, winsound.SND_ASYNC)
        print("""Yo are in the middle of a crossroads.
You have 3 paths in front of you :
1. Going to a village
2. Going to a forest 
3. Going to a desert """)
        path_option = input("Chose your path ->")

        """Create a method path
        that uses the returned value from crossroads method """

        if path_option == "1":
            print("You enter in the village")
            # chemam functia in_the_village
            print("From a backside street a enemy appears")

            sound = "BattleFinal.wav"
            winsound.PlaySound(sound, winsound.SND_ASYNC)
            random_number = random.randint(0,2)
            if random_number == 0:
                enemy = Enemy.Goblin()
            elif random_number == 1:
                enemy = Enemy.Orc()
            elif random_number == 2:
                enemy = Enemy.Rat()

        elif path_option == "2":
            print("You enter in the forest")
            # chemam functia in_the_forest
        elif path_option == "3":
            print("You enter in the desert")
            # chemam functia in_the_desert
        else:
            print("Path not available")

    elif player_answer == "2":
        player_name = input("What is your name brave wizard ? ->")
        player = Player.Wizard(player_name)

    else:
        print("Chose a valid option")
else:
    print("Good bye")


