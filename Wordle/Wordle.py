from flask import Flask, request, make_response, Blueprint, render_template, redirect, url_for
import json
import requests
from datetime import datetime

app = Flask(__name__)
#bp = Blueprint('Wordle', __name__, url_prefix='')

def make_guess(guess: str, target: str):
    output = ["gray"]*len(target)
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
# Add grid of letters already guessed - seperate element on right of guesses
# Change cookie dict to be dict of guesses? - default would be {word: "     ", matches[(five color)]}
# Randomisation - retrieve json using random date from 19/06/2021

current = datetime.today().strftime('%Y-%m-%d')
target = requests.get('https://www.nytimes.com/svc/wordle/v2/'+current+'.json').json()["solution"]
print(target)
max_guesses = 6

@app.route("/")
def game():
    guess_no = int(request.cookies.get('guess_no', 0))
    if 'prev_guesses' in request.cookies:
        prev_guesses = json.loads(request.cookies.get('prev_guesses'))
    else:
        prev_guesses = { "prior":[["     ",["gray"]*len(target)]]*max_guesses}
    
    print(prev_guesses)
    prev_words = [ x[0].lower() for x in prev_guesses["prior"] ]
    print("Prev:", prev_words)
    won = target in prev_words
    valid = False
    guess = request.args.get("guess", "")
    if won:
        output = "You already won!"
    elif guess and not guess in prev_words:
        if len(guess) != len(target):
            output = "Error: Length mismatch"
        elif guess_no >= max_guesses:
            output = "You have run out of guesses"
        else:
            out, solved = make_guess(guess, target)
            valid = True
            if not solved:
                output = "Incorrect guess, try again "
            else:
                output = "Correct!"
            prev_guesses["prior"][guess_no] = [guess.upper(), out]
            guess_no += 1
    else:
        output = ""

    resp = make_response(render_template("base.html", output=output, prev_guesses=prev_guesses, guess_no=guess_no))
    
    resp.set_cookie('guess_no', str(guess_no))
    if valid:
        print(prev_guesses)
        resp.set_cookie('prev_guesses', json.dumps(prev_guesses))
    return resp

@app.route("/reset")
def reset():
    resp = make_response(redirect(url_for('game')))
    resp.delete_cookie('guess_no')
    resp.delete_cookie('prev_guesses')
    return resp


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)