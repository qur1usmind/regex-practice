#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# # 30 REGULAR EXPRESSION EXERCISES!

# Regex, you never know when they might come in handy. It's one of the "good programmer"'s fundamental yet a few people actually masters them.
# 
# Challenge yourself in 30 exercises, just hide the solution in order not to peek ;)

# In[2]:


import re


# 1) Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).

# In[18]:


# Solution
def is_allowed_specific_char(string):
  # Definite a regex pattern
    pattern = r'[a-zA-Z/d]'
  # Use the pattern to search for ....
    if re.search(pattern, string): 
        return ('True')
    else:
        return('False')
    
print(is_allowed_specific_char("ABCDEFabcdef123450")) # True
print(is_allowed_specific_char("*&%@#!}{")) # False


# 2) Write a Python program that matches a string that has an a followed by zero or more b's

# In[17]:


# Solution
def text_match(text):
  #pass
    pattern = r'ab*'
    if re.match(pattern,text): 
        return ('Found a match!')
    else:
        return('Not matched')
    
print(text_match("ac"))   # Found a match!
print(text_match("abc"))  # Found a match!
print(text_match("abbc"))   # Found a match!
print(text_match("bbc"))  # Not matched


# 3) Write a Python program that matches a string that has an a followed by one or more b's

# In[16]:


# Solution
def text_match(text):
    pattern = r'ab+'
    if re.match(pattern,text): 
        return ('Found a match!')
    else:
        return('Not matched') 

print(text_match("ab"))   # Found a match!
print(text_match("abc"))   # Found a match!
print(text_match("ac"))  # Not matched
print(text_match("bbc"))  # Not matched


# 4) Write a Python program that matches a string that has an a followed by zero or one 'b'

# In[15]:


# Solution
def text_match(text):
    pattern = r'ab?'
    if re.match(pattern,text): 
        return ('Found a match!')
    else:
        return('Not matched')
    
print(text_match("ab"))  # Found a match!
print(text_match("abc"))  # Found a match!
print(text_match("abbc"))  # Found a match!
print(text_match("aabbc"))  # Found a match!
print(text_match("ac"))  # Found a match!
print(text_match("bbc"))  # Not matched


# 5) Write a Python program that matches a string that has an a followed by three 'b'

# In[14]:


# Solution
def text_match(text):
    pattern = r'a+b{3,}'
    if re.match(pattern,text): 
        return ('Found a match!')
    else:
        return('Not matched')

print(text_match("abbb"))  # Found a match!
print(text_match("aabbbbbc"))  # Found a match!
print(text_match("aabbc"))  # Not matched
print(text_match("ac"))  # Not matched
print(text_match("bbc"))  # Not matched


# 6) Write a Python program that matches a string that has an a followed by two to three 'b'.

# In[13]:


# Solution
def text_match(text):
    pattern = r'a+b{2,3}'
    if re.match(pattern,text): 
        return ('Found a match!')
    else:
        return('Not matched')

print(text_match("ab"))  # Not matched
print(text_match("aabbbbbc"))  # Found a match!
print(text_match("aabbc"))  # Found a match!
print(text_match("ac"))  # Not matched
print(text_match("bbc"))  # Not matched


# 7) Write a Python program to find sequences of lowercase letters joined with a underscore.

# In[34]:


# Solution
def text_match(text):
    pattern = r'^[a-z]+_[a-z]'
    if re.match(pattern,text): 
        return ('Found a match!')
    else:
        return('Not matched')

print(text_match("aab_cbbbc"))  # Found a match!
print(text_match("aab_Abbbc"))  # Not matched
print(text_match("Aaab_abbbc"))  # Not matched


# 8) Write a Python program to find the sequences of one upper case letter followed by lower case letters.

# In[75]:


# Solution
def text_match(text):
    pattern = r'[A-Z]+[a-z]'
    if re.search(pattern,text): 
        return ('Found a match!')
    else:
        return('Not matched')

print(text_match("aab_cbbbc"))  # Not matched
print(text_match("aab_Abbbc"))  # Found a match!
print(text_match("Aaab_abbbc"))  # Found a match!


# 9) Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

# In[42]:


# Solution
def text_match(text):
    pattern = r'a.*?b$'
    if re.match(pattern,text): 
        return ('Found a match!')
    else:
        return('Not matched')

