from random import randint

from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

import compare as c
import translate_value as tv

app = Flask(__name__)


@app.route("/")
def home_page():
    return app.send_static_file('index.html')


@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a reply to an incoming text message"""
    # Get the message the user sent to a Twilio number
    body = request.values.get('Body', None)

    # Translates human player's move from a string to integer between 1 and 3.
    player_move = tv.from_string_to_integer(body)

    # Generates a random integer between 1 and 3 as a computer move.
    computer_move = randint(1, 3)

    # Compares computer and human player's moves.
    result = c.compare_moves(player_move, computer_move)

    # Generates a string that is sent to a human player as a final result.
    send_result = "You chose {p}.\nComputer chose {c}.\n{r}".format(
        p=tv.from_integer_to_string(player_move), c=tv.from_integer_to_string(computer_move), r=result)

    # Start TwiML response
    resp = MessagingResponse()

    # Determine the right reply for this message
    if body in tv.all_moves:
        resp.message(send_result)
    else:
        resp.message("Please enter Rock, Paper or Scissors.\nSee https://twilio-rps.herokuapp.com for more "
                     "information.")

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
