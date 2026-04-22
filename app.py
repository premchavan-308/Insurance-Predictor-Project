import os  # <--- THIS WAS THE MISSING PIECE!
import pickle
import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)

# Load the trained model
try:
    with open('insurance_model.pkl', 'rb') as file:
        model = pickle.load(file)
    print("✅ Model loaded successfully!")
except Exception as e:
    print(f"❌ Model load error: {e}")

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction_text = None
    if request.method == 'POST':
        try:
            # 1. Extract inputs from the form
            age = int(request.form['age'])
            bmi = float(request.form['bmi'])
            children = int(request.form['children'])
            smoker = 1 if request.form['smoker'] == 'yes' else 0

            # 2. Region One-Hot Encoding (matching your 7-feature model)
            region_str = request.form['region']
            region_ne, region_nw, region_se = 0, 0, 0

            if region_str == 'northeast':
                region_ne = 1
            elif region_str == 'northwest':
                region_nw = 1
            elif region_str == 'southeast':
                region_se = 1

            # 3. Create the 7-feature array in correct order
            final_features = np.array([[
                age, bmi, children, smoker, 
                region_ne, region_nw, region_se
            ]])

            # 4. Make prediction
            prediction_usd = model.predict(final_features)
            # Conversion rate: 1 USD = 83.50 INR
            prediction_inr = prediction_usd[0] * 83.50
            
            output = round(prediction_inr, 2)
            
            # Format with Rupee symbol and commas for Indian numbering system
            prediction_text = f'Estimated Annual Insurance Charges: ₹{output:,}'
        
        except Exception as e:
            prediction_text = f'Error: {str(e)}. Please check your inputs.'

    return render_template('index.html', prediction_text=prediction_text)

# RENDER DEPLOYMENT SETTINGS
if __name__ == "__main__":
    # This detects the port Render wants, or defaults to 5000 for local testing
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
