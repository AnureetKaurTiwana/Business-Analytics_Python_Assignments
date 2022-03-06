#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time

start_time=time.time()
end_time=start_time
lap_num=1

print("Click on ENTER to count laps.\nPress CTRL+C to stop")

try:
   while True:

      input()
      time_laps=round((time.time() - end_time), 2)

      tot_time=round((time.time() - start_time), 2)

      print("Lap No. "+str(lap_num))
      print("Total Time: "+str(tot_time))
      print("Lap Time: "+str(time_laps))

      print("*"*20)

      end_time=time.time()
      lap_num+=1

except KeyboardInterrupt:
   print("Exit!")


# In[3]:


# Python program to convert 
# date to timestamp
  
  
  
import time
import datetime
  
  
string = "20/01/2020"
  
element = datetime.datetime.strptime(string,"%d/%m/%Y")
  
tuple = element.timetuple()
timestamp = time.mktime(tuple)
  
print(timestamp)


# # A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
# 
# RegEx can be used to check if a string contains the specified search pattern.

# Regex in Python to put spaces between words starting with capital letters

# In[9]:


import re
   
def putSpace(input):
   
    # regex [A-Z][a-z]* means any string starting 
    # with capital character followed by many 
    # lowercase letters 
    words = re.findall('[A-Z][a-z]*', input)
   
    # Change first letter of each word into lower
    # case
    for i in range(0,len(words)):
        words[i]=words[i][0].lower()+words[i][1:]
        print(' '.join(words))
     
   
# Driver program
if __name__ == "__main__":
    input = 'BruceWayneIsBatman'
    putSpace(input)


# # Python Regex to extract maximum numeric value from a string

# In[11]:


import re
  
def extractMax(input):
  
     # get a list of all numbers separated by 
     # lower case characters 
     # \d+ is a regular expression which means
     # one or more digit
     # output will be like ['100','564','365']
     numbers = re.findall('\d+',input)
  
     # now we need to convert each number into integer
     # int(string) converts string into integer
     # we will map int() function onto all elements 
     # of numbers list
     numbers = map(int,numbers)
  
     print(max(numbers))
  
# Driver program
if __name__ == "__main__":
    input = '100klh564abc365bg'
    extractMax(input)


# # The most occurring number in a string using Regex in python

# In[14]:


from collections import Counter 
  
def most_occr_element(word):
      
    # re.findall will extract all the elements 
    # from the string and make a list
    arr = re.findall(r'[0-9]+', word)    
    print(arr)
    # to store maxm frequency
    maxm = 0  
  
    # to store maxm element of most frequency
    max_elem = 0
      
    # counter will store all the number with 
    # their frequencies  
    c = Counter(arr)
    print(c)
    # Store all the keys of counter in a list in
    # which first would we our required element    
    for x in list(c.keys()):
  
        if c[x]>= maxm:
            maxm = c[x]
            max_elem = int(x)
                  
    return max_elem
  
# Driver program 
if __name__ == "__main__": 
    word = 'geek55of55gee4ksabc3dr2x'
    print(most_occr_element(word))


# # Python program to Count Uppercase, Lowercase, special character and numeric values using Regex

# In[15]:


string = "ThisIsGeeksforGeeks !, 123"
 
# Creating separate lists using
# the re.findall() method.
uppercase_characters = re.findall(r"[A-Z]", string)
lowercase_characters = re.findall(r"[a-z]", string)
numerical_characters = re.findall(r"[0-9]", string)
special_characters = re.findall(r"[, .!?]", string)
 
print("The no. of uppercase characters is", len(uppercase_characters))
print("The no. of lowercase characters is", len(lowercase_characters))
print("The no. of numerical characters is", len(numerical_characters))
print("The no. of special characters is", len(special_characters))


# # Python – Check if String Contain Only Defined Characters using Regex

# In[25]:


def check(str, pattern):
    
    # _matching the strings
    if re.search(pattern, str):
        print("Valid String")
    else:
        print("Invalid String")
  
# _driver code
pattern = re.compile('^[1234]+$')
check('2134', pattern)
check('349', pattern)


# # Find the number of times every day occurs in a month

# In[27]:


# Python program to count
# occurrence of days in a month
import math
 
# function to find occurrences
def occurrenceDays( n, firstday):
 
    # stores days in a week
    days = [ "Monday", "Tuesday", "Wednesday",
           "Thursday",  "Friday", "Saturday",
           "Sunday" ]
  
    # Initialize all counts as 4.
    count= [4 for i in range(0,7)]
     
    # find index of the first day
    pos=-1
    for i in range(0,7):
        if (firstday == days[i]):
            pos = i
            break
# number of days whose occurrence will be 5
    inc = n - 28
  
    # mark the occurrence to be 5 of n-28 days
    for  i in range( pos, pos + inc):
        if (i > 6):
            count[i % 7] = 5
        else:
            count[i] = 5
     
  
    # print the days
    for i in range(0,7):
        print (days[i] , " " , count[i])
     
 
  
# driver program to test
# the above function
n = 31
firstday = "Tuesday"
occurrenceDays(n, firstday)


# In[ ]:




