# 🌾 Smart Irrigation Prediction Using Machine Learning

This project is a machine learning solution for predicting irrigation needs using environmental sensor data. It leverages a multi-label classification model to automate irrigation decisions, contributing to efficient water usage in agriculture.

---

## 🚀 Features

- Predicts multiple irrigation decisions from sensor inputs
- Data preprocessing and feature scaling
- Multi-label classification using `RandomForestClassifier`
- Model evaluation using classification metrics
- Model serialization with `joblib`

---

## 📁 Dataset

- **File**: `irrigation_data.csv`
- **Features**: 20 sensor columns (`sensor_0` to `sensor_19`)
- **Labels**: Multiple irrigation-related target variables

---

## 📊 Workflow

1. **Load & Preprocess Data**
   - Removed unnecessary columns
   - Normalized sensor values using `MinMaxScaler`

2. **Train-Test Split**
   - Split data into training and testing sets (using `train_test_split`)

3. **Model Training**
   - Trained a `RandomForestClassifier` wrapped in a `MultiOutputClassifier` to handle multiple outputs

4. **Evaluation**
   - Evaluated the model using `classification_report` from `sklearn`

5. **Model Saving**
   - Saved the trained model using `joblib` for future inference

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Seaborn
- Matplotlib

---

## 📌 How to Run

1. Clone the repository
2. Upload `irrigation_data.csv` to the root directory
3. Run the notebook `irrigation.ipynb` in Google Colab or Jupyter

---

## 📎 License

This project is open-source and available under the MIT License.

---

## 🤝 Contributions

Feel free to open issues or submit pull requests to improve this project!
