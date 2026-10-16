# ------------------------------------------------------
#        Name: Langley Owen
#       Peers: (add any collaborators)
#  References: (anything you checked to solve this)
# ------------------------------------------------------
import sys

secret_word = "food"

# Task 1
def check_text():
    """ This function checks the text inputted by the user for
    the secret word, or the word dog. If user inputs neither,
    they get a 'Try again' message"""
    
    #while loop to check input
    while True:
    
        #ask for a sentence 
        sentence = input("Give me a sentence: ")
        
        #if sentence contains the secret word, print 
        if secret_word in sentence:
            print ("You used the secret word!")
            break
    
        #if sentence contains dog or Dog, print
        elif "dog" in sentence or "Dog" in sentence:
            print("You used the word \"dog\" or the word \"Dog\"!")
            break

        #if doesn't include word, print Try again and loop back to get another input
        else:
            print ("Try again")
            
        

# Task 2
def check_greater():
    """ This function takes two inputs from User
     and prints whether the first or second integer is greater.
     If equal, the user has to input again """
    
    
    while True:
        #ask for integer input
        int_a = int(input("Give me a first integer: "))
        int_b = int(input("Give me a second integer: "))
        
        #if first int greater than second, print
        if int_a > int_b:
            print ("First is Greater")
            break
        
        #if second int is greater than first, print
        elif int_a < int_b:
            print ("Second is Greater")
            break
        
        #if int_a == int_b, print "Try again" to get another input
        else:
            print ("Try again")
            


# Task 3
def get_special_numbers():
    """ This function checks that each number in range [1, 40] is odd,
     multiple of 3, and not a multiple of 5. ."""
    
    #set range
    for i in range (1 , 41):
        #if number is even, discard (check if odd (!=))
        #if number is not multiple of 3, discard (check if multiple of 3 (==))
        # if number is mutiple of five, discard (not multiple of five (!=))
        
        if i %2 != 0 and i %3 == 0 and i %5 != 0:
            
            #print integers
            print(i)


# Task 4.a
def my_for_loop():
    """ This function asks user for input, sorts each letter
     of the word into vowel or consonant. If neither, bad word is printed"""
    
    #ask for input
    user_input = input("Give me a string: ")
    
    #if string length not in range, return 
    if len(user_input) < 2 or len(user_input) > 5 or ' ' in user_input :
        print("bad word")
        return
    
    #define vowels, sort input into consonant or vowel
    for letter in user_input:
        
        vowels = "AaEeIiOoUu"

    
        if (letter in vowels):
            print(f"letter {letter} is a vowel")
        
        else:
            print(f"letter {letter} is a consonant")
            
        
# Task 4.b
def my_while_loop():
    """ This function asks for user to choose a, b, or c.
    It executes specific actions depending on whihc is chosen """
    
    #while loop
    while True:
        #ask for input
        x = input("Choose one option: a, b, or c: ")
        
        #if user inputs a, run menu again
        if x == "a":
            continue
        
        #if user inputs b, print Goodbye & break
        elif x == "b":
            print("Goodbye")
            break
            
        #if user inputs c, end program
        elif x == "c":
            exit()
            
        #if user inputs anything else, run menu again
        else:
            print("try again")
            continue

# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

def main():

    # Task 1 calls
    check_text()

    # Task 2 calls
    check_greater()

    # Task 3 calls
    get_special_numbers()

    # Task 4 calls
    my_for_loop()
    my_while_loop()

if __name__ == "__main__":
    main()
    print("The End")
