#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random
n = random.randrange(1,200)
guess = int(input("Enter any number: "))
while n!= guess:
    if guess < n:
        print("Too low")
        guess = int(input("Enter number again: "))
    elif guess > n:
        print("Too high!")
        guess = int(input("Enter number again: "))
    else:
        break
print("you guessed it right!!")


# In[ ]:





# In[ ]:




