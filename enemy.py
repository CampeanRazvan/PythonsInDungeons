import os
import winsound
import random
import character
from colors import Use_colors



class Enemy:
    def __init__(self,name, hitpoints, mana, attack, defence, magic, items):
        self.name = name
        self.atack = attack
        self.full_hitpoints = hitpoints
        self.hitpoints = hitpoints
        self.mana = mana
        self.full_mana = mana
        self.attack_low = attack - 10
        self.attack_high = attack + 10
        self.defence = defence
        self.magic = magic
        self.items = items
        self.clas = ["Wizard", "Warrior", "Ranger"]
        self.actions = ["Attack", "Magic", "Items"]


    def take_damage(self, damage):
        self.hitpoints -= damage
        if self.hitpoints < 0:
            self.hitpoints = 0
        return self.hitpoints

    def get_hitpoints(self):
        return self.hitpoints

    def heal(self, damage):
        self.hitpoints += damage
        if self.hitpoints > self.full_hitpoints:
            self.hitpoints = self.full_hitpoints

    def get_max_hitpoints(self):
        return self.full_hitpoints

    def get_mana(self):
        return self.mana

    def get_max_mana(self):
        return self.full_mana

    def reduce_mana(self, cost):
        self.mana -= cost

    # def get_spell_name(self, i):
    #     return self.magic[i]['name']

    # def get_spell_mana_cost(self, i):
    #     return self.magic[i]["cost"]

    def choose_action(self):
        i = 1
        print("\n" + "           " + Use_colors.BOLD + self.name + Use_colors.ENDC)
        print(Use_colors.BLUE + Use_colors.BOLD + "    ACTIONS" + Use_colors.ENDC)
        for item in self.actions:
            print("        " + str(i) + '.', item)
            i += 1

    def choose_magic(self):
        i = 1
        # print(self.magic)
        # for i in self.magic:
        #     print(i.name)
        # return False
        print("\n" + "       " + Use_colors.BLUE + Use_colors.BOLD + "     MAGIC" + Use_colors.ENDC)
        for spell in self.magic:
            print("        " + str(i) + ".", spell.name, '(cost:', str(spell.cost) + ')')
            i += 1

    def choose_item(self):
        i = 1
        print("\n" + Use_colors.GREEN + Use_colors.BOLD + "     ITEMS" + Use_colors.ENDC)
        for item in self.items:
            print("            " + str(i) + ".", item["item"].name, ":", item["item"].description,
                  " x" + str(item["quantity"]))
            i += 1

    def get_stats(self, ):

        print(Use_colors.BOLD + str(self.name) +
              str(self.hitpoints) + "/" + str(self.full_hitpoints) + " |" + Use_colors.GREEN + "██████████████          " + Use_colors.ENDC + "|" +
              str(self.mana) + "/" + str(self.full_mana) + Use_colors.BLUE + " |" + "██████████" + Use_colors.ENDC)

    @staticmethod
    def random_enemy():
        sound = 'BattleFinal.wav'
        # the sound will play in a loop and async
        winsound.PlaySound(sound, winsound.SND_ASYNC + winsound.SND_LOOP)
        random_number = random.randint(0, 2)
        if random_number == 0:
            goblin = Goblin()
            return goblin

        elif random_number == 1:
            orc = Orc()
            return orc

        elif random_number == 2:
            wrath = Wrath()
            return wrath


class Goblin(Enemy):
    def __init__(self):
        super().__init__(Goblin , 90, 30, 9, 11,  "", "")
        print("""\nI'm a vengeful goblin.
My poisonous arrows will pierce you!""")

    def get_stats(self, ):

        print(Use_colors.BOLD + str(self.name) +
              str(self.hitpoints) + "/" + str( self.full_hitpoints) + " |" + Use_colors.GREEN + "██████████████   " + Use_colors.ENDC + "|" +
              str(self.mana) + "/" + str(self.full_mana) + Use_colors.BLUE + " |" + "██████████" + Use_colors.ENDC)


    def generate_damage(self):
        return random.randrange(self.attack_low, self.attack_high)

    def take_damage(self, damage):
        self.hitpoints -= damage
        if self.hitpoints < 0:
            self.hitpoints = 0
        return self.hitpoints

    def get_hitpoints(self):
        return self.hitpoints

    def heal(self, damage):
        self.hitpoints += damage
        if self.hitpoints > self.full_hitpoints:
            self.hitpoints = self.full_hitpoints

    def get_max_hitpoints(self):
        return self.full_hitpoints

    def get_mana(self):
        return self.mana

    def get_max_mana(self):
        return self.full_mana

    def reduce_mana(self, cost):
        self.mana -= cost

    # def get_spell_name(self, i):
    #     return self.magic[i]['name']

    # def get_spell_mana_cost(self, i):
    #     return self.magic[i]["cost"]

    def choose_action(self):
        i = 1
        print("\n" + "           " + Use_colors.BOLD + self.name + Use_colors.ENDC)
        print(Use_colors.BLUE + Use_colors.BOLD + "    ACTIONS" + Use_colors.ENDC)
        for item in self.actions:
            print("        " + str(i) + '.', item)
            i += 1

    def choose_magic(self):
        i = 1
        # print(self.magic)
        # for i in self.magic:
        #     print(i.name)
        # return False
        print("\n" + "       " + Use_colors.BLUE + Use_colors.BOLD + "     MAGIC" + Use_colors.ENDC)
        for spell in self.magic:
            print("        " + str(i) + ".", spell.name, '(cost:', str(spell.cost) + ')')
            i += 1

    def choose_item(self):
        i = 1
        print("\n" + Use_colors.GREEN + Use_colors.BOLD + "     ITEMS" + Use_colors.ENDC)
        for item in self.items:
            print("            " + str(i) + ".", item["item"].name, ":", item["item"].description,
                  " x" + str(item["quantity"]))
            i += 1


