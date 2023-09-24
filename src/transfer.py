from flask import Flask, request, jsonify
from flask_cors import CORS
import gen_word as gw

app = Flask(__name__)
CORS(app)

@app.route('/process', methods=['POST'])
def process_input():
    data = request.json  # Receive JSON data from JavaScript
    input_value = data.get('input')

    # Process the input (e.g., perform some computation)
    result = gw.generate_next_word(input_value)
    # result = input_value.lower()

    # Send the result back to JavaScript
    response = {'output': result}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
