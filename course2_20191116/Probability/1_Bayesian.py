# -*- coding: utf-8 -*-

import numpy as np
import math


dataSet = [[0, 0], # no email
           [1,1], # yes spam
           [1,1],
           [0,0],
           [0,1], # no spam
           [1,1],
           [0,0],
           [1,0], # yes email
           [0,0],
           [0,0]]

n_spam = 0.0
n_yes = 0.0
n_yes_spam = 0.0
total = len(dataSet)
print (total)

for i in dataSet:
    if i[0] == 1:
        n_yes += 1.0
    if i[1] == 1:
        n_spam += 1.0
    if i[0] == 1 and i[1] == 1:
        n_yes_spam += 1.0

p_yes = n_yes / len(dataSet)
p_spam = n_spam / len(dataSet)
p_yes_spam = n_yes_spam / (n_spam)

print (n_yes)
print (n_spam)
print (n_yes_spam)
print ('!!!!!!!!!')
p_spam_yes = p_yes_spam * p_spam / p_yes
print ('!!!!!!!!!!!!!')
print (p_spam_yes)




'''
n_spam = 0.0
n_spam_yes = 0.0
n_spam_not = 0.0
n_yes = 0.0
n_total = len(dataSet)

for i in dataSet:
    yes_not = i[0]
    spam_email = i[1]
    if spam_email == 1:
        n_spam += 1.0
    if yes_not == 1:
        n_yes += 1.0
    if spam_email == 1 and yes_not == 1:
        n_spam_yes += 1.0
    if spam_email == 1 and yes_not == 0:
        n_spam_not += 1.0

p_spam = n_spam / n_total
p_yes = n_yes / n_total
p_yes_spam = n_spam_yes / (n_spam_yes + n_spam_not)

print (p_spam)
print (p_yes)
print (p_yes_spam)

p_result = (p_yes_spam * p_spam) / p_yes
print (p_result)

exit()

'''



'''
# simpleWay
Email = 0.0
Spam = 0.0
Yes = 0.0
No = 0.0
Yes_Email = 0.0
Yes_Spam = 0.0

for i in dataSet:
    if i[0] == 1:
        Yes += 1.0
    else:
        No += 1.0

    if i[1] == 0:
        Email += 1.0
    else:
        Spam += 1.0

    if i[0] == 1 and i[1] == 0:
        Yes_Email += 1.0
    elif i[0] ==1 and i[1] ==1 :
        Yes_Spam += 1.0
No_Email = Email - Yes_Email
No_Spam = Spam - Yes_Spam
z = 1

P_yes = Yes / (Yes + No)
P_spam = Spam / (Email + Spam)
P_spam_yes = (Yes_Spam) / (Yes_Spam + No_Spam)

print (P_spam_yes * P_spam / P_yes)
'''