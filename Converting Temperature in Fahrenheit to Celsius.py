#!/usr/bin/env python
# coding: utf-8

# In[ ]:


temperature = input("Enter the temperature you would like to convert (e.g., 56F, 39C, etc.): ") #Getting input from the user
degree = int(temperature[0:-1]) #Getting digits from the input
scale = temperature[-1].upper() #Getting the scale from the input
result_scale='' #Initializing an empty string


# In[9]:


#Converting Celsius to Fahrenheit
if scale == 'C':
    result = int(round((9 * degree) / 5 + 32))
    result_scale = 'Fahrenheit'
    
#Converting Fahrenheit to Celsius
elif scale == 'F':
    result = int(round((degree - 32) * 5 / 9))
    result_scale = 'Celsius'
    
#Warning the user in case of not entering proper input 
else:
    print("Your input is not proper")
    quit()


# In[1]:


#Printing out the final result
print("The temperature in", result_scale, "is", result, "degrees.")


# In[ ]:




