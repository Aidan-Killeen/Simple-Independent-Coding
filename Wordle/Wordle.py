from flask import Flask, request

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

target = "minow"
guess_no = 0

@app.route("/")
def game():
    global guess_no
    guess = request.args.get("guess", "")
    if guess:
        if len(guess) != len(target):
            output = "Error: Length mismatch"
        else:
            out, solved = make_guess(guess, target)
            if not solved:
                output = "Incorrect guess, try again " + str(out)
            else:
                output = "Correct!"
            guess_no += 1
    else:
        output = ""

    return(
        """<form action="" method="get">
                Make a Guess: <input type="text" name="guess">
                <input type="submit" value="Submit">
            </form>"""
        + "Last Guess: "
        + output
        + "<br>Current Guess: "
        + str(guess_no)
    )

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)