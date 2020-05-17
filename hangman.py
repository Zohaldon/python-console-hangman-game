import random

list_word = ['python', 'java', 'kotlin', 'javascript']
print("H A N G M A N")
my_word = random.choice(list_word)
hint = "".join(["-" for _ in my_word])
guess_count = 8
user_input_list = []
make_hint = []
first_run = True
user_input_list_incorrect = []
play = "r"

def get_started():
    global my_word, hint, guess_count, user_input_list, user_input_list_incorrect, make_hint, first_run, play
    my_word = random.choice(list_word)
    hint = "".join(["-" for _ in my_word])
    guess_count = 8
    user_input_list = []
    make_hint = []
    first_run = True
    user_input_list_incorrect = []
    play = "r"
def get_hint():
    global make_hint, hint, user_input_list
    to_check = list(set(user_input_list))
    for i in range(len(my_word)):
        added = False
        for j in range(len(to_check)):
            if added == False:
                if to_check[j] == my_word[i]:
                    make_hint.append(my_word[i])
                    added = True
                    break
        if added == False:
            make_hint.append("-")
    hint = "".join(make_hint) 
    make_hint = []

play = input('Type "play" to play the game, "exit" to quit:')
print()

while play == "play":
    while guess_count != 0:
        # print hint
        if first_run == True:
            print(hint)
            first_run = False
        else:
            get_hint()
            print()
            print(hint)
        
        # get input from user
        user_input = input("Input a letter:")
        
        # Check if the user printed exactly one letter. If not, the program should print You should print a single letter . Remember that zero is also not one!
        if len(user_input) > 1 or len(user_input) == 0:
            print("You should print a single letter")
        else:
            if user_input.isalpha() and user_input.islower():
                # Add user input to check list
                if user_input in my_word:
                    user_input_list.append(user_input)
                    get_hint()
                else:
                    user_input_list_incorrect.append(user_input)

                # if the word guessed by the program doesn't contain this letter
                if user_input not in my_word:
                    if user_input_list_incorrect.count(user_input) > 1:
                        print("You already typed this letter")
                    else:
                        # Print No such letter in the word
                        print("No such letter in the word")
                        # reduce the attempts count
                        guess_count -= 1
                else:
                    # if the guessed word contains this letter
                    if user_input in my_word:
                        # but the user tried this letter before
                        if user_input_list.count(user_input) > 1:
                            # Print No improvements
                            print("You already typed this letter")
            else:
                print("It is not an ASCII lowercase letter")


        # update hint variable
        get_hint()

        # if the word is already guessed then exit loop
        if hint == my_word:
            print()
            print(hint)
            print("You guessed the word!")
            print("You survived!")
            get_started()
            while play not in ["play","exit"]:
                play = input('Type "play" to play the game, "exit" to quit:')
            print()
            break
    else:
        print("You are hanged!")
        print()
        get_started()
        while play not in ["play","exit"]:
            play = input('Type "play" to play the game, "exit" to quit:')
        print()