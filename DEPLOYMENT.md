# Deployment Guide

## Project Structure

```
├── api/                    # Backend API (Production)
│   └── predict.py         # Flask API endpoint
├── public/                # Frontend (Production)
│   ├── index.html        # Main HTML page
│   ├── script.js         # JavaScript logic
│   └── style.css         # Styling
├── diabetes.csv          # Training dataset (Development only)
├── diabetes_model.pkl    # Trained ML model (Production)
├── train_model.py        # Training script (Development only)
├── requirements.txt      # Python dependencies
├── vercel.json          # Vercel configuration
└── .gitignore           # Git ignore rules

```

## Local Testing

### 1. Install Python Dependencies

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Test the API Locally

```bash
# Run Flask development server
python api/predict.py
```

The API will be available at `http://localhost:5000`

### 3. Test the Frontend

Open `public/index.html` in your browser or use a local server:

```bash
# Using Python's built-in server
python -m http.server 8000 --directory public
```

Then visit `http://localhost:8000`

## Deploy to Vercel

### Prerequisites

- Node.js and npm installed
- Vercel account (free tier available)

### Installation Steps

1. **Install Vercel CLI**

```bash
npm install -g vercel
```

2. **Login to Vercel**

```bash
vercel login
```

3. **Deploy**

```bash
# From the project root directory
vercel

# For production deployment
vercel --prod
```

4. **Follow the prompts:**
   - Set up and deploy? **Y**
   - Which scope? Select your account
   - Link to existing project? **N**
   - Project name? (default or custom name)
   - In which directory is your code located? **.**
   - Want to override settings? **N**

### Alternative: Deploy via Vercel Dashboard

1. Go to [vercel.com](https://vercel.com)
2. Click "Add New Project"
3. Import your GitHub repository
4. Vercel will auto-detect the configuration from `vercel.json`
5. Click "Deploy"

## Environment Variables

No environment variables are required for this project.

## Testing the Deployed Application

Once deployed, Vercel will provide you with a URL (e.g., `https://your-project.vercel.app`).

Test the prediction with sample data:
- Pregnancies: 5
- Glucose: 166
- Blood Pressure: 72
- Skin Thickness: 19
- Insulin: 175
- BMI: 25.8
- Diabetes Pedigree Function: 0.587
- Age: 51

Expected result: **Diabetic**

## Troubleshooting

### API Returns 500 Error

- Check that `diabetes_model.pkl` is in the root directory
- Verify all dependencies are in `requirements.txt`
- Check Vercel deployment logs

### Frontend Not Loading

- Ensure `public/` directory contains all files
- Check browser console for errors
- Verify `vercel.json` routes configuration

### Model Not Found Error

- Ensure `diabetes_model.pkl` is committed to git
- Check file path in `api/predict.py`

## Development vs Production

**Development files (not deployed):**
- `venv/` - Virtual environment
- `diabetes.csv` - Training data
- `train_model.py` - Training script
- `Diabetes Prediction.ipynb` - Jupyter notebook

**Production files (deployed):**
- `api/` - Backend API
- `public/` - Frontend
- `diabetes_model.pkl` - Trained model
- `requirements.txt` - Dependencies
- `vercel.json` - Configuration

## Retraining the Model

To retrain the model with new data:

```bash
# Activate virtual environment
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # Linux/Mac

# Run training script
python train_model.py

# Commit and push the new model
git add diabetes_model.pkl
git commit -m "Update trained model"
git push

# Redeploy to Vercel
vercel --prod
```

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python, Flask, Flask-CORS
- **ML**: scikit-learn, pandas, numpy
- **Deployment**: Vercel (Serverless)
- **Model**: Support Vector Machine (SVM)

## Performance

- Model Accuracy: ~77%
- API Response Time: < 1s
- Serverless: Auto-scaling
- Global CDN: Fast worldwide access
