from flask import Flask, render_template, request
import pickle
import numpy as np
from waitress import serve # Gunicorn-alternative for easy serving

app = Flask(__name__)

# Load the trained model
with open('insurance_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction_text = None
    if request.method == 'POST':
        try:
           # 1. Extract and process form data
            age = int(request.form['age'])
            # 'sex' is usually dropped as a baseline if it's binary (Female/Male). 
            # We only need 'Male' (1 or 0). If 0, the model knows it's Female.

            bmi = float(request.form['bmi'])
            children = int(request.form['children'])
            is_smoker = 1 if request.form['smoker'] == 'yes' else 0

            # 2. Hand-craft the one-hot encoding for region (keeping 3 columns, 4th is baseline)
            region_str = request.form['region']
            region_northeast, region_northwest, region_southeast = 0, 0, 0

            if region_str == 'northeast':
                region_northeast = 1
            elif region_str == 'northwest':
                region_northwest = 1
            elif region_str == 'southeast':
                region_southeast = 1

            # 3. Create the 7-feature array (The "Input Vector")
            # Order: [age, bmi, children, is_smoker, is_male, reg_ne, reg_nw, reg_se]
            # Verify this order matches your X.columns in Jupyter!
            final_features = np.array([[
                age, bmi, children, is_smoker, 
                region_northeast, region_northwest, region_southeast
            ]])

            # 4. Make prediction
            prediction = model.predict(final_features)
            output = round(prediction[0], 2)
            prediction_text = f'Estimated Annual Insurance Charges: ${output}'

        except Exception as e:
            prediction_text = f'Error: {str(e)}. Please check your inputs.'

    # Serve the page, either blank (GET) or with result (POST)
    return render_template('index.html', prediction_text=prediction_text)

if __name__ == "__main__":
    # Render provides a port through environment variables
    # If it can't find one, it defaults to 5000 for local testing
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
