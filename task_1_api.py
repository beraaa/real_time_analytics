# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/v1.0/predict', methods=['GET'])
def predict():

    # Take numbers 
    num1 = float(request.args.get('num1', 0))
    num2 = float(request.args.get('num2', 0))
    
    # Calculate sum
    sum = num1 + num2
    
    # Apply the rule
    if sum > 5.8:
        prediction = 1
    else:
        prediction = 0
    
    # Prepare response
    response = {
        "prediction": prediction,
        "features": {
            "num1": num1,
            "num2": num2,
            "sum": sum
        }
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
