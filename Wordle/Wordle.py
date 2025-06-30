def make_guess(guess: str, target: str):
    output = [""]*len(target)
    solved = True
    for i in range(len(guess)):
        char = guess[i]
        if target[i] == char:
            output[i] = "green"
        elif char in target:
            output[i] = "yellow"
            solved = False
        else:
            solved = False

    return output, solved

#Todo
#Archive prior guesses and colors
#Create UI
#Get randomised list of words for game
if __name__=="__main__":
    solved = False
    while not solved:
        guess = input("Make a Guess: ")
        target = "minow"
        if len(guess) != len(target):
            print("Error: Lenght mismatch")
        else:
            out, solved = make_guess(guess, target)
            if solved:
                print("You Win!")
            else:
                print("Incorrect guess, try again", out)