print(text_match("aabbbbd"))  # Not matched
print(text_match("aabAbbbc"))  # Not matched
print(text_match("accddbbjjjb"))  # Found a match!


# 10) Write a Python program that matches a word at the beginning of a string.

# In[44]:


# Solution
def text_match(text):
    pattern = r'^\w+'
    if re.match(pattern,text): 
        return ('Found a match!')
    else:
        return('Not matched')

print(text_match("The quick brown fox jumps over the lazy dog."))  # Found a match!
print(text_match(" The quick brown fox jumps over the lazy dog."))  # Not matched


# 11) Write a Python program that matches a word at the end of string, with optional punctuation.

# In[76]:


# Solution
def text_match(text):
    pattern = r'\w+[.]+$'
    if re.search(pattern,text): 
        return ('Found a match!')
    else:
        return('Not matched')

print(text_match("The quick brown fox jumps over the lazy dog."))  # Found a match!
print(text_match("The quick brown fox jumps over the lazy dog. "))  # Not matched
print(text_match("The quick brown fox jumps over the lazy dog "))  # Not matched


# 12) Write a Python program that matches a word containing 'z'

# In[81]:


# Solution
def text_match(text):
    pattern = r'\w[z]'
    if re.search(pattern,text): 
        return ('Found a match!')
    else:
        return('Not matched')

print(text_match("The quick brown fox jumps over the lazy dog."))  # Found a match!
print(text_match("Python Exercises."))  # Not matched


# 13) Write a Python program that matches a word containing 'z', not at the start or end of the word.

# In[82]:


# Solution
def text_match(text):
    pattern = r'\w[z]'
    if re.search(pattern,text): 
        return ('Found a match!')
    else:
        return('Not matched')

print(text_match("The quick brown fox jumps over the lazy dog."))  # Found a match!
print(text_match("Python Exercises."))  # Not matched


# 14) Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.

# In[83]:


# Solution
def text_match(text):
    pattern = r'^[A-Za-z0-9_]*$'
    if re.search(pattern,text): 
        return ('Found a match!')
    else:
        return('Not matched')

print(text_match("The quick brown fox jumps over the lazy dog."))  # Not matched
print(text_match("Python_Exercises_1"))  # Found a match!


# 15) Write a Python program where a string will start with a specific number. 

# In[90]:


# Solution
def match_num(text):
    pattern = r'^5'
    if re.search(pattern,text): 
        return ('True')
    else:
        return('False')
    
print(match_num('5-2345861')) # True
print(match_num('6-2345861')) # False


# 16) Write a Python program to remove leading zeros from an IP address

# In[99]:


# Solution

def rewrite_ip(ip):    
  # your code here 
    pattern = '\.[0]*'
    my_ip = re.sub(pattern,'.',ip)
    print(my_ip)
ip = "216.08.094.196"
string = rewrite_ip(ip)
#print(string) # 216.8.94.196


# 17) Write a Python program to check for a number at the end of a string.

# In[101]:


# Solution
def end_num(string):
    pattern = r'\d$'
    if re.search(pattern,string): 
        return ('True')
    else:
        return('False')

print(end_num('abcdef'))  # False
print(end_num('abcdef6')) # True


# 18) Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string. 

# In[105]:


# Solution
def print_digits(string):
    pattern = r'\d{1,3}'
    if re.match(pattern,string): 
        #return string #('Found a match!')
        print (string)
    #else:
    #    return('Not matched')

string = "Exercises number 1, 12, 13, and 345 are important"
print_digits(string)
# Number of length 1 to 3
# 1
# 12
# 13
# 345


# 19) Write a Python program to search some literals strings in a string. 
# Sample text : 'The quick brown fox jumps over the lazy dog.'
# Searched words : 'fox', 'dog', 'horse'

# In[106]:


# Solution
def print_match(patterns, text):
    pattern = r'[fox|dog|hourse]'
    if re.search(pattern,text): 
        return ('Found a match!')
    else:
        return('Not matched') 


patterns = [ 'fox', 'dog', 'horse' ]
text = 'The quick brown fox jumps over the lazy dog.'
print_match(patterns, text)
# Searching for "fox" in "The quick brown fox jumps over the lazy dog." ->
# Matched!
# Searching for "dog" in "The quick brown fox jumps over the lazy dog." ->
# Matched!
# Searching for "horse" in "The quick brown fox jumps over the lazy dog." ->
# Not Matched!


