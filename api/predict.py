from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np
import os

app = Flask(__name__)
CORS(app)

# Load the model
model_path = os.path.join(os.path.dirname(__file__), '..', 'diabetes_model.pkl')
model = pickle.load(open(model_path, 'rb'))

@app.route('/api/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        
        # Extract features
        features = [
            float(data.get('pregnancies', 0)),
            float(data.get('glucose', 0)),
            float(data.get('bloodPressure', 0)),
            float(data.get('skinThickness', 0)),
            float(data.get('insulin', 0)),
            float(data.get('bmi', 0)),
            float(data.get('diabetesPedigreeFunction', 0)),
            float(data.get('age', 0))
        ]
        
        # Reshape and predict
        input_data = np.asarray(features).reshape(1, -1)
        prediction = model.predict(input_data)
        
        result = {
            'prediction': int(prediction[0]),
            'result': 'Diabetic' if prediction[0] == 1 else 'Not Diabetic'
        }
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
