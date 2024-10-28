#TBC MODULE PSEUDOCODE

#import random module
import random
#define new function for main
def main():
#make fight function for character and monster to fight
def fight():
#character and monster fight

#if monster dies print character wins
if monster.hitPoints = 0:
    print ("character wins")
#if character dies print monster wins
if character.hitPoints = 0:
    print ("monster wins")
#end game
break
#Create new object called Character
class Character:
#create Character name
    self.name = name
#Character properties
def __init__():
#Property for Character called hitPoints, must be an integer, can be negative, no maximum or minimum value 
    self.hitPoints = hitPoints
#Property for Character called hitChance, percent chance a hit will land, must be an integer, cannot be negative, must be between 0 and 100
    self.hitChance = hitChance
#Property for Character called maxDamage, must be an integer, cannot be negative, no maximum or minimum value
    self.maxDamage = maxDamage
#Property for Character called armor, must be an integer, cannot be negative, no max or min value
    self.armor = armor
#function to print character stats
def printStats():
#Print character properties

#print character name 
    print (f"{self.name}")
#print hitPoints integer
    print (f"hit points: {self.hitPoints}")
#print hitChance percentage
    print (f"hit chance: {self.hitChance}")
#print maxDamage integer
    print (f"max damage: {self.maxDamage}")
#print armor integer
    print (f"armor: {self.armor}")
#function for characters to hit eachother
def hit
#Successful hit is based on character hitChance
    self.hitChance
#print character hit lands if hit is successful
    print("hit lands")
#damage is random integer between 1 and maxDamage
    damage = random.randint(1, self.maxDamage)
#totalDamage is damage - armor
    totalDamage = damage - self.armor
#hitPoints is hitPoints - totalDamage
    hitPoints = self.hitPoints - totalDamage
#otherwise print hit missed
    print("hit missed")
