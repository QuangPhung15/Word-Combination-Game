from flask import Flask, request, jsonify
from flask_cors import CORS
import gen_word as gw

app = Flask(__name__)
CORS(app)

@app.route('/process', methods=['POST'])
def process_input():
    data = request.json  # Receive JSON data from JavaScript
    input_value = data.get('input')

    response = {}

    valid = gw.check_valid_word(input_value)
    if (valid):
        not_used = gw.check_used_word(input_value)
        if (not_used):
            result = gw.generate_next_word(input_value)
            lose = gw.checkLose(result)
            if (lose):
                response = {'output': result,
                            'check': True,
                            'lose': lose}
            else:
                response = {'output': result,
                            'check': True,
                            'lose': lose}
        else:
            response = {'output': input_value,
                        'check': False,
                        'lose': False}
    else:
        response = {'output': input_value,
                    'check': False,
                    'lose': False}

    # Send the result back to JavaScript
    return jsonify(response)

@app.route('/start', methods=["POST"])
def startGame():
    gw.eraseUsedWords()

    return jsonify(message="Game Started")

if __name__ == '__main__':
    app.run(port=5002)
