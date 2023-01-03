# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 23:28:21 2023

@author: Legion
"""

from predictbasic import similarities, printRecommendations

while 1:
    print("\nEnter 0 to exit.")
    user_id = input("Enter user ID to get recommendation: ")
    if user_id == '0':
        break
    print(printRecommendations(similarities, int(user_id), 40, 10))