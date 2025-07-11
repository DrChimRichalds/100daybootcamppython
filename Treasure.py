# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 09:09:42 2024

@author: charles.mullins
"""

print('''
                                ,-
                               ,'::|
                              /::::|
                            ,'::::o\                                      _..
         ____........-------,..::?88b                                  ,-' /
 _.--"""". . . .      .   .  .  .  ""`-._                           ,-' .;'
<. - :::::o......  ...   . . .. . .  .  .""--._                  ,-'. .;'
 `-._  ` `":`:`:`::||||:::::::::::::::::.:. .  ""--._ ,'|     ,-'.  .;'
     """_=--       //'doo.. ````:`:`::::::::::.:.:.:. .`-`._-'.   .;'
         ""--.__     P(       \               ` ``:`:``:::: .   .;'
                "\""--.:-.     `.                             .:/
                  \. /    `-._   `.""-----.,-..::(--"".\""`.  `:\
                   `P         `-._ \          `-:\          `. `:\
                                   ""            "            `-._)  -Seal
    
   '''   )
print("Welcome to Treasure Island. Your mission is to find the treasure")


#### Start where you come to a path
D1 = input("You come to a path. Left or right?:\n")

if D1 == "left" or D1== "Left" or D1=="L":
    D2 = input("you have come to a shore. There is deep water. You can either wait \n or swim across. What will you do?\n")
    if D2== "wait" or D2 == "Wait":
            D3 =input("you have now come to a door. There is a red, blue, or yellow door \n You have the option to open any door")   
            if D3 == "Yellow" or D3== "yellow":
                   print("You win the treasure")

            elif D3=="Blue" or D3=="blue" or D3=="b":
                   print("You have been eaten by beasts. Game over.")

            elif D3 == "red" or D3=="Red" or D3=="R":
                   print("You have been burned by fire. Game over.")
           ##### come out of first loop    
       
            else:
                print("Game over.")
    
   
    else:
            print("You have been attacked by a Shark. Game over")





else:
         print("You have fallen into a hole game over")
         

#### They are now swimming or waiting


### They now come to three doors

    
