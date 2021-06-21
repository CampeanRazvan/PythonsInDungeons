
import os
import winsound
import utils
from Player import Player
from utils import Mesaje
from utils import Use_colors
from utils import Utils




Mesaje.intro()
sound = "Main_Menu.wav"
winsound.PlaySound(sound,winsound.SND_ASYNC)
print(Use_colors.BOLD + Use_colors.RED + "Do you want to start the adventure?" + Use_colors.ENDC)

Player.choose_character()
