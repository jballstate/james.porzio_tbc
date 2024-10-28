#COMBAT.PY PSEUDOCODE

#import tbc module 
import tbc
#define new function for main
def main():
#guy gets tbc.character
    guy = tbc.Character()
#guy name is strongguy
    guy.name = "strongguy"
#guy hitPoints is 30
    guy.hitPoints = 30
#guy hitChance is 70
    guy.hitChance = 70
#guy maxDamage is 10
    guy.maxDamage = 10
#guy armor is 4
    guy.armor = 2
#monster gets tbc.character
    monster = tbc.Character ("monster", 50, 20, 12, 1)
#monster hitPoints is 50

#monster hitChance is 20

#monster maxDamage is 12

#monster armor is 1

#print stats for guy
guy.printStats()
#print stats for monster
monster.printStats()
#run fight from tbc module
tbc.fight(guy, monster)
#if name is main, call main function to start game
if __name__ == "__main__":
    main()
