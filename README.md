# 🩺 Diabetes Prediction using Machine Learning (SVM)

This project uses Support Vector Machine (SVM), a supervised machine learning algorithm, to predict whether a person is likely to have diabetes based on certain diagnostic health measurements. The dataset used for training the model was obtained from Kaggle.

## 📊 Dataset

The dataset is the **Pima Indians Diabetes Database**, a popular dataset from [Kaggle](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database), containing several medical predictor variables and one target variable indicating whether or not a patient has diabetes.

### Features include:
- Pregnancies
- Glucose
- Blood Pressure
- Skin Thickness
- Insulin
- BMI
- Diabetes Pedigree Function
- Age

## 🧠 Model Used

- **Support Vector Machine (SVM)**: A powerful classification algorithm effective for high-dimensional spaces and commonly used for classification tasks.

## ⚙️ Installation

1. Clone the repository:
```bash
git clone https://github.com/allwin107/Diabetes-Prediction-using-Machine-Learning.git
cd Diabetes-Prediction-using-Machine-Learning
```
2. Install dependencies:

```bash
pip install -r requirements.txt
```
## 🚀 How to Run

Run the prediction script:

```bash
python diabetes_prediction.py
```
Make sure diabetes.csv is in the same directory as the script.

## ✅ Accuracy
The SVM model achieved good accuracy on the test data 78%.

## 💾 Model Saving
The trained model is saved using pickle for later use in deployment or integration into applications.

## 🧪 Future Improvements
Integrate with a web app using Flask or Streamlit

Add cross-validation and hyperparameter tuning

Implement other models for comparison (e.g., Random Forest, Logistic Regression)
