## Watch Options ##


options = {

    ## Movie options ##

    # 80s #

    "Top Gun": ["movie", "80s", "action"],
    "Beetlejuice" : ["movie", "80s", "comedy"],
    "Sixteen Candles" : ["movie", "80s", "romance"],
    "The Breakfast Club" : ["movie", "80s", "drama"],
    
    # 90s #
                              
    "10 Things I Hate About You" : ["movie", "90s", "romance"],
    "Independance_Day" : ["movie", "90s", "action"],
    "Austin Powers: The Spy Who Shagged Me" : ["movie", "90s", "comedy"],
    "Clueless" : ["movie", "90s", "drama"],
    
    # 2000s # 
    "The Sisterhood of the Traveling Pants" : ["movie", "2000s", "drama"],
    "A Cinderella Story" : ["movie", "2000s", "romance"],
    "Mean Girls" : ["movie", "2000s", "comedy"],
    "Spiderman" : ["movie", "2000s", "action"],
    
    # 2020s #
    
    "Top Gun: Maverick" : ["movie", "2020s", "action"],
    "I Still Believe" : ["movie", "2020s", "drama"],
    "To All the Boys I've Loved Before" : ["movie", "2020s", "romance"],
    "The Mitchells vs The Machines" : ["movie", "2020s", "comedy"],
         
    
    ## TV options ##
    
    # 80s #
    
    "Growing Pains" : ["tv show", "80s", "comedy"],
    "21 jumpstreet" : ["tv show", "80s", "drama"],
    "Full House" : ["tv show", "80s", "romance"],
    "He Man and the Masters of the Universe" : ["tv show", "80s", "action"],
    
    # 90s #
    
    "The Fresh Prince of Bel Air" : ["tv show", "90s", "comedy"],
    "Boy Meets World" : ["tv show", "90s", "drama"],
    "Friends" : ["tv show", "90s", "romance"],
    "Sailor Moon" : ["tv show", "90s", "action"],
    
    # 2000s #
    
    "Gilmore Girls" : ["tv show", "2000s", "romance"],
    "Gossip Girl" : ["tv show", "2000s", "drama"],
    "The OC" : ["tv show", "2000s", "comedy"],
    "Criminal Minds" : ["tv show", "2000s", "action"],
        
    # 2020s #
    
    "Stranger Things" : ["tv show", "2020s", "action"],
    "Euphoria" : ["tv show", "2020s", "drama"],
    "Bridgerton" : ["tv show", "2020s", "romance"],
    "The Umbrella Academy" : ["tv show", "2020s", "comedy"],
    
}



## Functions ##

def greeting():
    
    """
    This greets the user and explains how to do the quiz
    """
    
    print ("Welcome to the best quiz for finding what to watch!")
    print()
    print("Here's how this works. We'll show you some simple questions.")
    print("They are multiple choice, meaning please answer by typing 'A', 'B', 'C', or 'D'... got it?")
    print()
    print("Prepare to be un-bored!")
    print()

def answers(answer, option_a, option_b, option_c, option_d):

    """
    This sorts what letter the user inputs and allows that letter to be set to the variable it matched for that question. 
    """

    if answer == "A":
        answer = option_a
        return answer

    elif answer == "B":
        answer = option_b
        return answer

    elif answer == "C":
        answer = option_c
        return answer

    elif answer == "D":
        answer = option_d
        return answer
       

def choose(type, year, genre):
    
    """
    This filters through the lists to chose something to watch
    """
    # This filters through the dictionary keys with the movie and tv options.
    for option in options:
        # This selects the titles (keys) of the dictionary
        watch = options[option]
        # This filters through the list in each key (movie or tv show)
        if watch[0] == type and watch[1] == year and watch[2] == genre: 
            print()
            print(f"Based on your taste, you should watch: {option}")
            print()


            
# Questions for shows: #

# 1 #

def question_1():
    
    """
    This question chooses type (movie vs tv show)
    """

    print("1. Would you like to watch a movie or a tv show? ")
    print()
    print("A. movie")
    print("B. tv show")
    print()
    print()
    
    one = input("Remember, only type the letter! Type answer here: ")
    one = one.upper()
    return one


 # 2 #
 
def question_2():

    """
    This question chooses release years
    """
    
    print()
    print("2. What era is the best? ")
    print()
    print("A. groovy 80's")
    print("B. 90's baby")
    print("C. 2000's yo")
    print("D. Give me something from this decade, pls (2020's)")
    print()
    
    two = input("Remember, only type the letter! Type answer here: ")
    two = two.upper()
    return two


# 3 #
def question_3():

    """
    This question chooses genre
    """
    
    print()
    print("3. What genre are you feeling?")
    print("A. romance")
    print("B. comedy")
    print("C. drama")
    print("D. action")
    print()
    
    three = input("Remember, only type the letter! Type answer here: ")
    three = three.upper()
    return three


## Run the program here ##


def run_program():

# Greeting #
    
    greeting()
   
# Question 1 #
    
    while True:
        one = question_1()
        if one == "A" or one =="B":
            # code below sorts through function "answers" and picks which option based on letter answered 
            one = answers(one, "movie", "tv show", None, None) 
            break
        else:
            print()
            print("Sorry, I don't understand. Try again")
            print()

# Question 2 #
    
    while True:
        two = question_2()
        if two == "A" or two == "B" or two == "C" or two == "D":
            # code below sorts through function "answers" and picks which option based on letter answered 
            two = answers(two, "80s", "90s", "2000s", "2020s")
            break
        else:
            print()
            print("Sorry, I don't understand. Try again") 
            print()

# Question 3 #
            
    while True:
        three = question_3()
        if three == "A" or three == "B" or three == "C" or three == "D":
             # code below sorts through function "answers" and picks which option based on letter answered 
            three = answers(three, "romance", "comedy", "drama", "action")
            break
        else:
            print()
            print("Sorry, I don't understand. Try again")
            print()

# Double Check # 
    print()
    print("Your choices were:")
    print(one)
    print(two)
    print(three)

# Choose #
    choose(one, two, three)

run_program()