fleetmac_questions = 'Fleetwood Mac Questions'
beatles_questions = 'Beatles Questions'
floyd_questions = 'Pink Floyd Questions'

questions = [fleetmac_questions, beatles_questions, floyd_questions]

quiz = {fleetmac_questions : [("At least 1 in 6 households owns the album, Rumours", 1),
                        ("Fleetwood mac has had 18 different members over 50 years", 1),
                        ("Stevie Nicks joined Fleetwood Mac in 1975", 0), 
                        ("Stevie Nicks sings the lead vocals on the song, 'Sara'", 1)],
        beatles_questions : [("The Beatles made their first appearance on the Ed Sullivan Show on Feb 9, 1964", 1),
                         ("the last Beatles album is Let It Be in 1970", 0),
                         ("Paul McCartney's song 'Yesterday' came to him in a dream", 0)],

        floyd_questions : [("The name 'Pink Floyd' came from two blues musicians, Pink Anderson and Floyd Council", 0),
                     ("the album, 'another brick in the wall (part 2)' was released in 1979", 1),
                     ("Pink Floyd has sold over 250 million records worldwide", 1)]
}



result = {"InCorrect": 0, "Correct": 0}

def get_quiz_choice():
    
    """Selecting a quiz of choice to proceed based on the user's input. 
    
    Parameters
    ----------
    no direct inputs
    quiz : dict
        taking the list of questions from above to organize three different quizzes
        
    
    Returns
    -------
    quiz_number:
        the number that will decidee which quiz is chosen."""

    while True:
        
        try:
            quiz_number = int(input('Choose the quiz you like\n1 for Fleetwood Mac\n2 for The Beatles\n3 for Pink Floyd\nYour choice:').format(fleetmac_questions,
                                                                                            beatles_questions,
                                                                                          floyd_questions))
        
        except ValueError:
            print ("Not a number, please try again\n")
            
 #if the user input is not a selected value, it will prompt the user to pick another value           
        else: 
            if 0 >= quiz_number or quiz_number > len(quiz):
                print("Invalid value, please try again\n")
            else:
                return quiz_number

    

def get_answer(quiz, correct_answer):
    
    """Providing answer options to user, and giving a response and score. 
    
    Parameters
    ----------
    quiz : dict
        Where the quiz questions are located 
        
    correct_answer : int
        The assigned correct answer for questions
        qui
        
    
    Returns
    -------
    True and False: bool
        The outcome of the answer given by user """
    
    score = 0 
    
#formatting and presenting the questions and answer options for the 'Quiz'

    while True:
        try:
            print("Q: {}".format(quiz[0:]))
            answer = int(input("1 True\n0 False\nThe answer: "))
        
        except ValueError:
            print ("Not a number, please try again\n")
            
        else:
            
            if answer != 0 and answer != 1:
                print ("Invalid value, please try again\n")
                
#if the answer is listed, it will give it an according score

            elif answer == (quiz[1:]):
                result["Incorrect"] += 1
                return False
                    
            elif answer != (quiz[1:]):
                result["Correct"] += 1
                return True
            
def surprise_message(): 
    print("\nSurprise! this wasn't a quiz, it was actually a pop trivia with facts! enjoy your day!:)")
        
        