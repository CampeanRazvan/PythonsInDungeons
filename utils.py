import os
import winsound
import enemy
import random
import character
from colors import Use_colors

class Item:
    def __init__(self, name, type, description, prop):
        self.name = name
        self.type = type
        self.description = description
        self.prop = prop





class Utils:

    @staticmethod
    def intro_message():
        sound = 'Main_Menu.wav'
        # the sound will play in a loop and async
        winsound.PlaySound(sound, winsound.SND_ASYNC + winsound.SND_LOOP)
        intro_message = Use_colors.BOLD + Use_colors.BLUE + """ 
       ***************************************************************************************
                                         Welcome stranger,
         Here in Hinderlands, you'll get to fight dragons and conquer the deadliest dungeons.
         In a country where magic rules, anything is possible if you wish so.
                                It all depends on you, brave hero!
       ***************************************************************************************
        """ + Use_colors.ENDC
        return intro_message

    @staticmethod
    def world_intro():
        sound = 'Exploring.wav'
        # the sound will play in a loop and async
        winsound.PlaySound(sound, winsound.SND_ASYNC + winsound.SND_LOOP)
        os.system('cls')
        world_intro_message =Use_colors.BLUE +Use_colors.BOLD + "The Hinderlands are in grave danger and only you can stand a chance against the enemy armies"+ Use_colors.ENDC
        print(Use_colors.BLUE + f"""******************************************************************************************
{world_intro_message}""" + Use_colors.BLUE  +"""
********************************************************************************************** """ + Use_colors.ENDC)

        crossroad_options = ('village', 'forest', 'desert')
        print("You are at a crossroads with 3 possible paths:")
        index = 1
        for option in crossroad_options:
            print(f'{index}.{option}')
            index += 1
        try:
            chosen_path = int(input("\nChoose your destiny: 1,2 or 3? -> "))
            if chosen_path == 1:
                Utils.village()
            elif chosen_path == 2:
                Utils.forest()
            elif chosen_path == 3:
                Utils.desert()
            else:
                print("Incorrect choice")
        except ValueError:
            print("Only numbers are accepted")
        else:
            return chosen_path



    # @staticmethod
    # def warrior_name():
    #     warrior_name = input("Welcome mighty warrior , what's your ? -> ")
    #     warrior = character.Warrior(warrior_name)
    #
    #     return warrior










    @staticmethod
    def village():
        os.system('cls')
        village_intro_message = "\t\t\tYour adventure starts in the village of Bannockburn\n"
        print(village_intro_message)

        return

    @staticmethod
    def forest():
        os.system('cls')
        forest_intro_message = "\t\t\tYour adventure starts in the Wolfbel forest\n"
        print(forest_intro_message)

        return

    @staticmethod
    def desert():
        os.system('cls')
        desert_intro_message = "\t\t\tYour adventure starts in the Dead Wasteland\n"
        print(desert_intro_message)

        return

    @staticmethod
    def game_start():
        start_option = input("Ready to begin your adventure?" + Use_colors.GREEN + "Yes" + Use_colors.ENDC +
                             "/" + Use_colors.RED + "No" + Use_colors.ENDC + " -> ")

        if start_option.strip() in ['Y', "Yes", "yes", "y", "YES"]:
            os.system('cls')
            print("To start your quest, please select your fighter:")
            print(Use_colors.RED + Use_colors.BOLD + "1.Warrior" + Use_colors.ENDC)
            print(Use_colors.BLUE + Use_colors.BOLD + "2.Wizard" + Use_colors.ENDC)
            print(Use_colors.GREEN + Use_colors.BOLD + "3.Ranger" + Use_colors.ENDC)


        elif start_option.strip() in ["N", "n", "no", "NO", "No"]:
            print("Goodbye")
        else:
            print(
                Use_colors.BOLD + Use_colors.RED + "Incorrect choice , please choose a valid option" + Use_colors.ENDC)
        return







            #             chosen_fighter = int(input("What's your choice: ? -> "))
        #             if chosen_fighter == 1:
        #
        #
        #                 Utils.world_intro()
        #                 Utils.first_battle()
        #
        #
        #             elif chosen_fighter == 2:
        #
        #                 Utils.world_intro()
        #             elif chosen_fighter == 3:
        #
        #                 Utils.world_intro()
        #
        #
        #             else:
        #                 print("Incorrect choice! please input a valid choice")
        #         elif start_option.strip().upper() == 'N':
        #             game_start = False
        #
        #         else:
        #             print("Incorrect choice")
        # except ValueError:
        #     print("Only numbers are accepted")
        # else:
        #     print()
        # return

    @staticmethod
    def generate_damage_warrior(self):
        warrior_attack = random.randrange(self.attack_low, self.attack_high) * 1.1
        print(warrior_attack)
        return warrior_attack



    @staticmethod
    def first_battle():


        running = True
        while running:


            character.Player.get_stats(character.Warrior.warrior_name())
            character.Player.choose_action(character.Warrior.warrior_name())
            print(" You are under attack , this are your option ")


            choice = input("    Choose action: ->")
            index = int(choice) - 1
            if index == 0:
                damage = character.Player.generate_damage(character.Warrior.warrior_name())
                print(damage)
                print("You attacked for", damage, "points of damage . Enemy HP:", enemy.Enemy.get_hitpoints(Utils.random_enemy()))
            elif index == 1:
                 character.Player.choose_magic()
                 magic_choice = int(input("Choose magic:")) - 1
                 spell = character.Player.magic[magic_choice]
                 magic_damage = spell.generate_damage()
                 curent_mana = character.Player.get_mana()
                 if magic_choice == -1:
                      continue

                 if spell.cost > curent_mana:
                     print(Use_colors.RED + "\n Not enough mana" + Use_colors.ENDC)
                     continue
                 character.Player.reduce_mana(spell.cost)

                 if spell.type == "white":
                    character.Player.heal(magic_damage)
                    print(Use_colors.BLUE + "\n" + spell.name + " heals for", str(magic_damage),
                          "HP." + Use_colors.ENDC)

                 elif spell.type == "black":

                    enemy.take_damage(magic_damage)
                    print(character.Player.BLUE + "\n" + spell.name + " deals", str(magic_damage),
                        "points of damage" + Use_colors.ENDC)

            elif index == 2:

                character.Player.choose_item()
                item_choice = int(input("Chose item ->")) - 1

                if item_choice == -1:
                     continue
                item = character.Player.items[item_choice]["item"]
                if character.Player_items[item_choice]["quantity"] == 0:
                    print(Use_colors.RED+ "\n" + "None left..." + Use_colors.ENDC)
                    continue

                character.Player.items[item_choice]["quantity"] -= 1

                if item.type == "potion":
                    character.Player.heal(item.prop)
                    print(Use_colors.GREEN + "\n" + item.name + "heals for", str(item.prop),
                          Use_colors.ENDC)
                elif item.type == "elixer":
                    character.Player.hitpoints = character.Player.max_hitpoints
                    character.Player.mana = character.Player.max_mana
                    print(Use_colors.GREEN + "\n" + item.name + "fully restore HP/MP" + Use_colors.ENDC)
                elif item.type == "atack":
                    enemy.take_damage(item.prop)
                    print(Use_colors.RED + "\n", + item.name + " deals", str(item.prop),
                              " points of damage " + Use_colors.ENDC)
            enemy_choice = 1

            enemy_damage = enemy.generate_damage()
            character.Player.take_damage(enemy_damage)
            print("Enemy attacks for", enemy_damage, "Player HP:", character.Player.get_hitpoints())

            print("___________________________________")
            # print("Enemy HP:", battle_colors.FAIL + str(enemy.get_hitpoints()) + "/" + str(enemy.get_max_hitpoints()) + battle_colors.ENDC + "\n" )
            # print("Your HP:", battle_colors.OKGREEN + str(player.get_hitpoints()) + "/" + str(player.get_max_hitpoints()) + battle_colors.ENDC )

            print("Your mana: ", Use_colors.BLUE + str(character.Player.get_mana()) + "/" + str(
                character.Player.get_max_mana()) + Use_colors.ENDC + "\n")
            if enemy.get_hitpoints() == 0:
                print(Use_colors.GREEN + "You WIN!" + Use_colors.ENDC)
            elif character.Player.get_hitpoints() == 0:
                print(Use_colors.RED + "You are ded! " + Use_colors.ENDC)
                running = False