#!/usr/bin/env python
# coding: utf-8

# 1. Create a checker board generator, which takes as inputs n and 2 elements
# to generate an n x n checkerboard with those two elements as alternating
# squares.
# Examples
# checker_board(2, 7, 6) ➞ [
# [7, 6],
# [6, 7]
# ]
# checker_board(3, &quot;A&quot;, &quot;B&quot;) ➞ [
# [&quot;A&quot;, &quot;B&quot;, &quot;A&quot;],
# [&quot;B&quot;, &quot;A&quot;, &quot;B&quot;],
# [&quot;A&quot;, &quot;B&quot;, &quot;A&quot;]
# ]
# checker_board(4, &quot;c&quot;, &quot;d&quot;) ➞ [
# [&quot;c&quot;, &quot;d&quot;, &quot;c&quot;, &quot;d&quot;],
# [&quot;d&quot;, &quot;c&quot;, &quot;d&quot;, &quot;c&quot;],
# [&quot;c&quot;, &quot;d&quot;, &quot;c&quot;, &quot;d&quot;],
# [&quot;d&quot;, &quot;c&quot;, &quot;d&quot;, &quot;c&quot;]
# ]
# checker_board(4, &quot;c&quot;, &quot;c&quot;) ➞ &quot;invalid&quot;
# 
# 
# 
# 
# 
# 
# 
# 
# 
# Ans:-

# In[1]:


def checker_board(grid_size,in_one,in_two):
    if in_one != in_two:
        input = [in_one,in_two]
        output = []
        for ele_1 in range(grid_size):
            output.append([])
            for ele_2 in range(grid_size):
                output[ele_1].append(input[(ele_1+ele_2)%2])
    else:
        output = 'Invalid'
    print(f'checker_board{grid_size,in_one,in_two} ➞ {output}')
    
checker_board(2, 7, 6)
checker_board(3, "A", "B")
checker_board(4, "c", "d")
checker_board(4, "c", "c") 


# 2. A string is an almost-palindrome if, by changing only one character, you
# can make it a palindrome. Create a function that returns True if a string is an
# almost-palindrome and False otherwise.
# Examples
# almost_palindrome(&quot;abcdcbg&quot;) ➞ True
# # Transformed to &quot;abcdcba&quot; by changing &quot;g&quot; to &quot;a&quot;.
# almost_palindrome(&quot;abccia&quot;) ➞ True
# # Transformed to &quot;abccba&quot; by changing &quot;i&quot; to &quot;b&quot;.
# almost_palindrome(&quot;abcdaaa&quot;) ➞ False
# # Can&#39;t be transformed to a palindrome in exactly 1 turn.
# almost_palindrome(&quot;1234312&quot;) ➞ False
# 
# 
# 
# 
# 
# 
# 
# Ans:-

# In[2]:


def almost_palindrome(in_string):
    in_string_rev = in_string[::-1]
    count = 0
    for ele in range(len(in_string)):
        if in_string[ele] != in_string_rev[ele]:
            count +=1
    output = True if count == 2 else False
    print(f'almost_palindrome({in_string}) ➞ {output}')
    
almost_palindrome("abcdcbg")
almost_palindrome("abccia")
almost_palindrome("abcdaaa")
almost_palindrome("1234312")


# 3. Create a function that finds how many prime numbers there are, up to the
# given integer.
# 
# Examples
# prime_numbers(10) ➞ 4
# # 2, 3, 5 and 7
# prime_numbers(20) ➞ 8
# # 2, 3, 5, 7, 11, 13, 17 and 19
# prime_numbers(30) ➞ 10
# # 2, 3, 5, 7, 11, 13, 17, 19, 23 and 29
# 
# 
# 
# 
# 
# 
# 
# 
# 
# Ans:-

# In[3]:


def prime_numbers(in_num):
    out_num = 0
    out_list = [2,3]
    for ele in range(1,in_num+1):
        if ele <= 3 and ele > 0:
            out_num = 2 if ele==3 else 1 if ele ==2 else 0
        elif ele > 3 and (((ele-1)%6 == 0) or ((ele+1)%6 == 0)):
            out_num +=1
            out_list.append(ele)    
    for top in out_list:
        for bottom in out_list:
            if top != bottom:
                if top%bottom == 0:
                    out_num -= 1
    print(f'prime_numbers({in_num}) ➞ {out_num}')
        
