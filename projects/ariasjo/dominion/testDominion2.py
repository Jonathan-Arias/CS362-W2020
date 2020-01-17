# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 15:42:42 2015
Updated on Thu Jan 16 19:13:00 2020

@author: Jonathan-Arias
"""

import testUtility

#Get player names
player_names = ["*Annie","*Ben","*Carla"]
num_players = len(player_names)

#number of curses and victory cards
nV = 0
nC = 0
nV, nV = testUtility.init_cards(num_players)

#Define box
box = testUtility.init_box(nV)

#Get the supply order
supply_order = testUtility.get_supply_order()

#initialize the supply
supply = testUtility.init_supply(box, nV, nC, num_players)

#initialize the trash
trash = []

#Costruct the Player objects
players = testUtility.init_players(player_names)

#Play the game
testUtility.play_game(supply, trash, supply_order, players)

#Final score
testUtility.end_game(players)