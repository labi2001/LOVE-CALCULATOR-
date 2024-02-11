#!/usr/bin/env python
# coding: utf-8

# In[16]:


name_1 = input("Enter your name: ")
name_2 = input("Enter your name: ")

# To get the value of TRUE
input_t = "t"
new_input_t = input_t.lower()

# Convert the names to lowercase before counting occurrences
count1 = name_1.lower().count(new_input_t)
count2 = name_2.lower().count(new_input_t)
count_of_t = count1 + count2

input_r = "r"
new_input_r = input_r.lower()

# Convert the names to lowercase before counting occurrences
count1 = name_1.lower().count(new_input_r)
count2 = name_2.lower().count(new_input_r)
count_of_r = count1 + count2

input_u = "u"
new_input_u = input_u.lower()

# Convert the names to lowercase before counting occurrences
count1 = name_1.lower().count(new_input_u)
count2 = name_2.lower().count(new_input_u)
count_of_u = count1 + count2

input_e = "e"
new_input_e = input_e.lower()

# Convert the names to lowercase before counting occurrences
count1 = name_1.lower().count(new_input_e)
count2 = name_2.lower().count(new_input_e)
count_of_e = count1 + count2

#print (count_of_t, count_of_r, count_of_u, count_of_e)
count_true = count_of_t + count_of_r + count_of_u + count_of_e
new_count_true = str(count_true)

# To get the value of LOVE

input_l = "l"
new_input_l = input_l.lower()

# Convert the names to lowercase before counting occurrences
count1 = name_1.lower().count(new_input_l)
count2 = name_2.lower().count(new_input_l)
count_of_l = count1 + count2

input_o = "o"
new_input_o = input_o.lower()

# Convert the names to lowercase before counting occurrences
count1 = name_1.lower().count(new_input_o)
count2 = name_2.lower().count(new_input_o)
count_of_o = count1 + count2

input_v = "v"
new_input_v = input_v.lower()

# Convert the names to lowercase before counting occurrences
count1 = name_1.lower().count(new_input_v)
count2 = name_2.lower().count(new_input_v)
count_of_v = count1 + count2

input_e = "e"
new_input_e = input_e.lower()

# Convert the names to lowercase before counting occurrences
count1 = name_1.lower().count(new_input_e)
count2 = name_2.lower().count(new_input_e)
count_of_e = count1 + count2

#print (count_of_l, count_of_o, count_of_v, count_of_e)
count_love = count_of_l + count_of_o + count_of_v + count_of_e
new_count_love = (str(count_love))

love_score = (new_count_true + new_count_love)
new_love_score = int(love_score)

if new_love_score < 10  or new_love_score > 90:
    print (f"Your love score is {love_score}, you go like coke and fanta")
elif new_love_score >= 40 and new_love_score  <=50: 
    print (f"Your love score is {love_score}, you are alright together")
else:
    print (f"Your love score is {love_score}")


# In[ ]:




