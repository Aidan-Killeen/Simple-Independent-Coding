from flask import Flask, request, make_response, render_template, redirect, url_for
import json
import requests
from datetime import datetime
from typing import Dict

app = Flask(__name__)

def make_guess(guess: str, target: str, prev_guesses: Dict):
    """
    Function to check if each letter in a guess is in the solution, and if it is in the right place
    
    """
    output = ["gray"] * len(target)
    solved = True
    yellow = set(prev_guesses["yellow_l"])
    green = set(prev_guesses["green_l"])
    gray = set(prev_guesses["gray_l"])
    for i in range(len(guess)):
        char = guess[i]
        if target[i] == char:
            yellow.discard(char)
            green.add(char)
            output[i] = "green"
        elif char in target:
            yellow.add(char)
            output[i] = "yellow"
            solved = False
        else:
            gray.add(char)
            solved = False
        prev_guesses["green_l"] = list(green)
        prev_guesses["yellow_l"] = list(yellow)
        prev_guesses["gray_l"] = list(gray)

    return output, solved

#Todo
# Adjust Layout - have elements next to each other
# block submit unless all letters filled - with valid potential letters
# Adjust Make_guess to automatically add parameters to prev_guesses (will reduce amount of outputs)
# Randomisation - retrieve json using random date from 19/06/2021

current = datetime.today().strftime('%Y-%m-%d')
target = requests.get('https://www.nytimes.com/svc/wordle/v2/'+current+'.json').json()["solution"]
print(target)
max_guesses = 6
letter_list = "qwertyuiopasdfghjklzxcvbnm"

@app.route("/")
def game():
    # Load details from prior guesses - or make blank cookie to store future information
    if 'prev_guesses' in request.cookies:
        prev_guesses = json.loads(request.cookies.get('prev_guesses'))
    else:
        prev_guesses = { 
            "words":["     "]*max_guesses,
            "colors":[["gray"]*len(target)]*max_guesses,
            "guess_no": 0,
            "green_l":[],
            "yellow_l":[],
            "gray_l":[],
            "target":target
            
            }
        
    solution = prev_guesses["target"]
    #print(prev_guesses)
    guess_no = prev_guesses["guess_no"]
    words = prev_guesses["words"]

    #print("Prev:", words)

    #Make a guess - cannot make one if game is already won
    won = solution.upper() in words
    valid = False
    guess = request.args.get("guess", "")
    output = ""
    if won:
        output = "You already won!"
    elif guess and guess.upper() not in words:
        if len(guess) != len(solution):
            output = "Error: Length mismatch"
        elif guess_no >= max_guesses:
            output = "You have run out of guesses"
        elif not guess.isalpha():
            output = "Invalid Guess: Not using alphabet char"
        else:
            out, solved = make_guess(guess, solution, prev_guesses)
            valid = True
            if solved:
                output = "Correct!"
                won = True
            words[guess_no] = guess.upper()
            prev_guesses["colors"][guess_no] = out
            guess_no += 1

    resp = make_response(render_template(
        "base.html", 
        output=output,
        won=won, 
        words=words,
        colors=prev_guesses["colors"],
        letter_list=letter_list,
        green_list=prev_guesses["green_l"],
        yellow_list=prev_guesses["yellow_l"],
        gray_list=prev_guesses["gray_l"],
        guess_no=guess_no))
    
    prev_guesses["guess_no"] = guess_no
    prev_guesses["words"] = words

    # Update the cookie - only if valid guess was made
    if valid:
        print(prev_guesses)
        resp.set_cookie('prev_guesses', json.dumps(prev_guesses))
    return resp

@app.route("/reset")
def reset():
    """
    Function that deletes the cookie of the currently active game, and redirects to the url for the game function.

    """
    resp = make_response(redirect(url_for('game')))
    resp.delete_cookie('prev_guesses')
    return resp


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)