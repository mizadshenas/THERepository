#!/usr/bin/env python
# coding: utf-8

# # Project Description

# Write a brief description of your project here. 
# 
# Note that projects should be self-sufficient, so make sure to provide enough information and context here for someone to understand what you are doing in your project, and why. 

# ## Project Code
# 
# If it makes sense for your project, you can have code and outputs here in the notebook as well.

# In[1]:


from my_module.functions import *


# In[2]:


# test it out
#I made a pop trivia project disguised as a quiz to give the user a surprise at the end! 
#I really just wanted to share trivia facts about some of my favorite artists 
#I used general information about the format method and the try and except areas (with Value Error) from online sources, but the rest is original. 

def run_facts():
    
    """Running the quiz using previous functions 
    
    Parameters
    ----------
    no direct inputs
    
    get_quiz_choice : function
    questions: list
    quiz : dict
    get_answer : function
    result : dict
    surprise_message : function
         
    Returns
    -------
    result : string
        The outcome of the quiz
    surprise_message: string outcome
        message for user ."""
    
    choice = get_quiz_choice()
    quiz_name = str(questions[choice - 1])
    
    #how to choose what quiz to choose based on user input 
    
    print ("\nYou chose the {}\n".format(quiz_name))
    
    quiz_questions = quiz[quiz_name]
    
    #presenting the quiz questions using the string of the quiz and the dictionary
    
    for q in quiz_questions:
        print ("Your answer is: {}\n".format(str(get_answer(q[0], q[1]))))
    print(result)
    
    #depending on the question, the function will find the answer
    
    surprise_message()


# In[ ]:


run_facts()


# In[ ]:


# !pytest my_module/test_functions.py

