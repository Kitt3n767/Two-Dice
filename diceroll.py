#diceroll.py

dice_roll1 = 0
dice_roll2 = 0
total = 0
count = 0
total2 = 0
total3 = 0
total4 = 0
total5 = 0
total6 = 0
total7 = 0
total8 = 0
total9 = 0
total10 = 0
total11 = 0
total12 = 0

import random

while count < 1000:
    dice_roll1 = randint(1, 7)
    dice_roll2 = randint(1, 7)
    total = dice_roll1 + dice_roll2
    
    if total == 2:
        total2 += 1
        
    elif total == 3:
        total3 += 1
        
    elif total == 4:
        total4 += 1
        
    elif total == 5:
        total5 += 1
        
    elif total == 6:
        total6 += 1
        
    elif total == 7:
        total7 += 1
        
    elif total == 8:
        total8 += 1
        
    elif total == 9:
        total9 += 1
        
    elif total == 10:
        total10 += 1
        
    elif total == 11:
        total11 += 1
        
    elif total == 12:
        total12 += 1


percent2 = total2 / 10
percent3 = total3 / 10
percent4 = total4 / 10
percent5 = total5 / 10
percent6 = total6 / 10
percent7 = total7 / 10
percent8 = total8 / 10
percent9 = total9 / 10
percent10 = total10 / 10
percent11 = total11 / 10
percent12 = total12 / 10

print("Number: 2, percent: {}, normal: 2.78".format(percent2))
print("Number: 3, percent: {}, normal: 5.56".format(percent3))
print("Number: 4, percent: {}, normal: 8.33".format(percent4))
print("Number: 5, percent: {}, normal: 11.11".format(percent5))
print("Number: 6, percent: {}, normal: 13.89".format(percent6))
print("Number: 7, percent: {}, normal: 16.67".format(percent7))
print("Number: 8, percent: {}, normal: 13.89".format(percent8))
print("Number: 9, percent: {}, normal: 11.11".format(percent9))
print("Number: 10, percent: {}, normal: 8.33".format(percent10))
print("Number: 11, percent: {}, normal: 5.56".format(percent11))
print("Number: 12, percent: {}, normal: 2.78".format(percent12))
