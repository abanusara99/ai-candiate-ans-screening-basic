# import
from flask import Flask, render_template, request, jsonify
from model.ai_gen import evaluate_candidates

app = Flask(__name__)

# route
@app.route('/')

# home url
def home():
    return render_template('aiin.html')

# evaluate url
@app.route('/evaluate', methods=['POST'])
def evaluate():
    data = request.json
    responses = data['responses']
    results = evaluate_candidates(responses)
    return jsonify(results)

# main and debug setup
if __name__ == '__main__':
    app.run(debug=True)    