# 20) Write a Python program to search a literals string in a string and also find the location within the original string where the pattern occurs
# 
# Sample text : 'The quick brown fox jumps over the lazy dog.'
# Searched words : 'fox'

# In[115]:


# Solution
def print_match_location(pattern, text):
    pattern ='fox'
    match=re.search(pattern,text)
    s=match.start()
    e=match.end() 
    #print('Found {} in {} from {} to {}.format(pattern,text, s, e)) 
    print("Found '%s' in '%s' from %d to %d" % (match.re.pattern,match.string,s,e))
text = 'The quick brown fox jumps over the lazy dog.'
print_match_location(pattern, text)
# Found "fox" in "The quick brown fox jumps over the lazy dog." from 16 to 19


# 21) Write a Python program to find the substrings within a string.
# 
# #Sample text :
# 
# #'Python exercises, PHP exercises, C# exercises'
# 
# #Pattern :
# 
# #'exercises'
# 
# #Note: There are three instances of exercises in the input string.

# In[ ]:


# Solution
def find_all_matches(pattern, text):
  pass

text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
find_all_matches(pattern, text)
# Found "exercises"
# Found "exercises"
# Found "exercises"


# 22) Write a Python program to find the occurrence and position of the substrings within a string.

# In[ ]:


# Solution
def find_all_matches_location(pattern, text):
  pass


text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
find_all_matches_location(pattern, text)
# Found "exercises" at 7:16
# Found "exercises" at 22:31
# Found "exercises" at 36:45


# 23) Write a Python program to replace whitespaces with an underscore and vice versa.

# In[ ]:


text = 'Python Exercises'

# Your code

print(text) # Python_Exercises


# Your code

print(text) # Python Exercises


# 24) Write a Python program to extract year, month and date from a an url. 

# In[116]:


# Solution
def extract_date(url):
    match = re.findall(r'/(\d{4})/(\d{1,2})/(\d{1,2})/',url)
    return match
  
url1= "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"
print(extract_date(url1)) # [('2016', '09', '02')]


# 25) Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.

# In[129]:


# Solution
def change_date_format(dt):
    return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})''\\3-\\2-\\1',dt1)
     
dt= "2026-01-02"
dt1 = "2026-01-02"
print("Original date in YYY-MM-DD Format: ",dt1)  # Original date in YYY-MM-DD Format:  2026-01-02
print("New date in DD-MM-YYYY Format: ",change_date_format(dt1))  # New date in DD-MM-YYYY Format:  02-01-2026


# 26) Write a Python program to match if any words from a list of words starting with letter 'P'.

# In[ ]:


# Sample strings.
def print_words_starting_with_P(words):
  pass

words = ["Python PHP", "Java JavaScript", "c c++"]
print_words_starting_with_P(words)  # ('Python', 'PHP')


# 27) Write a Python program to separate and print the numbers of a given string.

# In[ ]:


# Solution
def print_all_numbers(text):
  pass

# Sample string.
text = "Ten 10, Twenty 20, Thirty 30"
print_all_numbers(text)
# 10
# 20
# 30


# 28) Write a Python program to find all words starting with 'a' or 'e' in a given string.

# In[131]:


# Solution
def get_all_words_containing_a_or_e(text):
    return(re.findall("[ae]\w+",text)) 


# Input.
text = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
print(get_all_words_containing_a_or_e(text))
# ['example', 'eates', 'an', 'ayList', 'apacity', 'elements', 'elements', 'are', 'en', 'added', 'ayList', 'and', 'ayList', 'ed', 'accordingly']


# 29) Write a Python program to separate and print the numbers and their position of a given string.

# In[135]:


# Solution
def print_all_numbers_and_their_position(text):
    for num in re.finditer("\d+",text):
        print(num.group())
        print("index position:",num.start())

# Input.
text = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
print_all_numbers_and_their_position(text)
# 50
# Index position: 62


# 30) Write a Python program to abbreviate 'Road' as 'Rd.' in a given string.

# In[130]:


# Solution
def abbreviate_road(street):
    return(re.sub('Road$','Rd.',street))

street = '21 Ramkrishna Road'

print(abbreviate_road(street))  # 21 Ramkrishna Rd.


# In[ ]:




