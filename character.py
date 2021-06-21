


class Player:
    def __init__(self, name, life_points, mana_points, attack, defence, magic, items):
        self.name = name
        self.life_points = life_points
        self_mana_points











# import random
#
# from colors import Use_colors
#
# class Player:
#     def __init__(self, name, hitpoints, mana , attack, defence, magic, items):
#         self.name = name
#         self.atack = attack
#         self.full_hitpoints = hitpoints
#         self.hitpoints = hitpoints
#         self.mana = mana
#         self.full_mana = mana
#         self.attack_low = attack - 10
#         self.attack_high = attack + 10
#         self.defence = defence
#         self.magic = magic
#         self.items = items
#         self.clas = ["Wizard", "Warrior", "Ranger"]
#         self.actions = ["Attack", "Magic", "Items" ]
#         self.spells = ["Fire", "Thunder"]
#
#
#
#
#
#     def generate_damage(self):
#         return random.randrange(self.attack_low, self.attack_high)
#
#     def take_damage(self, damage):
#         self.hitpoints -= damage
#         if self.hitpoints < 0:
#             self.hitpoints = 0
#         return self.hitpoints
#
#     def get_hitpoints(self):
#         return self.hitpoints
#
#     def heal(self, damage):
#         self.hitpoints += damage
#         if self.hitpoints > self.full_hitpoints:
#             self.hitpoints = self.full_hitpoints
#
#     def get_max_hitpoints(self):
#         return self.full_hitpoints
#
#     def get_mana(self):
#         return self.mana
#
#     def get_max_mana(self):
#         return self.full_mana
#
#     def reduce_mana(self, cost):
#         self.mana -= cost
#
#     # def get_spell_name(self, i):
#     #     return self.magic[i]['name']
#
#     # def get_spell_mana_cost(self, i):
#     #     return self.magic[i]["cost"]
#
#     def choose_action(self):
#         i = 1
#         print("\n" + "           " + Use_colors.BOLD + self.name + Use_colors.ENDC)
#         print(Use_colors.BLUE + Use_colors.BOLD + "    ACTIONS" + Use_colors.ENDC)
#         for item in self.actions:
#             print("        " + str(i) + '.', item)
#             i += 1
#
#     def choose_magic(self):
#         i = 1
#
#         print("\n" + "       " +  Use_colors.BLUE + Use_colors.BOLD + "     MAGIC" + Use_colors.ENDC)
#         for spell in self.magic:
#             print("        " + str(i) + ".", str(spell.name), '(cost:', str(spell.cost) + ')' )
#             i += 1
#
#     def choose_item(self):
#         i = 1
#         print("\n" + Use_colors.GREEN + Use_colors.BOLD + "     ITEMS" + Use_colors.ENDC)
#         for item in self.items:
#             print("            " + str(i) + ".", item["item"].name, ":", item["item"].description, " x" + str(item["quantity"]))
#             i += 1
#
#
#     def get_stats(self):
#         print("                 ____________________        __________ ")
#         print(Use_colors.BOLD + self.name + "    " +
#               str(self.hitpoints) + "/" + str(self.full_hitpoints) + " |" + Use_colors.GREEN + "██████████████          " + Use_colors.ENDC + "|" +
#               str(self.mana) + "/" + str(self.full_mana) + Use_colors.BLUE + " |" + "██████████" + Use_colors.ENDC)
#
#
# class Warrior(Player):
#
#     def __init__(self,name):
#         super().__init__(name, 100,  50, 25, 15, "", "")
#
#     def generate_damage_warrior(self):
#         warrior_attack = random.randrange(self.attack_low, self.attack_high) * 1.1
#         print(warrior_attack)
#         return warrior_attack
#
#     @staticmethod
#     def warrior_name():
#         warrior_name = input("Welcome mighty warrior , what's your ? -> ")
#         warrior = Warrior(warrior_name.strip())
#
#         return warrior
#
#     @staticmethod
#     def choose_wizard():
#         wizard_name = input("\nYour powerful wizard needs a name -> ")
#         wizard = Wizard(wizard_name.strip())
#         return wizard
#
#     @staticmethod
#     def choose_ranger():
#         ranger_name = input("\nYour powerful ranger needs a name -> ")
#         ranger = Ranger(ranger_name.strip())
#         return ranger
#
# class Wizard(Player):
#
#     def __init__(self,name):
#         super().__init__(name, 100,  50, 25, 15, "" , "" )
#
#
# class Ranger(Player):
#
#     def __init__(self,name):
#         super().__init__(name, 100,  50, 25, 15, "", "")
#
#
#
#
#
