# 🏥 HealthSync: Medical Insurance Premium Predictor
[![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen)](https://insurance-predictor-project-dxdv.onrender.com)
[![Python](https://img.shields.io/badge/Python-3.14-blue)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Framework-Flask-lightgrey)](https://flask.palletsprojects.com/)

An end-to-end Machine Learning web application that predicts annual medical insurance costs with high precision. This project integrates **Predictive Analytics (DSBDA)** with **Modern Web Deployment (WT)**.

---

## 🚀 Key Highlights
* **Precision Modeling:** Trained on the Medical Cost dataset using Linear Regression.
* **Intelligent Encoding:** Automated handling of categorical variables like 'Smoker' and 'Region'.
* **Glassmorphism UI:** A sleek, modern frontend designed with high-end CSS for a premium user experience.
* **Cloud Native:** Fully deployed on Render with an automated CI/CD pipeline.

## 🛠️ Tech Stack
| Component | Technology |
| :--- | :--- |
| **Language** | Python (NumPy, Pandas) |
| **ML Engine** | Scikit-learn (Linear Regression) |
| **Backend** | Flask |
| **Frontend** | HTML5, CSS3 (Custom Responsive Design) |
| **Environment** | GitHub, Render, Gunicorn |

## 📊 How It Works
1. **Data Training:** The model was trained in Jupyter, reaching optimal weights for age, BMI, and lifestyle factors.
2. **Serialization:** The "brain" of the model is saved as `insurance_model.pkl`.
3. **Web Interface:** Users provide 6 key inputs (Age, BMI, Children, Smoker status, Sex, and Region).
4. **Prediction:** The Flask backend processes 7 distinct features (using One-Hot Encoding) to return a real-time dollar estimate.

## 💻 Installation & Local Setup
If you want to run this project locally:
```bash
# Clone the repository
git clone [https://github.com/premchavan-308/Insurance-Predictor-Project.git](https://github.com/premchavan-308/Insurance-Predictor-Project.git)

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
