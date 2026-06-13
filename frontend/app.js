document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('prediction-form');
    const submitBtn = document.getElementById('submit-btn');
    const btnText = document.getElementById('btn-text');
    const spinner = document.getElementById('spinner');
    const resultContainer = document.getElementById('result-container');
    const errorContainer = document.getElementById('error-container');
    
    // API URL - change if deployed
    const API_URL = '/predict';

    // Sync Sliders and Number Inputs
    const syncInputs = (id) => {
        const slider = document.getElementById(id);
        const num = document.getElementById(`${id}_num`);
        
        slider.addEventListener('input', (e) => {
            num.value = e.target.value;
        });
        
        num.addEventListener('input', (e) => {
            slider.value = e.target.value;
        });
    };

    ['sepal_length', 'sepal_width', 'petal_length', 'petal_width'].forEach(syncInputs);

    // 3D Card Tilt Effect
    const card = document.querySelector('.card');
    document.addEventListener('mousemove', (e) => {
        const xAxis = (window.innerWidth / 2 - e.pageX) / 50;
        const yAxis = (window.innerHeight / 2 - e.pageY) / 50;
        card.style.transform = `perspective(1000px) rotateY(${xAxis}deg) rotateX(${yAxis}deg)`;
    });

    // Reset card transform on mouse leave
    document.addEventListener('mouseleave', () => {
        card.style.transform = `perspective(1000px) rotateY(0deg) rotateX(0deg)`;
    });

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        // Reset UI
        resultContainer.classList.add('hidden');
        errorContainer.classList.add('hidden');
        
        // Loading State
        submitBtn.disabled = true;
        btnText.textContent = 'Analyzing...';
        spinner.classList.remove('hidden');

        // Gather Data
        const payload = {
            sepal_length: parseFloat(document.getElementById('sepal_length').value),
            sepal_width: parseFloat(document.getElementById('sepal_width').value),
            petal_length: parseFloat(document.getElementById('petal_length').value),
            petal_width: parseFloat(document.getElementById('petal_width').value)
        };

        try {
            const response = await fetch(API_URL, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(payload)
            });

            if (!response.ok) {
                throw new Error(`Server returned ${response.status}`);
            }

            const data = await response.json();
            showResult(data);

        } catch (error) {
            console.error('Prediction Error:', error);
            showError('Failed to connect to the prediction API. Ensure the backend is running on port 8000.');
        } finally {
            // Restore UI
            submitBtn.disabled = false;
            btnText.textContent = 'Predict Species';
            spinner.classList.add('hidden');
        }
    });

    function showResult(data) {
        const resultName = document.getElementById('prediction-result');
        const confidenceBar = document.getElementById('confidence-bar');
        const confidenceText = document.getElementById('confidence-text');

        // Clean up formatting (e.g., 'Iris-setosa' -> 'Setosa')
        let speciesName = data.prediction.replace('Iris-', '');
        speciesName = speciesName.charAt(0).toUpperCase() + speciesName.slice(1);
        
        resultName.textContent = `Iris ${speciesName}`;

        // Calculate confidence if probabilities exist
        if (data.probabilities && data.probabilities.length > 0) {
            const maxProb = Math.max(...data.probabilities);
            const probPercentage = (maxProb * 100).toFixed(1);
            
            // Allow a tiny delay so the transition triggers smoothly from 0
            setTimeout(() => {
                confidenceBar.style.width = `${probPercentage}%`;
            }, 50);
            
            confidenceText.textContent = `${probPercentage}% Confidence`;
        } else {
            confidenceBar.style.width = '100%';
            confidenceText.textContent = 'Prediction successful';
        }

        resultContainer.classList.remove('hidden');
    }

    function showError(message) {
        document.getElementById('error-message').textContent = message;
        errorContainer.classList.remove('hidden');
    }
});
