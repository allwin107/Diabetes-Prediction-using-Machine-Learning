QUICK DEPLOYMENT GUIDE
======================

Since Node.js is not installed on your machine, here are the steps to deploy:

OPTION 1: Install Node.js and Deploy via CLI
---------------------------------------------
1. Download and install Node.js from: https://nodejs.org/
2. Restart your terminal
3. Run: npm install -g vercel
4. Run: vercel login
5. Run: vercel --prod

OPTION 2: Deploy via Vercel Dashboard (RECOMMENDED - NO NODE.JS NEEDED)
------------------------------------------------------------------------
1. Go to https://vercel.com and sign up/login
2. Click "Add New Project"
3. Click "Import Git Repository"
4. Select your GitHub repository: Diabetes-Prediction-using-Machine-Learning
5. Vercel will auto-detect the configuration
6. Click "Deploy"
7. Wait for deployment to complete
8. You'll get a live URL like: https://diabetes-prediction-xyz.vercel.app

WHAT WAS DONE:
--------------
✓ Created Python virtual environment
✓ Installed all dependencies (numpy, pandas, scikit-learn, flask, flask-cors)
✓ Trained the SVM model successfully (77% accuracy)
✓ Created web interface (HTML, CSS, JavaScript)
✓ Created Flask API endpoint
✓ Configured for Vercel deployment
✓ Added .gitignore to exclude development files
✓ Committed and pushed to GitHub

PROJECT STRUCTURE:
------------------
Production files (deployed):
  - api/predict.py (Flask API)
  - public/index.html, script.js, style.css (Frontend)
  - diabetes_model.pkl (Trained model)
  - requirements.txt (Dependencies)
  - vercel.json (Deployment config)

Development files (ignored):
  - venv/ (Virtual environment)
  - diabetes.csv (Training data)
  - train_model.py (Training script)
  - Diabetes Prediction.ipynb (Notebook)

TESTING LOCALLY:
----------------
1. Activate venv: venv\Scripts\activate
2. Run API: python api/predict.py
3. Open public/index.html in browser

NEXT STEPS:
-----------
Use Option 2 above to deploy to Vercel without needing Node.js!
