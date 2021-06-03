import os
introMsg = """
****************************************************************************************
* Welcome,stranger.                                                                    * 
* Here in Hinderlands, you'll get to fight dragons and conquer the deadliest dungeons. * 
* In a country where magic rules, anything is possible if you wish so.                 * 
* It all depends on you, brave hero.                                                   * 
********************************************************************************
"""

print(introMsg)
print("Do you want to start the adventure?")
user_answer = input("Yes or No ->")
if user_answer.upper() == "YES":
    print("ok")
    os.system('cls')  # windows
    #os.system('cls')
    print("")
else:
    print("Good bye")

