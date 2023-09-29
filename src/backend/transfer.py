from flask import Flask, request, jsonify
from flask_cors import CORS
import backend.gen_word as gw

app = Flask(__name__)
CORS(app)

@app.route('/process', methods=['POST'])
def process_input():
    data = request.json  # Receive JSON data from JavaScript
    input_value = data.get('input')

    valid = gw.check_valid_word(input_value)
    not_used = gw.check_used_word(input_value)
    result = gw.generate_next_word(input_value)
    lose = gw.checkLose(result)
    response = {'output': result,
                'check': not_used and valid,
                'lose': lose}

    # Send the result back to JavaScript
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=5002)
