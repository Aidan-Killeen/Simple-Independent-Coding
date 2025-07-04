from flask import Flask, request, make_response
import json

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
#guess_no = 0
#prev_guesses = []

@app.route("/")
def game():
    #global guess_no
    guess_no = int(request.cookies.get('guess_no', 0))
    prev_guesses = json.loads(str(request.cookies.get('prev_guesses', '{ "prior":[]}')))
    
    print(prev_guesses)
    valid = False
    guess = request.args.get("guess", "")
    if guess:
        if len(guess) != len(target):
            output = "Error: Length mismatch"
        else:
            out, solved = make_guess(guess, target)
            valid = True
            if not solved:
                output = "Incorrect guess, try again " + str(out)
            else:
                output = "Correct!"
            prev_guesses["prior"].append((guess, out))
            guess_no += 1
    else:
        output = ""

    resp = make_response("""<form action="" method="get">
                Make a Guess: <input type="text" name="guess">
                <input type="submit" value="Submit">
            </form>"""
        + "Last Guess: "
        + output
        + ", Prior Guesses: "
        + str(prev_guesses)
        + "<br>Current Guess: "
        + str(guess_no))
    
    resp.set_cookie('guess_no', str(guess_no))
    if valid:
        print(prev_guesses)
        resp.set_cookie('prev_guesses', json.dumps(prev_guesses))
    return(resp)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)