class Orc(Enemy):
    def __init__(self):
        super().__init__(Orc , 100, 50, 15, 9, "", "")
        print("""\nI'm the Dark Lord orc captain.
Your head will be my trophy!""")

    def generate_damage(self):
        return random.randrange(self.attack_low, self.attack_high)

    def get_stats(self, ):

        print(Use_colors.BOLD + str(self.name) +
              str(self.hitpoints) + "/" + str(
            self.full_hitpoints) + " |" + Use_colors.GREEN + "██████████████          " + Use_colors.ENDC + "|" +
              str(self.mana) + "/" + str(self.full_mana) + Use_colors.BLUE + " |" + "██████████" + Use_colors.ENDC)

    def take_damage(self, damage):
        self.hitpoints -= damage
        if self.hitpoints < 0:
            self.hitpoints = 0
        return self.hitpoints

    def get_hitpoints(self):
        return self.hitpoints

    def heal(self, damage):
        self.hitpoints += damage
        if self.hitpoints > self.full_hitpoints:
            self.hitpoints = self.full_hitpoints

    def get_max_hitpoints(self):
        return self.full_hitpoints

    def get_mana(self):
        return self.mana

    def get_max_mana(self):
        return self.full_mana

    def reduce_mana(self, cost):
        self.mana -= cost

    # def get_spell_name(self, i):
    #     return self.magic[i]['name']

    # def get_spell_mana_cost(self, i):
    #     return self.magic[i]["cost"]

    def choose_action(self):
        i = 1
        print("\n" + "           " + Use_colors.BOLD + self.name + Use_colors.ENDC)
        print(Use_colors.BLUE + Use_colors.BOLD + "    ACTIONS" + Use_colors.ENDC)
        for item in self.actions:
            print("        " + str(i) + '.', item)
            i += 1

    def choose_magic(self):
        i = 1
        # print(self.magic)
        # for i in self.magic:
        #     print(i.name)
        # return False
        print("\n" + "       " + Use_colors.BLUE + Use_colors.BOLD + "     MAGIC" + Use_colors.ENDC)
        for spell in self.magic:
            print("        " + str(i) + ".", spell.name, '(cost:', str(spell.cost) + ')')
            i += 1

    def choose_item(self):
        i = 1
        print("\n" + Use_colors.GREEN + Use_colors.BOLD + "     ITEMS" + Use_colors.ENDC)
        for item in self.items:
            print("            " + str(i) + ".", item["item"].name, ":", item["item"].description,
                  " x" + str(item["quantity"]))
            i += 1


class Wrath(Enemy):
    def __init__(self):
        super().__init__( Wrath, 100, 50, 15, 10 ,"", "")
        print("""\nI'm one of the nine dead kings."
You are no match to my powers!""")

    def generate_damage(self):
        return random.randrange(self.attack_low, self.attack_high)

    def get_stats(self, ):

        print(Use_colors.BOLD + str(self.name) +
              str(self.hitpoints) + "/" + str(self.full_hitpoints) + " |" + Use_colors.GREEN + "██████████████          " + Use_colors.ENDC + "|" +
              str(self.mana) + "/" + str(self.full_mana) + Use_colors.BLUE + " |" + "██████████" + Use_colors.ENDC)

    def take_damage(self, damage):
        self.hitpoints -= damage
        if self.hitpoints < 0:
            self.hitpoints = 0
        return self.hitpoints

    def get_hitpoints(self):
        return self.hitpoints

    def heal(self, damage):
        self.hitpoints += damage
        if self.hitpoints > self.full_hitpoints:
            self.hitpoints = self.full_hitpoints

    def get_max_hitpoints(self):
        return self.full_hitpoints

    def get_mana(self):
        return self.mana

    def get_max_mana(self):
        return self.full_mana

    def reduce_mana(self, cost):
        self.mana -= cost

    # def get_spell_name(self, i):
    #     return self.magic[i]['name']

    # def get_spell_mana_cost(self, i):
    #     return self.magic[i]["cost"]

    def choose_action(self):
        i = 1
        print("\n" + "           " + Use_colors.BOLD + self.name + Use_colors.ENDC)
        print(Use_colors.BLUE + Use_colors.BOLD + "    ACTIONS" + Use_colors.ENDC)
        for item in self.actions:
            print("        " + str(i) + '.', item)
            i += 1

    def choose_magic(self):
        i = 1
        # print(self.magic)
        # for i in self.magic:
        #     print(i.name)
        # return False
        print("\n" + "       " + Use_colors.BLUE + Use_colors.BOLD + "     MAGIC" + Use_colors.ENDC)
        for spell in self.magic:
            print("        " + str(i) + ".", spell.name, '(cost:', str(spell.cost) + ')')
            i += 1

    def choose_item(self):
        i = 1
        print("\n" + Use_colors.GREEN + Use_colors.BOLD + "     ITEMS" + Use_colors.ENDC)
        for item in self.items:
            print("            " + str(i) + ".", item["item"].name, ":", item["item"].description,
                  " x" + str(item["quantity"]))
            i += 1