prime_numbers(10)     
prime_numbers(20)
prime_numbers(30)


# 
# 4. If today was Monday, in two days, it would be Wednesday.
# Create a function that takes in a list of days as input and the number of days
# to increment by. Return a list of days after n number of days has passed.
# Examples
# after_n_days([&quot;Thursday&quot;, &quot;Monday&quot;], 4) ➞ [&quot;Monday&quot;, &quot;Friday&quot;]
# after_n_days([&quot;Sunday&quot;, &quot;Sunday&quot;, &quot;Sunday&quot;], 1) ➞ [&quot;Monday&quot;, &quot;Monday&quot;,
# &quot;Monday&quot;]
# after_n_days([&quot;Monday&quot;, &quot;Tuesday&quot;, &quot;Friday&quot;], 1) ➞ [&quot;Tuesday&quot;, &quot;Wednesday&quot;,
# &quot;Saturday&quot;]
# 
# 
# 
# 
# 
# 
# 
# 
# 
# Ans:-

# In[4]:


def after_n_days(in_list,in_num):
    week_dict = {0:'Sunday',1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday'}
    week_days_no = list(week_dict.keys())
    week_days_name = list(week_dict.values())
    output = []
    for ele in in_list:
        output.append(week_dict[(week_days_name.index(ele)+in_num)%7])
    print(f'after_n_days{in_list,in_num} ➞ {output}')
    
after_n_days(["Thursday", "Monday"], 4)
after_n_days(["Sunday", "Sunday", "Sunday"], 1)
after_n_days(["Monday", "Tuesday", "Friday"], 1)


# 5. You are in the process of creating a chat application and want to add an
# anonymous name feature. This anonymous name feature will create an alias
# that consists of two capitalized words beginning with the same letter as the
# users first name.
# Create a function that determines if the list of users is mapped to a list of
# anonymous names correctly.
# Examples
# is_correct_aliases([&quot;Adrian M.&quot;, &quot;Harriet S.&quot;, &quot;Mandy T.&quot;], [&quot;Amazing
# Artichoke&quot;, &quot;Hopeful Hedgehog&quot;, &quot;Marvelous Mouse&quot;]) ➞ True
# is_correct_aliases([&quot;Rachel F.&quot;, &quot;Pam G.&quot;, &quot;Fred Z.&quot;, &quot;Nancy K.&quot;],
# [&quot;Reassuring Rat&quot;, &quot;Peaceful Panda&quot;, &quot;Fantastic Frog&quot;, &quot;Notable Nickel&quot;]) ➞
# True
# is_correct_aliases([&quot;Beth T.&quot;], [&quot;Brandishing Mimosa&quot;]) ➞ False
# 
# # Both words in &quot;Brandishing Mimosa&quot; should begin with a &quot;B&quot; - &quot;Brandishing
# Beaver&quot; would do the trick.
# 
# 
# 
# 
# 
# Ans:-

# In[5]:


def is_correct_aliases(in_list_one, in_list_two):
    output = False
    if len(in_list_one) == len(in_list_two):
        for ele in range(len(in_list_one)):
            if in_list_one[ele].split(" ")[0][0] == in_list_two[ele].split(" ")[0][0] == in_list_two[ele].split(" ")[1][0]:
                output = True
            else:
                output = False
                break
    print(f'is_correct_aliases{in_list_one,in_list_two}➞{output}')

is_correct_aliases(["Beth T."],["Brandishing Mimosa"])
is_correct_aliases(["Adrian M.","Harriet S.","Mandy T."], ["Amazing Artichoke", "Hopeful Hedgehog", "Marvelous Mouse"])
is_correct_aliases(["Rachel F.","Pam G.","Fred Z.","Nancy K."], ["Reassuring Rat", "Peaceful Panda", "Fantastic Frog", "Notable Nickel"])

