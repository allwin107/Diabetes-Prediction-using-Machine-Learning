document.getElementById('predictionForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const formData = new FormData(e.target);
    const data = Object.fromEntries(formData.entries());
    
    const resultDiv = document.getElementById('result');
    const resultText = document.getElementById('resultText');
    const errorDiv = document.getElementById('error');
    
    // Hide previous results
    resultDiv.classList.add('hidden');
    errorDiv.classList.add('hidden');
    
    try {
        const response = await fetch('/api/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        });
        
        const result = await response.json();
        
        if (response.ok) {
            resultText.textContent = result.result;
            resultDiv.classList.remove('hidden');
            
            if (result.prediction === 1) {
                resultDiv.classList.add('positive');
                resultDiv.classList.remove('negative');
            } else {
                resultDiv.classList.add('negative');
                resultDiv.classList.remove('positive');
            }
        } else {
            throw new Error(result.error || 'Prediction failed');
        }
    } catch (error) {
        errorDiv.textContent = 'Error: ' + error.message;
        errorDiv.classList.remove('hidden');
    }
});
