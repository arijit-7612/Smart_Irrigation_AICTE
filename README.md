🌾 Smart Irrigation System – Streamlit Web App
This project is an AI-powered irrigation management system built with Streamlit.
It predicts the ON/OFF status of 20 smart sprinklers based on real-time scaled sensor inputs (0 to 1), helping farmers optimize water usage efficiently.

🚀 Features
🖥️ Interactive Web UI using Streamlit

🔢 20 Sensor Inputs via sliders

💧 Multi-Sprinkler Prediction (ON/OFF for each parcel)

📊 Machine Learning Model trained with RandomForestClassifier

⚡ Instant Prediction without retraining the model

🛠️ Tech Stack
Python 3

Streamlit

NumPy

Scikit-learn

Joblib

📦 Project Structure
bash
Copy
Edit
Smart_Irrigation_AICTE/
│
├── app.py                       # Main Streamlit web app
├── Farm_Irrigation_System.pkl    # Trained ML model
├── irrigation_data.csv           # Dataset used for model training
├── irrigation.ipynb              # Model training notebook
├── requirements.txt              # Python dependencies for deployment
└── README.md                     # Project documentation
▶️ How to Run Locally
Clone the repository:

bash
Copy
Edit
git clone https://github.com/arijit-7612/Smart_Irrigation_AICTE.git
cd Smart_Irrigation_AICTE
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the Streamlit app:

bash
Copy
Edit
streamlit run app.py
Open the link shown in the terminal (usually http://localhost:8501).

