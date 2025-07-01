from flask import Flask

app = Flask(__name__)

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
# Options - retrieve json using random date from 19/06/2021 https://www.nytimes.com/svc/wordle/v2/{yyyy}-{MM}-{dd}.json
@app.route("/")
def game():
    solved = False
    i = 0
    while not solved and i < 6:
        guess = input("Make a Guess: ")
        target = "minow"
        if len(guess) != len(target):
            print("Error: Lenght mismatch")
        else:
            out, solved = make_guess(guess, target)
            if not solved:
                print("Incorrect guess, try again", out)
        i += 1            
    if solved:
        return("You Win!")
    else:
        return("Failed")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)